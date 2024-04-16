from fastapi.testclient import TestClient
from main import app


# create a test lient using the TestClient class
client = TestClient(app)

#Test the check_payment_processing route
def check_payment_process():
   response = client.post("/card_details",
    json={
          "credit_card":{
               "name":"Somto Jideofor",
                "age":18,
                "account_type": "savings",
                "password":45367563223,
                "phoneNumber":+23465432178,
                "date":"2021-04-13"
                },
                            
             "price":35000 
        },
    )
assert response.status_code == 201
assert response.json() == {
    "data":{
        "client_name": "Iroaganachi Ikem",
        "client_age": 18,
        "pasword":45367563223,
        "phonenumber": +23465432178,
        "account_type":"savings"
    },
    "message": "Transaction successful"
}
    