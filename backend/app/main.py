from fastapi import FastAPI
from app.routes import recommend

app = FastAPI()
app.include_router(recommend.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Recommendation API"}
