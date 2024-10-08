from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
class TicketCreate(BaseModel):
    project_id: int
    title: str
    description: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[str] = None

class TicketResponse(TicketCreate):
    id: int
    created_at: datetime
    due_date: Optional[datetime] = Field(None, alias="dueDate", description="Due date of the ticket")