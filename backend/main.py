from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from data import jobs

app = FastAPI()

# Allow frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this to your Angular URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the expected request schema using Pydantic
class Job(BaseModel):
    id: int
    title: str
    company: str
    location: str
    salary: str

@app.get("/api/jobs")
def get_jobs():
    return jobs

@app.post("/api/jobs")
def add_job(job: Job):
    jobs.append(job.dict())
    return {"message": "Job added successfully", "job": job}

