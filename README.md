Autonomous AI Document Generation Agent

Overview

This project is an Autonomous AI Agent that understands a user's business request, creates its own execution plan, generates professional business content using a Large Language Model (LLM), and produces a polished Microsoft Word (".docx") document.

The project demonstrates autonomous planning, task execution, document generation, and API-based interaction using FastAPI.

---

Features

- Accepts business requests through a REST API
- Generates an autonomous execution plan
- Uses Google Gemini LLM for content generation
- Creates professional Microsoft Word documents
- Modular and extensible architecture
- FastAPI-based API interface

---

Tech Stack

- Python
- FastAPI
- Google Gemini API
- python-docx
- Pydantic
- Uvicorn
- python-dotenv

---

Project Structure

project/
│── app.py                  # FastAPI application
│── agent.py                 # Autonomous agent workflow
│── document_generator.py    # DOCX generation
│── requirements.txt
│── .env
│── output/
│     └── generated_document.docx

---

Installation

1. Clone the repository

git clone <repository-url>
cd project

2. Install dependencies

pip install -r requirements.txt

3. Configure environment variables

Create a ".env" file:

GOOGLE_API_KEY=your_google_gemini_api_key

---

Running the Application

Start the FastAPI server:

uvicorn main:app --reload

The API will be available at:

http://127.0.0.1:8000

Swagger UI:

http://127.0.0.1:8000/docs

---

API Endpoint

POST "/agent"

Request:

{
  "request": "Create a proposal for implementing an AI-powered customer support chatbot."
}

Response:

{
  "status": "success",
  "message": "Agent completed execution",
  "plan": [
    "Analyze user request",
    "Identify document type",
    "Generate business content",
    "Review content",
    "Create Word document"
  ],
  "generated_document": "AI_Generated_Business_Report.docx"
}

---

Agent Workflow

1. Receive user request
2. Analyze the requirement
3. Generate an execution plan
4. Generate business content using the LLM
5. Create the Microsoft Word document
6. Return the execution plan and document path

---

Output

The agent generates:

- Agent execution plan
- Professional business document
- Microsoft Word (".docx") file

---

Future Enhancements

- Multi-agent architecture
- LangGraph integration
- Memory support
- Retrieval-Augmented Generation (RAG)
- PDF export
- Cloud deployment
- Authentication and user management

---

Requirements

fastapi
uvicorn
google-generativeai
python-docx
python-dotenv
pydantic
