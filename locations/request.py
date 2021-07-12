LOCATIONS = [
    {
      "id": 1,
      "name": "Nashville North",
      "address": "8445 Johnson Pike"
    },
    {
      "id": 2,
      "name": "Nashville South",
      "address": "210 Emory Drive"
    }
]

def get_all_locations():
    return LOCATIONS

def get_single_location(id):
    requested_location = None

    for location in LOCATIONS:
        if location["id"] == id:
            requested_location = location
    
    return requested_location