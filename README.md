# 💰 Crypto Price Alert Bot

A Python-based tool that monitors the real-time price of cryptocurrencies (e.g., Solana, Cardano, Dogecoin) using the CoinGecko API. It automatically sends **Telegram alerts** when prices fall below a defined threshold, and also **logs price history to CSV** for visualization.

## 📦 Features

- 🔔 Sends buy alerts to Telegram
- 🕒 Fetches live prices every 10 minutes
- 📊 Logs all prices in a local `price_log.csv` file
- 📈 Built-in function to plot historical price charts using `matplotlib`
- 💾 Simple and lightweight, no database needed

## 🔧 Technologies Used

- Python 3.x
- Requests
- Matplotlib
- Pandas
- CoinGecko Public API
- Telegram Bot API

## 🚀 How to Use

1. Clone the repo:
   ```bash
   git clone https://github.com/esmael1997/crypto-price-tracker.git
   cd crypto-price-tracker
