# Real-Time Financial Transaction Analytics Pipeline

A simulation framework demonstrating a high-throughput **Modern Data Streaming ELT Pipeline** utilizing a Medallion Architecture pattern (Bronze -> Silver -> Gold).

## 🏗️ Architecture Blueprint

The system processes streaming transactions through three decoupled processing environments:
1. **Bronze Ingestion:** Simulated Apache Kafka event broker broadcasting raw JSON credit card transactions.
2. **Silver Compute:** Simulated Apache Spark Structured Streaming worker executing schema enforcement, null-cleansing, and threshold risk monitoring.
3. **Gold Analytics:** Simulated dbt (data build tool) modeling layer aggregating multi-row user behaviors and building an operational compliance auditing matrix.

## 📁 Repository Structure
* `producer.py` - Simulates the immutable Kafka transaction event loop.
* `spark_processor.py` - Standardizes individual streams into structured, typed silver tables.
* `dbt_simulator.py` - Compiles aggregate analytical profiles and executes fraud velocity checks.
* `gold_metrics.sql` - The production-ready declarative dbt modeling script.

## 🚀 How to Execute the Ecosystem

To witness the entire event-driven architecture running concurrently, open three parallel terminals:

**In terminal:**
```bash
python producer.py
python spark_processor.py
python dbt_simulator.py
