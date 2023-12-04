from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

mongodb_uri = os.getenv("MONGODB_URI")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

from superduperdb import superduper
from superduperdb import Document
from superduperdb.backends.mongodb import Collection
from superduperdb.ext.openai import OpenAIChatCompletion

# It just super dupers your database
db = superduper(mongodb_uri)

# Define the prompt for the OpenAIChatCompletion model
prompt = (
    "Use the following description and code snippets about SuperDuperDB to answer this question about SuperDuperDB\n"
    "Do not use any other information you might have learned about other python packages\n"
    "Only base your answer on the code snippets retrieved and provide a very concise answer\n"
    "{context}\n\n"
    "Here's the question:\n"
)

# Create an instance of OpenAIChatCompletion with the specified model and prompt
chat = OpenAIChatCompletion(model="gpt-3.5-turbo", prompt=prompt)

# Add the OpenAIChatCompletion instance
db.add(chat)

# Create a FastAPI app instance with version, description, and lifespan manager
app = FastAPI(
    title="SuperDuperDB Question The Docs",
)

# Configure Cross-Origin Resource Sharing (CORS) settings
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Query(BaseModel):
    query: str
    collection_name: str


# Endpoint for showing components in the database
@app.post("/query")
async def show(payload: Query):
    # Define the search parameters
    search_term = payload.query
    # Select the collection
    collection = Collection("questiondocs")

    # search_term = "Can you give me a code-snippet to set up a `VectorIndex`?"

    num_results = 5

    # Use the SuperDuperDB model to generate a response based on the search term and context
    output, context = db.predict(
        model_name="gpt-3.5-turbo",
        input=search_term,
        context_select=(
            collection.like(
                Document({"txt": search_term}), vector_index="my-index", n=num_results
            ).find()
        ),
        context_key="txt",
    )

    return {"answer": output.content, "source_urls": ["https://docs.superduperdb.com"]}
