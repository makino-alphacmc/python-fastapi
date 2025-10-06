from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
import schemas.contact as contact_schema
import cruds.contact as contact_crud
from database import get_db
from datetime import datetime

router = APIRouter()

@router.get("/contacts", response_model=list[contact_schema.ContactList])
async def get_contact_all():
    dummy_date = datetime.now()
    return [contact_schema.ContactList(
      id=1,
      name="John Doe",
      email="john.doe@example.com",
      url="https://www.example.com",
      gender=0,
      message="Hello, world!",
      is_enabled=True,
      created_at=dummy_date
      )]


@router.post("/contacts", response_model=contact_schema.ContactCreate)
async def create_contact(body: contact_schema.ContactCreate, db: AsyncSession = Depends(get_db)):
  return await contact_crud.create_contact(db, body)

@router.get("/contacts/{id}", response_model=contact_schema.ContactDetail)
async def get_contact(id: int):
    return contact_schema.ContactDetail(id)

@router.put("/contacts/{id}", response_model=contact_schema.ContactCreate)
async def update_contact(id: int, body: contact_schema.ContactCreate):
    return contact_schema.Contact(**body.model_dump())

@router.delete("/contacts/{id}", response_model=None)
async def delete_contact(id: int):
    return
