from fastapi import FastAPI

app = FastAPI()

@app.get("/welcome") # It means that when someone enter /welcome in the URL it will execute the function next to it
def welcome():
    return {
        "message": "Hello World!"
    }