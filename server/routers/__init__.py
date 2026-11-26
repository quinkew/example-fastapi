from fastapi import APIRouter
from .auth import router as auth_router
from .post import router as post_router
from .user import router as user_router
from .vote import router as vote_router
from .root import router as root_router

main_router = APIRouter()

main_router.include_router(auth_router)
main_router.include_router(post_router)
main_router.include_router(user_router)
main_router.include_router(vote_router)
main_router.include_router(root_router)