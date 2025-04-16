from pydantic import BaseModel, EmailStr
from typing import List

class Order(BaseModel):
    order_id: int
    product: str
    price: float

class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    is_active: bool
    orders: List[Order]


data = {
    "id": 1,
    "name": "Ala",
    "email": "ala@example.com",
    "is_active": True,
    "orders": [
        {"order_id": 101, "product": "Laptop", "price": 999.99},
        # {"order_id": 101, "product": "Laptop", "price": "bezcenny"},
        {"order_id": 102, "product": "Myszka", "price": 29.50}
    ]
}

user = User(**data)

# Dostęp do zamówień
for order in user.orders:
    print(f"{order.product} za {order.price} zł")

