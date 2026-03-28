import logging
from bot.client import get_client


def place_order(symbol, side, order_type, quantity, price=None):
    client = get_client()

    try:
        logging.info(f"Placing order: {symbol} | {side} | {order_type}")

        # Market order
        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

        # Limit order
        elif order_type == "LIMIT":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                timeInForce="GTC",
                quantity=quantity,
                price=str(price)  # safer to send as string
            )

        else:
            # fallback (should not happen if validation is correct)
            raise ValueError(f"Invalid order type: {order_type}")

        logging.info("Order placed successfully")
        logging.info(f"Order response: {order}")

        return order

    except Exception as e:
        logging.error("Error while placing order")
        logging.error(str(e))
        raise
