from flask import Flask, request, jsonify
from uuid import uuid4
from openai_utils import ai_extract_ticket_info
from storage_utils import write_ticket_to_file, read_ticket_from_file, update_ticket_status, get_all_tickets
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Endpoint to report a problem
@app.route('/report', methods=['POST'])
def report_issue():
  description = request.json.get("description")
  bot_data = request.json.get("bot_data")
  problem_type, problem_location, summary = ai_extract_ticket_info(description, bot_data)
  ticket_id = str(uuid4())
  ticket = {
    "ticket_id": ticket_id,
    "problem_location": problem_location,
    "problem_type": problem_type.lower(),
    "description_prompt": description,
    "summary": summary,
    "bot_id": bot_data["bot_id"],
    "status": "open"
  }
  write_ticket_to_file(ticket)

  return jsonify(ticket), 201

# Endpoint to get all tickets
@app.route('/tickets')
def get_tickets():
  tickets = get_all_tickets()
  return jsonify(tickets)

# Endpoint to get the Status of a ticket by its ID
@app.route('/ticket_status/<string:ticket_id>', methods=['GET'])
def get_ticket_status(ticket_id):
  ticket = read_ticket_from_file(ticket_id)

  if ticket is None:
    return jsonify({"error": "Ticket not found"}), 404
  
  return jsonify({"status": ticket["status"]})

# Endpoint to update the Status of a ticket by its ID
@app.route('/update_status/<ticket_id>', methods=['PATCH'])
def update_status(ticket_id):
  new_status = request.json['status']

  # Update the ticket status in the file
  success = update_ticket_status(ticket_id, new_status)

  if not success:
    return jsonify({"error": "Ticket not found"}), 404

  return jsonify({"status": new_status})


if __name__ == '__main__':
  app.run(debug=True)