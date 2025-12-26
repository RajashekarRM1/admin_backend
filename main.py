from fastapi import FastAPI
from routes.user_route import router as user_router
from routes.application_route import router as application_router
from routes.master_route import router as master_router

app = FastAPI()

app.include_router(user_router)
app.include_router(application_router)
app.include_router(master_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Admission API"}