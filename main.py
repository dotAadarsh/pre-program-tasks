# Import the FastAPI Library
from fastapi import FastAPI

app = FastAPI() # Create an instance

# Define a path operation for the root endpoint
@app.get("/")
def hello():
    return {"message": "Hello there!"}

# Define a path operation for the /name endpoint
@app.get("/name")
def get_full_name(first_name: str, last_name: str):
    # Concatenate the first and second name
    full_name = first_name + " " + last_name

    # Return the full name as a JSON obj
    return {"full_name": full_name}
