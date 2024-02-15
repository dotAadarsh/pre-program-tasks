from fastapi import FastAPI

# Import the router
from routers import pdf

# Create a FastAPI instance
app = FastAPI()

# Mount the PDF router at the "/pdf" prefix with "PDF" tag for documentation
app.include_router(pdf.router, prefix="/pdf", tags=["PDF"])
