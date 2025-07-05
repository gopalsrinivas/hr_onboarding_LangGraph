from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.core.database import Base, engine
from app.routes.employee_routes import router as employee_router
from app.logger.logger import setup_logger

# Initialize logger
logger = setup_logger("main")

# Initialize FastAPI app
app = FastAPI(title="HR Onboarding API")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ⚠️ Allow all for development, restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include employee-related routes
app.include_router(employee_router, prefix="/employee", tags=["Employee"])


# Health check endpoint
@app.get("/health", tags=["Health"])
def health_check():
    """
    Health check endpoint to verify API is running
    """
    logger.info("Health check endpoint accessed.")
    return {"status": "OK", "message": "API is healthy"}


# Startup event: Create tables
@app.on_event("startup")
def startup_event():
    try:
        logger.info("Starting application...")
        logger.info("Creating database tables if they don't exist...")
        Base.metadata.create_all(bind=engine)
        logger.info("Database setup complete.")
    except Exception as e:
        logger.error(f"Error during startup: {e}")
        raise


# Shutdown event: Cleanup if needed
@app.on_event("shutdown")
def shutdown_event():
    logger.info("Shutting down application...")


# Global exception handler for uncaught errors
@app.middleware("http")
async def global_exception_handler(request: Request, call_next):
    try:
        response = await call_next(request)
        return response
    except Exception as e:
        logger.error(f"Unhandled exception: {e}")
        return JSONResponse(
            status_code=500,
            content={"detail": "Internal Server Error. Please contact support."},
        )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
