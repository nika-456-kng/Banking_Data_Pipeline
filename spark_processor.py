import json
import os
import sys

def run_silver_processing_pipeline(raw_json_line: str):
    """
    Mimics Apache Spark's Structured Streaming transformation.
    Takes raw, messy string data and converts it into a clean analytical format.
    """
    try:
        # 1. Parse the raw string data into an object (Spark Schema Parsing)
        event_data = json.loads(raw_json_line)
        
        amount = event_data.get("amount", 0)
        account = event_data.get("account_id", "UNKNOWN")
        category = event_data.get("category", "UNKNOWN")
        
        # 2. Data Cleaning Layer (Ensuring quality boundaries)
        is_suspicious = "⚠️ HIGH RISK" if amount > 1000.00 else "✅ NORMAL"
        
        # 3. Output the structured Silver-tier record
        print(f"\n[SPARK PROCESSING - SILVER LAYER]")
        print(f"🔹 Account: {account} | Category: {category}")
        print(f"🔹 Amount: ${amount:<8} | Risk Status: {is_suspicious}")
        print("-" * 50)
        
    except Exception as e:
        print(f"❌ Data Corruption Detected: {e}")

if __name__ == "__main__":
    print("⚡ Mini-Spark Streaming Node Active...")
    print("📥 Awaiting stream lines from producer. Paste a line below to process:")
    
    # Keep listening for incoming data lines
    for line in sys.stdin:
        if line.strip():
            # Extract just the JSON part if the producer log prefix is attached
            if "raw-transactions]: " in line:
                line = line.split("raw-transactions]: ")[1]
            run_silver_processing_pipeline(line)