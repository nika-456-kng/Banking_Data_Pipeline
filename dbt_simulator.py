import json

# Simulated Silver Layer database table containing transactions processed by Spark
MOCK_STG_TRANSACTIONS = [
    {"account_id": "ACC-6192", "user_name": "Corey Huang", "amount": 317.74, "category": "Salary"},
    {"account_id": "ACC-7355", "user_name": "Sara", "amount": 1023.54, "category": "Coffee Shop"},
    {"account_id": "ACC-6192", "user_name": "Corey Huang", "amount": 4500.00, "category": "Salary"},
    {"account_id": "ACC-5792", "user_name": "Allison Erickson", "amount": 1154.07, "category": "Coffee Shop"},
    {"account_id": "ACC-7355", "user_name": "Sara", "amount": 55.20, "category": "Groceries"}
]

def run_dbt_gold_model():
    print("🚀 Running command: dbt run --select gold_metrics")
    print("==========================================================")
    print("🔨 Compiling code: models/gold/gold_metrics.sql")
    print("📦 Materializing table: DATABASE.GOLD.GOLD_METRICS")
    print("----------------------------------------------------------\n")
    
    # This dictionary simulates how dbt aggregates data over time in a data warehouse
    account_ledger = {}
    
    # Process rows just like our SQL group by statement
    for row in MOCK_STG_TRANSACTIONS:
        acc_id = row["account_id"]
        name = row["user_name"]
        amount = row["amount"]
        
        if acc_id not in account_ledger:
            account_ledger[acc_id] = {
                "user_name": name,
                "total_swipes": 0,
                "total_money_spent": 0.0
            }
            
        account_ledger[acc_id]["total_swipes"] += 1
        account_ledger[acc_id]["total_money_spent"] += amount

    # Print the final Gold Layer reporting table layout
    print(f"{'ACCOUNT ID':<12} | {'USER NAME':<18} | {'TOTAL SWIPES':<12} | {'TOTAL SPENT':<12} | {'RISK STATUS'}")
    print("-" * 75)
    
    for acc_id, metrics in account_ledger.items():
        spent = round(metrics["total_money_spent"], 2)
        
        # Simulating our SQL CASE WHEN condition logic
        risk_status = "⚠️ AUDIT REQUIRED" if spent > 4000.00 else "✅ Account Healthy"
        
        print(f"{acc_id:<12} | {metrics['user_name']:<18} | {metrics['total_swipes']:<12} | ${spent:<11} | {risk_status}")

    print("\n==========================================================")
    print("✅ dbt Run Complete! 1 model successfully materialized.")

if __name__ == "__main__":
    run_dbt_gold_model()