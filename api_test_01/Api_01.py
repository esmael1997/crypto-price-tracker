import requests
import time 
from datetime import datetime
import csv
#import matplotlib.pyplot as plt 
import pandas as pd 


coins = {
    "solana": 10000.0,
    "cardano": 10.5,
    "dogecoin": 10.12
    
}

limit = coins

def get_prices(coin_ids):
    
    ids = ",".join(coin_ids)
    
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies=usd"

    response = requests.get(url)
    
    if response.status_code == 200:
        
        return response.json()
    
    else:
        
        print("wrongggg!!!")
        
        return None
    
def log_to_csv(data):
    
    with open("price_log.csv", mode="a",newline="") as file:
        
        writer = csv.writer(file)
        
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        for coin, info in data.items():
            
            writer.writerow([now,coin,info['usd']])
            
def send_telegram_message(message):
    
    token = "7608849519:AAG2134QUwkhHEu9zVqDji44PYW-CsFh-A0"
    
    
    chat_id = "118762909"
    
    
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    
    
    payload = {"chat_id": chat_id, "text": message}
    
    
    try:
        
        
        response = requests.post(url , data = payload)
        
        
        if response.status_code != 200:
            
            
            print(f"sending message failed : {response.status_code}")
            
            
    except Exception as e :
        
        
        print(f"Error sendeing telegram message : {e}")
        
        
#def plot_price_history(coin_name):
    
    
def check_buy_signals():
    
    data = get_prices(coins.keys())
    if data :
       for coin, limit in coins.items(): 
           
           price = data[coin]['usd']  
      
           if price < limit:
            
               alert = f"{coin.capitalize()} is now {price} USD - Buy signal triggered!"
            
               send_telegram_message(alert)
            
    log_to_csv(data) 
    
    
df = pd.read_csv("price_log.csv")
print(df.tail(20)) 
    
        
        
if __name__ == "__main__":
    
    while True:
        
        check_buy_signals()
        
        time.sleep(600)
        
        
        
        
        
                      
                                
                
      