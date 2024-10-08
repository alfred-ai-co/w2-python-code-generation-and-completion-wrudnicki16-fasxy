from sqlalchemy.orm import Session
from app.db_models.base import Project, Ticket
from typing import Optional
from app.db_models.base import Ticket


# CRUD operations for Project
def create_ticket(db: Session, project_id: int, title: str, description: Optional[str] = None, status: Optional[str] = None, priority: Optional[str] = None) -> Ticket:
    new_ticket = Ticket(
        project_id=project_id,
        title=title,
        description=description,
        status=status,
        priority=priority
    )
    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)
    return new_ticket

# Create a function named get_ticket that retrieves a ticket from the database by its ID.
def get_ticket(db: Session, ticket_id: int) -> Ticket:
    return db.query(Ticket).filter(Ticket.id == ticket_id).first()

#  Create a function named update_ticket that updates a ticket's title, description, status, and priority based on its ID.
def update_ticket(db: Session, ticket_id: int, title: str, description: Optional[str] = None, status: Optional[str] = None, priority: Optional[str] = None) -> Ticket:
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    ticket.title = title
    ticket.description = description
    ticket.status = status
    ticket.priority = priority
    db.commit()
    db.refresh(ticket)
    return ticket

#  Create a function named delete_ticket that deletes a ticket from the database by its ID.
def delete_ticket(db: Session, ticket_id: int) -> Ticket:
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    db.delete(ticket)
    db.commit()
    return ticket