## Task 2

Create a simple fast API that takes the first and last name of a user and returns the user's full name

## To run

Clone the repo

```bash
git clone https://github.com/dotAadarsh/pre-program-tasks.git
```

Switch to task 2 branch

```bash
git checkout taskID_2
```

Install the dependencies

```bash
pip install -r requirements.txt
```

To run the application, enter the following command in your terminal:

```bash
uvicorn main:app --reload
```

The above command will start the FastAPI application, and you can access it at http://127.0.0.1:8000/docs to interact with the Swagger documentation or http://127.0.0.1:8000/redoc for the ReDoc documentation.

you can test the API by visiting http://127.0.0.1:8000/name?first_name=Aadarsh&last_name=Kannan in your browser. You can change the values of the first_name and last_name parameters in the URL to see different results.

## References
- https://fastapi.tiangolo.com/tutorial/bigger-applications/
- https://www.uvicorn.org/