from datetime import datetime
import random

BOOKINGS = {}

def book_cab(pickup_location: str, dropoff_location: str) -> dict:
    """Book a cab for the given route."""
    booking_id = f"BKG{random.randint(1000, 9999)}"
    BOOKINGS[booking_id] = {
        "pickup": pickup_location,
        "dropoff": dropoff_location,
        "driver": {
            "name": random.choice(["Ravi Patel", "Amit Sharma", "Pooja Mehta"]),
            "vehicle": random.choice(["Hyundai Aura", "Maruti Dzire", "Toyota Etios"]),
            "rating": round(random.uniform(4.2, 4.9), 1),
            "phone": f"+91-9{random.randint(100000000, 999999999)}"
        },
        "status": "confirmed",
        "timestamp": datetime.now().isoformat()
    }
    return {"booking_id": booking_id, "message": "Cab booked successfully!"}


def cancel_cab(booking_id: str) -> dict:
    """Cancel a booking if exists."""
    if booking_id not in BOOKINGS:
        return {"error": "Booking not found"}
    BOOKINGS[booking_id]["status"] = "cancelled"
    return {"message": f"Booking {booking_id} cancelled successfully"}


def get_driver_details(booking_id: str) -> dict:
    """Retrieve driver info for a given booking."""
    booking = BOOKINGS.get(booking_id)
    if not booking:
        return {"error": "Booking not found"}
    return booking["driver"]

