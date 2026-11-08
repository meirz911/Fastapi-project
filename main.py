from fastapi import FastAPI

from routers.tasks import router as tasks_router

app = FastAPI(
    title="Task Manager",
    description="Первый API на FastAPI: список задач хранится в памяти",
    version="1.0.0",
)
app.include_router(tasks_router)


@app.get("/", summary="Root")
def root():
    return {"message": "Task Manager API"}


@app.get("/ping", summary="Health check")
def ping():
    return {"status": "ok"}