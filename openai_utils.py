import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('OPENAI_KEY')

VALID_PROBLEM_TYPES = {"software", "hardware", "field"}

def ai_extract_ticket_info(description, bot_data):
  # Initialize variables to default values
  problem_type = None
  location = None
  summary = None

  try:
    # Prompt for GPT-3.5-turbo
    prompt = f"A customer reported an issue with a Kiwibot. The problem description is as follows:\n\n{description}\n\n"

    if bot_data and bot_data.get("location"):
      prompt += f"The bot's current location based on its data is: latitude {bot_data['location']['lat']}, longitude {bot_data['location']['lon']}.\n\n"
    else:
      prompt += "There's no bot location data available.\n\n"
    
    prompt += "Please provide the following details based on the problem description:\n\n1. Problem type (software, hardware, or field)\n2. Location (if not already provided by bot data)\n3. Brief summary of the issue."

    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[{"role": "assistant", "content": prompt }]
    )

    # We expect GPT-3 to respond in the format:
    # 1. Problem type: X
    # 2. Location: Y
    # 3. Brief summary: Z
    parsed_response = response.choices[0]['message']['content'].split("\n")
    problem_type = parsed_response[0].split(": ")[1]
    if problem_type.lower() not in VALID_PROBLEM_TYPES:
      problem_type = "unknown"

    location = parsed_response[1].split(": ")[1]
    if bot_data and bot_data.get("location") and location == 'not provided':
      location = bot_data['location']
    summary = parsed_response[2].split(": ")[1]

  except Exception as e:
    print(f"Exception occurred: {str(e)}")
    #In the event that there is a problem with GPT-3.5 resulting in an error or a limit on requests
    #These variables are populated with local functions 
    problem_type = determine_problem_type(description)
    summary = description
    location = "Unknown"
    if bot_data and bot_data.get("location"):
      location = f"Latitude {bot_data['location']['lat']}, longitude {bot_data['location']['lon']}."

  return problem_type, location, summary

# Manual version of the function to extract ticket data
def extract_ticket_info(description, bot_data):
  problem_type = determine_problem_type(description)
  problem_location = f"Latitude {bot_data['location']['lat']}, longitude {bot_data['location']['lon']}."
  summary = description
  return problem_type, problem_location, summary

def determine_problem_type(description):
  keywords_software = ['software', 'code', 'bug']
  keywords_hardware = ['hardware', 'device', 'physical']
  keywords_field = ['field', 'environment', 'outdoors']

  if any(keyword in description for keyword in keywords_software):
    return 'software'
  elif any(keyword in description for keyword in keywords_hardware):
    return 'hardware'
  elif any(keyword in description for keyword in keywords_field):
    return 'field'
  else:
    return 'unknown'