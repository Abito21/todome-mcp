from fastapi import FastAPI
from app.database import create_db_and_tables
from app.router import router

app = FastAPI(
    title="Simple Todos API",
    description="A super simple todos API with CRUD operations",
    version="1.0.0"
)

# Include the todos router
app.include_router(router)

@app.on_event("startup")
def on_startup():
    """Create database tables on startup"""
    create_db_and_tables()

@app.get("/")
def root():
    """Root endpoint"""
    return {"message": "Welcome to Simple Todos API"}

@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}