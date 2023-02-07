from fastapi import APIRouter

from . import auth, tasks

router = APIRouter()
router.include_router(tasks.router)
router.include_router(auth.router)
