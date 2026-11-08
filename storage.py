tasks = [
    {"id": 1, "title": "Eat", "done": True},
    {"id": 2, "title": "Work", "done": False},
    {"id": 3, "title": "Sleep", "done": True},
]


def next_id() -> int:
    return max((task["id"] for task in tasks), default=0) + 1


def find_task(task_id: int) -> dict | None:
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None