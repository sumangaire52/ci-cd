from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
	return {"message": "CI/CD is working"}