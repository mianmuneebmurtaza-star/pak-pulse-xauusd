
import yfinance as yf
import pandas as pd

def get_gold_data():
    try:
        gold = yf.Ticker("GC=F")
        data = gold.history(period="5d", interval="15m")

        if data.empty:
            return None

        return data

    except Exception as e:
        print("Market data error:", e)
        return None


def get_gold_price():
    data = get_gold_data()

    if data is None:
        return None

    return round(float(data["Close"].iloc[-1]), 2)
