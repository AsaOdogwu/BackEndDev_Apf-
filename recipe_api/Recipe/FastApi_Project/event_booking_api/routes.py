from fastapi import APIRouter,HTTPException
from models import TicketTypes,BookingResponse,BookingRequest,ResponseModel

book_event_router = APIRouter(prefix="/book_event", tags = ["clients"])


@book_event_router.post("/",response_model = ResponseModel)
async def book_event(booking_request: BookingRequest):
    # Validate ticket type
    if booking_request.ticket_type.lower() not in TicketTypes:
        raise HTTPException(status_code=400, detail="Invalid ticket type")

    # booking confirmation
    confirmation_message = " Event booking confirmed!"

    return BookingResponse(
        confirmation=confirmation_message,
        event_details=booking_request.event_details,
        attendee_details=booking_request.attendee_details,
        ticket_type=booking_request.ticket_types.get("type")
    )