from fastapi import FastAPI, UploadFile, File
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
import uuid

app = FastAPI()

# MongoDB Connection
client = AsyncIOMotorClient("mongodb://db:27017")
db = client.healthcare_db

class Appointment(BaseModel):
    pid: str
    doctor_name: str
    date: str

@app.post("/register")
async def register_patient(name: str):
    pid = str(uuid.uuid4())[:8] # Generate short unique PID
    patient = {"pid": pid, "name": name, "reports": []}
    await db.patients.insert_one(patient)
    return {"pid": pid, "message": "Patient registered successfully"}

@app.post("/book")
async def book_appointment(appointment: Appointment):
    await db.appointments.insert_one(appointment.dict())
    return {"status": "Success", "appointment": appointment}

@app.get("/patient/{pid}")
async def get_records(pid: str):
    patient = await db.patients.find_one({"pid": pid})
    return patient if patient else {"error": "Patient not found"}
