from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


# uvicorn main:app --reload

# import uvicorn
# if __name__ == "__main__":
#     uvicorn.run(app)
