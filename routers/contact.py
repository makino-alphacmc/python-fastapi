from fastapi import APIRouter
import schemas.contact as contact_schema
from datetime import datetime
router = APIRouter()

@router.get("/contacts", response_model=list[contact_schema.Contact])
async def get_contact_all():
    dummy_date = datetime.now()
    return [contact_schema.Contact(
      id=1,
      name="John Doe",
      email="john.doe@example.com",
      url="https://www.example.com",
      gender=0,
      message="Hello, world!",
      is_enabled=True,
      created_at=dummy_date
      )]


@router.post("/contacts", response_model=contact_schema.Contact)
async def create_contact(body: contact_schema.Contact):
  return contact_schema.Contact(**body.model_dump())

@router.get("/contacts/{id}", response_model=contact_schema.Contact)
async def get_contact(id: int):
    return contact_schema.Contact(id)

@router.put("/contacts/{id}", response_model=contact_schema.Contact)
async def update_contact(id: int, body: contact_schema.Contact):
    return contact_schema.Contact(**body.model_dump())

@router.delete("/contacts/{id}", response_model=contact_schema.Contact)
async def delete_contact(id: int):
    return
