# tests/test_main.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_book_event_success():
    event_details = {
        "name": "Concert",
        "date": "2024-04-10",
        "location": "Venue A"
    }
    attendee_details = {
        "name": "John Doe",
        "email": "john@example.com",
        "age": 19
    }
    ticket_type = "standard"

    response = client.post("/book_event/", json={
        "event_details": event_details,
        "attendee_details": attendee_details,
        "ticket_type": ticket_type
    })

    assert response.status_code == 200
    assert response.json()["confirmation"] == "Event booking confirmed!"

def test_book_event_invalid_ticket_type():
    event_details = {
        "name": "Workshop",
        "date": "2024-04-15",
        "location": "Venue B"
    }
    attendee_details = {
        "name": "Jane Smith",
        "email": "jane@example.com",
        "age": 18
    }
    ticket_type = "premium"  

    response = client.post("/book_event/", json={
        "event_details": event_details,
        "attendee_details": attendee_details,
        "ticket_type": ticket_type
    })

    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid ticket type"
