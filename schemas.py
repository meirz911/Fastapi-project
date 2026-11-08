from pydantic import BaseModel, Field


class TaskCreate(BaseModel):
    title: str = Field(
        min_length=3,
        max_length=100,
        description="Название задачи",
        examples=["Read a book"],
    )
    done: bool = Field(default=False, description="Выполнена ли задача")


class TaskReplace(BaseModel):
    title: str = Field(
        min_length=3,
        max_length=100,
        description="Название задачи",
        examples=["Read a book"],
    )
    done: bool = Field(description="Выполнена ли задача")


class TaskUpdate(BaseModel):
    title: str | None = Field(
        default=None,
        min_length=3,
        max_length=100,
        description="Новое название (если нужно изменить)",
    )
    done: bool | None = Field(
        default=None,
        description="Новый статус (если нужно изменить)",
    )


class TaskOut(BaseModel):
    id: int
    title: str
    done: bool