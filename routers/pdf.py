from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import os

router = APIRouter()

@router.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):
    try:
        if file.content_type != "application/pdf":
            raise HTTPException(status_code=400, detail="Only PDF files are allowed.")
        
        # Set the path to store the uploaded PDF files
        upload_folder = "uploaded_pdfs"
        os.makedirs(upload_folder, exist_ok=True)

        # Save the file to disk
        file_path = os.path.join(upload_folder, file.filename)
        with open(file_path, "wb") as pdf_file:
            pdf_file.write(file.file.read())

        return JSONResponse(content={
            "message": "File uploaded successfully",
            "file_path": file_path
            })
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))