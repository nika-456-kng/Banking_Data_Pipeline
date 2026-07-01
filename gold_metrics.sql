-- This represents a dbt Gold Layer Model
-- It dynamically transforms raw transactions into high-value aggregate tables

{{ config(materialized='table') }}

WITH clean_transactions AS (
    SELECT 
        transaction_id,
        account_id,
        user_name,
        amount,
        category,
        merchant,
        -- Convert text timestamps to real database datetime formats
        CAST(timestamp AS TIMESTAMP) AS transaction_at
    FROM {{ ref('stg_transactions') }} -- dbt uses ref() to automatically track data lineage
),

final_metrics AS (
    SELECT
        account_id,
        user_name,
        COUNT(transaction_id) AS total_swipes,
        SUM(amount) AS total_money_spent,
        AVG(amount) AS average_transaction_value,
        
        -- High-Value Business Logic Check
        CASE 
            WHEN SUM(amount) > 5000 THEN '⚠️ AUDIT REQUIRED: High Velocity Volume'
            ELSE '✅ Account Healthy'
        END AS risk_compliance_status
        
    FROM clean_transactions
    GROUP BY account_id, user_name
)

SELECT * FROM final_metrics