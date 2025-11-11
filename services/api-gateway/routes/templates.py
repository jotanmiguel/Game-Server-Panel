from fastapi import APIRouter
from services.template_service import template_service

router = APIRouter()

@router.get("/")
def list_templates():
    return template_service.list_templates()
