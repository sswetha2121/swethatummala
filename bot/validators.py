def validate_side(side):
    if not side:
        raise ValueError("Side is required")

    side = side.upper()

    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be either BUY or SELL")

    return side


def validate_order_type(order_type):
    if not order_type:
        raise ValueError("Order type is required")

    order_type = order_type.upper()

    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")

    return order_type


def validate_quantity(quantity):
    if quantity is None:
        raise ValueError("Quantity is required")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")

    return quantity


def validate_price(order_type, price):
    if order_type == "LIMIT":
        if price is None:
            raise ValueError("Price is required for LIMIT orders")

        if price <= 0:
            raise ValueError("Price must be greater than 0")

    return price
