## Task 2

Create a simple fast API that takes the first and last name of a user and returns the user's full name

## To run

Clone the repo

```bash
git clone https://github.com/dotAadarsh/pre-program-tasks.git
```

Switch to task 2 branch

```bash
git checkout taskID_3
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

To send a POST request to the endpoint using `curl`, open a new terminal and enter the following command.

```bash
curl -X POST "http://127.0.0.1:8000/pdf/upload/" -H "accept: application/json" -H "Content-Type: multipart/form-data" -F "file=@path/to/your/file.pdf"
```

Replace "path/to/your/file.pdf" with the actual path to the PDF file you want to upload. Once you send the request, the files will be added in the uploaded_pdfs folder. 


## References
- https://fastapi.tiangolo.com/tutorial/bigger-applications/
- https://www.uvicorn.org/
- https://fastapi.tiangolo.com/reference/uploadfile/
- https://fastapi.tiangolo.com/tutorial/request-files/