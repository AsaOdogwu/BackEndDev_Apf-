

async def license_inventory(license):
    """Process the license inventory,this is for the vehicle inventory"""

    vehicle_outcome = {
        "client_name": license.Vehicle_check.name,
        "client_age": license.Vehicle_check.age,
        "client_email": license.Vehicle_check.email,
        "client_phone": license.Vehicle_check.phone,
    }
    return vehicle_outcome
