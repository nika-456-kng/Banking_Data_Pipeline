import time
import json
import random
from datetime import datetime
from faker import Faker

# Initialize Faker to generate mock user details
fake = Faker()

# Define structural variables for our banking network
TRANSACTION_CATEGORIES = ["Groceries", "Electronics", "Streaming Service", "Coffee Shop", "Rent", "Salary"]
MERCHANTS = ["SuperMart", "TechZone", "Netflix", "Starbucks", "PropManagement", "EmployerCorp"]

def generate_banking_event():
    """Simulates a live credit card swipe or account event."""
    category_index = random.randint(0, len(TRANSACTION_CATEGORIES) - 1)
    
    # Construct the raw event object (The JSON package Kafka would transport)
    event_payload = {
        "transaction_id": f"TXN-{random.randint(100000, 999999)}",
        "account_id": f"ACC-{random.randint(5555, 9999)}",
        "user_name": fake.name(),
        "amount": round(random.uniform(5.50, 1500.00), 2),
        "category": TRANSACTION_CATEGORIES[category_index],
        "merchant": MERCHANTS[category_index],
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return event_payload

def start_streaming_conveyor_belt():
    """Runs a continuous loop mimicking a live data ingestion stream."""
    print("🚀 Kafka Topic [raw-transactions] initialized...")
    print("📡 Press CTRL+C to halt the streaming ingestion server.\n")
    
    try:
        while True:
            # 1. Capture the event
            live_event = generate_banking_event()
            
            # 2. Convert to JSON string format (Standard text transmission)
            json_message = json.dumps(live_event)
            
            # 3. Simulate transmitting it live down the pipeline
            print(f"[PRODUCER -> TOPIC: raw-transactions]: {json_message}")
            
            # Wait 1 second before generating the next transaction swipe
            time.sleep(1.0)
            
    except KeyboardInterrupt:
        print("\n🛑 Streaming conveyor belt paused safely.")

if __name__ == "__main__":
    start_streaming_conveyor_belt()