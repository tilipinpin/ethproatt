import time
import random
from web3 import Web3
import datetime

# Define global variables
RPC_URL = "https://eth1.lava.build/lava-referer-c22dbde6-26da-4021-ae91-5e8f32ffbe1f/"
web3 = Web3(Web3.HTTPProvider(RPC_URL))

# Create some accounts
num_accounts = 10
accounts = [web3.eth.account.create() for _ in range(num_accounts)]

def create_wallet():
    account = web3.eth.account.create()
    print("Wallet Address:", account.address)
    balance = web3.eth.get_balance(account.address)
    balance_eth = web3.from_wei(balance, 'ether')  # Fix here
    print("Balance:", balance_eth, "ETH")
    if balance > 0:
        print("Wallet Balance is greater than 0. Printing Private Key and Exiting.")
        print("Private Key:", account._private_key.hex())
        exit()

def get_block_number():
    block_number = web3.eth.block_number
    print("Current Block Number:", block_number)

def get_block_info():
    block_number = web3.eth.block_number
    block_info = web3.eth.get_block(block_number)
    print("Block Info:", block_info)

def get_transaction_receipt():
    latest_block = web3.eth.get_block('latest')
    transactions = latest_block.transactions
    if transactions:
        tx_hash = random.choice(transactions)
        try:
            receipt = web3.eth.get_transaction_receipt(tx_hash)
            if receipt:
                print("Transaction Receipt:", receipt)
            else:
                print("Transaction Receipt not found for hash:", tx_hash)
        except web3.exceptions.TransactionNotFound as e:
            print("Transaction not found:", e)
    else:
        print("No transactions found in the latest block.")

def get_transaction_details():
    latest_block = web3.eth.get_block('latest')
    transactions = latest_block.transactions
    if transactions:
        tx_hash = random.choice(transactions)
        tx_details = web3.eth.get_transaction(tx_hash)
        print("Transaction Details:", tx_details)
    else:
        print("No transactions found in the latest block.")

def get_transaction_count():
    address = random.choice(accounts).address
    tx_count = web3.eth.get_transaction_count(address)
    print("Transaction Count:", tx_count)

def get_network_version():
    network_version = web3.eth.chain_id
    print("Network Version:", network_version)

def get_client_version():
    client_version = web3.client_version
    print("Client Version:", client_version)

def create_eth_account():
    account = web3.eth.account.create()
    print("New Ethereum Account Created:")
    print("Address:", account.address)
    print("Private Key:", account._private_key.hex())

def unlock_account():
    address = random.choice(accounts).address
    password = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', k=12))
    print("Unlocking account:", address)
    print("Password:", password)
    print("Note: Account unlocking is not needed when signing transactions with private key.")

def get_gas_price():
    gas_price = web3.eth.gas_price
    print("Current Gas Price:", gas_price)

# Define task list
tasks = [
    create_wallet,
    get_block_number,
    get_block_info,
    get_transaction_receipt,
    get_transaction_details,
    get_transaction_count,
    get_network_version,
    get_client_version,
    create_eth_account,
    unlock_account,
    get_gas_price,
]

# Execute tasks with random delays within a minute
while True:
    print("\n--- New Round ---")
    tasks_copy = tasks[:]  # Create a copy of tasks list to avoid modifying the original
    random.shuffle(tasks_copy)  # Shuffle the tasks to randomize their order
    for task in tasks_copy:
        task()
        time.sleep(random.uniform(5, 15))  # Random delay between 5 to 15 seconds
    
    current_time = datetime.datetime.now()
    print("Current Time:", current_time)
    
    time.sleep(60)  # Sleep for 60 seconds
