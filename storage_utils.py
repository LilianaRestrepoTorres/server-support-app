import json

def write_ticket_to_file(ticket, filename='tickets.json'):
  try:
    with open(filename, 'r') as f:
      tickets = json.load(f)
  except (FileNotFoundError, json.JSONDecodeError):
    # If the file doesn't exist or is empty, start with an empty list
    tickets = []

  tickets.append(ticket)

  # Write the tickets back to the file
  with open(filename, 'w') as f:
    json.dump(tickets, f)

def read_ticket_from_file(ticket_id, filename='tickets.json'):
  try:
    with open(filename, 'r') as f:
      tickets = json.load(f)
  except (FileNotFoundError, json.JSONDecodeError):
    # If the file doesn't exist or is empty, there are no tickets
    return None

  # Find the ticket with the matching ID
  for ticket in tickets:
    if ticket['ticket_id'] == ticket_id:
      return ticket

  # If no ticket was found, return None
  return None

def update_ticket_status(ticket_id, new_status, filename='tickets.json'):
  found_ticket = False
  try:
    with open(filename, 'r') as f:
      tickets = json.load(f)
  except (FileNotFoundError, json.JSONDecodeError):
    # If the file doesn't exist or is empty, there are no tickets
    return False

  # Find the ticket with the matching ID and update its status
  for ticket in tickets:
    if ticket['ticket_id'] == ticket_id:
      ticket['status'] = new_status
      found_ticket = True
      break

  # Write the tickets back to the file
  with open(filename, 'w') as f:
    json.dump(tickets, f)

  return found_ticket

def get_all_tickets(filename='tickets.json'):
  """
  Retrieves all tickets from the JSON file.
  """
  try:
    with open(filename, 'r') as f:
      tickets = json.load(f)
  except (FileNotFoundError, json.JSONDecodeError):
    # If the file doesn't exist or is empty, return an empty list
    return []

  return tickets
