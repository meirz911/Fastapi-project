from fastapi import APIRouter, HTTPException, Query, Response

from schemas import TaskCreate, TaskOut, TaskReplace, TaskUpdate
from storage import find_task, next_id, tasks

router = APIRouter(prefix="/tasks", tags=["tasks"])

NOT_FOUND = {404: {"description": "Task not found"}}


def get_or_404(task_id: int) -> dict:
    task = find_task(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.get("", response_model=list[TaskOut], summary="List tasks")
def list_tasks(
    done: bool | None = Query(default=None, description="Фильтр по статусу"),
    limit: int = Query(default=100, ge=1, le=100, description="Максимум задач"),
):
    result = tasks if done is None else [t for t in tasks if t["done"] == done]
    return result[:limit]


@router.get(
    "/{task_id}",
    response_model=TaskOut,
    responses=NOT_FOUND,
    summary="Get one task",
)
def get_task(task_id: int):
    return get_or_404(task_id)


@router.post(
    "",
    response_model=TaskOut,
    status_code=201,
    summary="Create task",
)
def create_task(data: TaskCreate):
    task = {"id": next_id(), "title": data.title, "done": data.done}
    tasks.append(task)
    return task


@router.put(
    "/{task_id}",
    response_model=TaskOut,
    responses=NOT_FOUND,
    summary="Replace task",
)
def replace_task(task_id: int, data: TaskReplace):
    task = get_or_404(task_id)
    task["title"] = data.title
    task["done"] = data.done
    return task


@router.patch(
    "/{task_id}",
    response_model=TaskOut,
    responses=NOT_FOUND,
    summary="Update task partially",
)
def update_task(task_id: int, data: TaskUpdate):
    task = get_or_404(task_id)
    if data.title is not None:
        task["title"] = data.title
    if data.done is not None:
        task["done"] = data.done
    return task


@router.delete(
    "/{task_id}",
    status_code=204,
    responses=NOT_FOUND,
    summary="Delete task",
)
def delete_task(task_id: int):
    task = get_or_404(task_id)
    tasks.remove(task)
    return Response(status_code=204)