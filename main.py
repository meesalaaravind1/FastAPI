from fastapi import FastAPI

app= FastAPI()

@app.get('/')
def root():
    return {"data":{"returnedData":"Hey!! Welcome to Fast API"}}

@app.get("/about")
def about():
    return {"data":"this is about page"}