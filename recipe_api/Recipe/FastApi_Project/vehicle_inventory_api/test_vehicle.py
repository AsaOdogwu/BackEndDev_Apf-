from fastapi.testclient import TestClient
from main import app

# Create a test client using the TestClient class
client = TestClient(app)

#Test the create_vehicle route
def test_create_vehicle():
    response = client.post("/license",json ={
        "vehicle-pattern": {
            "name":"Camry",
            "make": "Toyota",
            "model_year": 2023,
            "color": "red",
            "vehicle_date": "2023-03-13",
            "vin":"A-KS-GUR-W4-8",
            "condition":"NOT USED",
            "mileage": "1500KM",
            "price":"$10000.00"


        },
        "Vehicle_check":{
            "name": "Jideofor Kosisochukwu",
            "age": 32,
            "email": "clientk@15343.com",
            "phone": +2348166811459
        }
    },

    )
    assert response.status_code == 201
    assert response.json() == {
        "data": {
            "client_name": "Jideofor Kosisochukwu",
            "client_age": 32,
            "client_email": "clientk@15343.com",
            "client_phone": "tel:+234-654-456-3432",
            "vehicle_date": "2023-03-13",
            "vin":"Aks2345677QEARYFR",
            "condition":"NOT USED",
            "mileage": "1500KM",
            "price":"$10000.00"

        },
        "message": "vehicle inventory successful",
        
    }