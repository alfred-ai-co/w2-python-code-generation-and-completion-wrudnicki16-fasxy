from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db_models import crud
from app.api_models import tickets
from app.api.dependencies.sqldb import get_db

router = APIRouter()

@router.post("/", response_model=tickets.TicketResponse)
def create_ticket(ticket: tickets.TicketCreate, db: Session = Depends(get_db)):
    try:
        db_ticket = crud.create_ticket(
            db=db,
            project_id=ticket.project_id,
            title=ticket.title,
            description=ticket.description,
            status=ticket.status,
            priority=ticket.priority
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    if db_ticket is None:
        raise HTTPException(status_code=400, detail="Ticket could not be created")
    return db_ticket

@router.get("/{ticket_id}", response_model=tickets.TicketResponse)
def read_ticket(ticket_id: int, db: Session = Depends(get_db)):
    try:
        db_ticket = crud.get_ticket(db, ticket_id=ticket_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    if db_ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return db_ticket

@router.put("/{ticket_id}", response_model=tickets.TicketResponse)
def update_ticket(ticket_id: int, ticket: tickets.TicketCreate, db: Session = Depends(get_db)):
    try:
        db_ticket = crud.update_ticket(
            db=db,
            ticket_id=ticket_id,
            title=ticket.title,
            description=ticket.description,
            status=ticket.status,
            priority=ticket.priority
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    if db_ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return db_ticket

@router.delete("/{ticket_id}")
def delete_ticket(ticket_id: int, db: Session = Depends(get_db)):
    db_ticket = crud.get_ticket(db, ticket_id=ticket_id)
    if db_ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")

    try:
        crud.delete_ticket(db, ticket_id=ticket_id)
        return {"message": "Ticket successfully deleted"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))