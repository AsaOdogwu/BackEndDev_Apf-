from pydantic import BaseModel, Field,EmailStr

from datetime import date



class Attendants_Info(BaseModel):
    name: str = Field(...,max_length=20, description="Name of the client",title="Name")
    email: EmailStr
    age: int = Field(...,gt= 20,description="Age of the client",title="Age")

class EventDetails(BaseModel):
    name:str = Field(max_length=100)
    date: date
    location:str

class TicketTypes(BaseModel):
    type:str = Field(..., description= "This is strictly for MVP and VIPS")

class BookingRequest(BaseModel):
        event_details: EventDetails
        attendants_info: Attendants_Info
        ticket_type: TicketTypes

class BookingResponse(BaseModel):
    confirmation: str
    event_details: EventDetails
    attendee_details: Attendants_Info
    ticket_type: TicketTypes

class ResponseModel(BaseModel):
     message:str