# FastAPI Chat with Docs Apps Tutorial

This tutorial will guide you through setting up a basic FastAPI application for handling questions with documentation. The tutorial covers both local development and deployment to the Fly.io platform.

# SuperDuperDB Question The Docs - Prerequisites

Before proceeding with building a RAG (Retrieve, Ask, Generate) app using SuperDuperDB, please follow these prerequisites to set up your environment.

## 1. Run Jupyter Notebook - "Question the Doc"

To prepare your MongoDB database for the SuperDuperDB Question The Docs API, you need to run the Jupyter Notebook named [Question the Doc](https://github.com/SuperDuperDB/superduperdb/blob/main/examples/question_the_docs.ipynb). This notebook adds vector indexes to your existing MongoDB database.

Please follow the steps below:

- Open the [Question the Doc Jupyter Notebook](https://github.com/SuperDuperDB/superduperdb/blob/main/examples/question_the_docs.ipynb).
- Run each cell in the notebook to execute the necessary operations.
- This process will make your MongoDB database ready to work seamlessly with the SuperDuperDB Question The Docs API.
- Run it often to update the database.

## 2. Explore Sample Data

To understand the kind of data used in the SuperDuperDB Question The Docs API, you can explore the [sample data](https://jupyter-sessions.s3.us-east-2.amazonaws.com/superduperdb_docs_v1.json). This JSON file provides insights into the structure and content of the data.

You can use this information to tailor your RAG app based on your requirements.

## 3. Build Your RAG App

The implementation provided focuses on building a chat-with-the-docs app using SuperDuperDB. However, the API can be adapted to create various RAG applications. Feel free to improvise and customize the app to suit your needs.

### Important Note:

- Ensure that you have the necessary environment variables (OPENAI_API_KEY, MONGODB_URI) set up as per the API documentation.
- For any assistance or queries, you can join our Slack channel.

By completing these prerequisites, you'll be ready to build and deploy your RAG app using the SuperDuperDB Question The Docs API.

## Let's make an API for production

Before you begin, make sure you have the following installed on your machine:

- [Python](https://www.python.org/) (>= 3.7)
- [Docker](https://www.docker.com/) (optional for Docker deployment)
- [Flyctl](https://fly.io/docs/flyctl/install/) (optional for Fly.io deployment)

## Step 1: Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/SuperDuperDB/chat-with-your-docs-backend.git
cd chat-with-your-docs-backend
```

## Step 2: Set Up Environment Variables

Create a file named `.env` in the project root and add the following content:

```dotenv
OPENAPI_API_KEY=YOUR_OPENAPI_API_KEY
MONGODBQTD_URI=YOUR_MONGODB_URI
```

Replace `YOUR_OPENAPI_API_KEY` with your OpenAPI API key and `YOUR_MONGODB_URI` with your MongoDB URI.

## Step 3: Set Up Virtual Environment

Open PowerShell or Command Prompt and navigate to your project directory:

```bash
cd C:\path\to\your\project
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

```bash
.\venv\Scripts\Activate  # Windows Powershell
# OR
source venv/bin/activate  # MacOS/Linux
```

## Step 4: Install Dependencies

Install the project dependencies using:

```bash
pip install -r requirements.txt
```

## Step 5: Run the Application Locally

Run the FastAPI application locally:

```bash
python -m dotenv run uvicorn main:app --host 127.0.0.1 --port 8081 --reload
```

Now you can access the application at [http://localhost:8081/docs](http://localhost:8081/docs).

## Docker Deployment

### Step 6: Build Docker Image

Build the Docker image from the project directory:

```bash
docker build -t chatwithdoc .
```

### Step 7: Run Docker Container

Run the Docker container with environment variables:

```bash
docker run --env-file .env -p 8080:8080 chatwithdoc
```

Access the application at [http://localhost:8080/docs](http://localhost:8080/docs).

## Fly.io Deployment (Optional)

### Step 8: Deploy to Fly.io

If you haven't already, install Flyctl:

```bash
flyctl install
```

Deploy your application to Fly.io:

Before deploying update and add these environment variables in your `fly.toml` file. You can add secrets as well from the `fly` dashboard.

```bash
# Update this env
[env]
  MONGODB_URI = "mongodb+srv://username:password@xxx.xxx.mongodb.net/?retryWrites=true&w=majority"
  OPENAI_API_KEY = "sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
```

```bash
flyctl launch
```

### Step 9: Update Deployment

To update your deployment regularly, use the following command:

```bash
flyctl deploy # Add "--local-only" if you want to build locally instead of flyctls remote set up 
```

That's it! You've successfully set up a FastAPI application for handling questions with documentation, and you have the option to deploy it locally, with Docker, or on the Fly.io platform. Feel free to explore and modify the application according to your needs.
_____________________________________________________________

# API Documentation

## SuperDuperDB Question The Docs API Documentation

## Overview

The SuperDuperDB Question The Docs API allows you to query and interact with the database using a simple and powerful API. This documentation provides details on how to make requests and interpret responses.

### Base URL

The base URL for the API is: `https://chat-with-your-docs-backend-3-spring-bush-7707.fly.dev/query`

## Query Endpoint

### `POST /query`

#### Summary

Submit a query to retrieve data from the SuperDuperDB.


#### Request

- **Method:** `POST`
- **Content-Type:** `application/json`
- **Required Request Body:**
  - Schema: `Query`
  - Content: `application/json`

##### Request Body Schema: `Query`

```json
{
  "query": "string",
  "collection_name": "string"
}
```

- `query` (string, required): The query string to retrieve data.
- `collection_name` (string, required): The name of the collection to query.

## Example

### Request

```http
POST /query HTTP/1.1
Host: https://chat-with-your-docs-backend-3-spring-bush-7707.fly.dev
Content-Type: application/json

{
  "query": "What is CDC?",
  "collection_name": "user_data"
}
```

### `Output`

```json
{
  "answer": "CDC stands for Change Data Capture. In the context of SuperDuperDB, CDC refers to the process of capturing and tracking changes made to data in a database.\n\nCode snippet 1:\n```\nfrom superduperdb import CDC\n\ncdc = CDC(\"my_database\")\n```\n\nCode snippet 2:\n```\ncdc.start_capturing()\n```\n\nCode snippet 3:\n```\ncdc.stop_capturing()\n```\n\nBased on the code snippets provided, it seems that SuperDuperDB has a CDC feature implemented. Code snippet 1 initializes a CDC object with the name \"my_database\". Code snippet 2 starts capturing changes, and code snippet 3 stops the capturing process.",
  "source_urls": [
    "https://docs.superduperdb.com"
  ]
}
```

- `answer` (string): Retrieved data.
- `source_urls` (list): Source URLS

---

Feel free to use this documentation to interact with the SuperDuperDB Question The Docs API. Keep your MongoDB database updated by running the Jupyter Notebook regularly.

Now connect the app to your frontend. And let us know. 