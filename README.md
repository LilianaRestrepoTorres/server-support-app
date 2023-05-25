# AI Support Tickets System :robot: 

This is an AI-powered Support Tickets system built in Python with Flask. This application accepts a report of an issue in natural language format, analyzes it using an GPT3.5-turbo AI model, and creates a ticket. You can then **retrieve all tickets**, check the **status of a specific ticket** or **update the status of a ticket**.

![Flask-Powered](https://img.shields.io/badge/Powered_by-Flask-blue)
![Python Version](https://img.shields.io/badge/Python-3-green)
[![Powered by AI](https://img.shields.io/badge/Powered%20by-Artificial%20Intelligence-33ccff.svg)](https://openai.com/)

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation and Usage](#installationandusage)
- [Endpoints](#endpoints)
- [Features](#features)

## Prerequisites

Ensure you have the following installed on your local machine:

- Python 3.0+ 
- pip

## Installation and Usage
1. Clone the repository: `git clone https://github.com/LilianaRestrepoTorres/server-support-app.git`
2. Navigate into the cloned repository: `cd server-support-app`
3. Create a virtual environment: `python3 -m venv venv`
4. Add dependencies to the environment:
      ```bash
      pip3 install Flask
      pip install flask_restful
      pip install openai
      pip install python-dotenv
      pip install -U flask-cors
      ```
5. Activate the virtual environment: `source venv/bin/activate`
6. Run the application: `python3 server.py`

Now you should be able to access the application at `http://localhost:5000/`

## Endpoints

| Endpoint | Description | Method |
| --- | --- | --- |
| `/report` | Reports an issue | POST |
| `/tickets` | Returns all the tickets | GET |
| `/ticket_status/<string:ticket_id>` | Returns the status of a given ticket | GET |
| `/update_status/<ticket_id>` | Updates the status of a given ticket | PATCH |



https://github.com/LilianaRestrepoTorres/server-support-app/assets/17114826/56e08199-f6d5-4aab-aa9a-687357b473a5


## Key Features
- **AI Content Generation:** The system accepts natural language reports of problems with bots or orders. Then, process the input to extract **problem location**, **problem type** (software, hardware, or field) and a **summary** of the issue.
- **Support during AI Model Downtime:** We've added error handling to ensure continuous operation even when the GPT-3.5-turbo is offline or at its request limit. We support this feature by creating tickets for prompt assistance.
- **Data Persistence:** The application application stores data locally in a JSON file. It's a starting point for future improvements.


Enjoy using the AI Support Ticket System! :rocket:

---
 Built with 💚 by me.
