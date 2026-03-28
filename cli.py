import argparse
import logging

from bot.orders import place_order
from bot.validators import validate_side, validate_order_type, validate_quantity, validate_price
from bot.logging_config import setup_logger


def main():
    # initialize logging
    setup_logger()

    parser = argparse.ArgumentParser(description="Simple Binance Futures Testnet Bot")

    parser.add_argument("--symbol", required=True, help="Example: BTCUSDT")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        # basic validation
        validate_side(args.side)
        validate_order_type(args.type)
        validate_quantity(args.quantity)
        validate_price(args.type, args.price)

        print("\nPlacing order with following details:")
        print(f"Symbol   : {args.symbol}")
        print(f"Side     : {args.side}")
        print(f"Type     : {args.type}")
        print(f"Quantity : {args.quantity}")

        if args.type == "LIMIT":
            print(f"Price    : {args.price}")

        # call order function
        result = place_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price
        )

        print("\nOrder placed successfully")
        print("-" * 35)
        print(f"Order ID     : {result.get('orderId')}")
        print(f"Status       : {result.get('status')}")
        print(f"Executed Qty : {result.get('executedQty')}")

        avg_price = result.get("avgPrice")
        if avg_price:
            print(f"Avg Price    : {avg_price}")

    except Exception as err:
        print("\nSomething went wrong while placing the order.")
        print(f"Error: {err}")
        logging.error(f"Error occurred: {err}")


if __name__ == "__main__":
    main()
