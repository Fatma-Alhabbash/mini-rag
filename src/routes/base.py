from fastapi import FastAPI, APIRouter
import os # Because load_dotenv loads the variables and saves them in the OS

base_router = APIRouter(
    prefix = "/api/v1",  # This used to add this prefix before all the routes under that base_router
    tags = ["api_v1"]    # All the following routes will be under that tag 
)

@base_router.get("/") # It means that when someone enter / (default route) in the URL it will execute the function next to it
async def welcome():  # This improves the performance of the FastAPI and uvicorn to handle multiple requests together
    app_name = os.getenv("APP_NAME")
    app_version = os.getenv("APP_VERSION")

    return {
        "app_name": app_name,
        "app_version": app_version
    }