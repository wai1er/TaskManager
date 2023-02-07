from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi import Response
from fastapi import status

from .. import models
from ..services.auth import get_current_user
from ..services.tasks import TasksService

router = APIRouter(
    prefix='/tasks',
    tags=['tasks']
)


@router.get('/', response_model=List[models.Task])
def get_tasks(user: models.User = Depends(get_current_user), service: TasksService = Depends()):
    return service.get_list(user.id)


@router.get('/{task_id}', response_model=models.Task)
def get_task(task_id: int, user: models.User = Depends(get_current_user), service: TasksService = Depends()):
    return service.get(user.id, task_id)


@router.post('/', response_model=models.Task, status_code=status.HTTP_201_CREATED)
def create_task(task_data: models.TaskCreate, user: models.User = Depends(get_current_user),
                service: TasksService = Depends()):
    return service.create(user.id, task_data)


@router.put('/{task_id}', response_model=models.Task)
def update_task(task_id: int, task_data: models.TaskUpdate, user: models.User = Depends(get_current_user),
                service: TasksService = Depends()):
    return service.update(user.id, task_id, task_data)


@router.delete('/{task_id}')
def delete_task(task_id: int, user: models.User = Depends(get_current_user), service: TasksService = Depends()):
    service.delete(user.id, task_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
