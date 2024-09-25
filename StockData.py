import yfinance as yf


ticker = input("Enter the Ticket: ")
from_data = input("enter the start date (YYYY-MM-DD)")
to_data = input("Enter the end date (YYYY-MM-DD):")

stock_data = yf.download(ticker,start=from_data, end=to_data)
stock_data.to_html("stock_data.html")
print("Stock data written to stock_data.html")
