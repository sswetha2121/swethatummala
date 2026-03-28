import os
from binance.client import Client
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()


def get_client():
    api_key = os.getenv("API_KEY")
    api_secret = os.getenv("API_SECRET")

    if not api_key or not api_secret:
        raise ValueError("API keys not found. Please check your .env file.")

    # create Binance client (testnet)
    client = Client(api_key, api_secret)
    client.FUTURES_URL = "https://testnet.binancefuture.com"

    return client
