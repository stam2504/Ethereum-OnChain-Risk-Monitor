import time
import os
from web3 import Web3
import pandas as pd

# 1. Setup
alchemy_url = os.getenv("ALCHEMY_ETHEREUM_MAINNET_URL")
w3 = Web3(Web3.HTTPProvider(alchemy_url))
csv_file = "blockchain_risk_data.csv"

def fetch_and_save():
    if w3.is_connected():
        latest_block = w3.eth.block_number
        print(f"Ingesting Block: {latest_block}...")
        
        block = w3.eth.get_block(latest_block, full_transactions=True)
        all_tx_data = []

        for tx in block.transactions:
            all_tx_data.append({
                'Timestamp': time.strftime("%Y-%m-%d %H:%M:%S"),
                'Block': latest_block,
                'From': tx['from'],
                'To': tx['to'],
                'Value_ETH': float(w3.from_wei(tx['value'], 'ether'))
            })

        df = pd.DataFrame(all_tx_data)
        
        # 2. Smart save (append function)
        # If the file doesn't exist, write the headers. If it does, just append the data.
        if not os.path.isfile(csv_file):
            df.to_csv(csv_file, index=False)
        else:
            df.to_csv(csv_file, mode='a', header=False, index=False)
        
        print(f"Added {len(df)} transactions. Waiting for next block...")
    else:
        print("Connection Failed.")

# 3. The "Automated Pipeline" Loop
print("The program has started. Press Ctrl+C to stop it.")
while True:
    try:
        fetch_and_save()
        time.sleep(60) # Wait 60 seconds.
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(10) # Please wait a moment if there is a network error.