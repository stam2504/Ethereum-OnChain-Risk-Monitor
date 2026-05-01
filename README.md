# 🛡️ Ethereum On-Chain Risk Monitor (EORM)

**A Real-Time Data Pipeline for Cryptocurrency Institutional Risk Management.**

---

## 📌 Project Overview

This repository contains a professional-grade Python application designed to automate the ingestion and normalization of real-time transactional data from the Ethereum Mainnet. 

Specifically built for Cryptocurrency Funds and Fintech studios, EORM serves as the foundation for monitoring **Liquidity Risk**, **Whale Activity**, and **Smart Contract Exposure** with institutional-grade security and reliability.

> **Key Objective:** Transform raw, unstructured blockchain data into actionable financial metrics.

---

## ✨ Key Features

* **🔌 Real-Time Blockchain Ingestion:** Continuous polling of the latest Ethereum blocks via connection to high-availability Alchemy/Infura nodes.
* **🔒 Security-First Architecture:** Implements industry-standard environment variable management (`.env`) to isolate and protect sensitive API credentials—a critical requirement for financial systems.
* **📊 Financial Normalization:** Automatically converts blockchain-native units (Wei) into standardized Ether (ETH) for accurate financial reporting and analysis.
* **💾 Data Persistence Layer:** Streams raw block data into standardized, append-only CSV format, ready for immediate ingestion into BI tools (like Power BI) or SQL databases.

---

* **🛡️ Multi-Factor Stress Testing:**
    * **Market Risk Engine:** Simulates "Black Swan" events (e.g., -35% ETH price drops) to calculate portfolio drawdown and liquidation thresholds.
    * **Credit Risk Framework:** Implements Basel III-compliant scenarios (Baseline, Adverse, Severe) using **Probability of Default (PD)** and **Loss Given Default (LGD)** metrics to forecast Expected Loss (EL) in CHF.

---

## 🛠️ Technical Stack

* **Language:** `Python 3.10+`
* **Blockchain Interface:** `Web3.py`
* **Data Processing:** `Pandas`
* **Env Management:** `Python-Dotenv`

---

## 🚀 Quick Start Guide

### 1️⃣ Prerequisites
Ensure you have Python installed, along with a valid Ethereum node provider URL (e.g., from Alchemy or Infura).

### 2️⃣ Installation
Clone the repository and install the required dependencies:

```bash
# Clone the repo
git clone [https://github.com/stam2504/Ethereum-OnChain-Risk-Monitor.git](https://github.com/stam2504/Ethereum-OnChain-Risk-Monitor.git)

# Navigate to the directory
cd Ethereum-OnChain-Risk-Monitor

# Install packages
pip install -r requirements.txt

3️⃣ Configuration

Create a .env file in the root directory and add your provider URL.
Plaintext

# .env file
ALCHEMY_ETHEREUM_MAINNET_URL=your_actual_url_here

(Note: For security, the .env file is included in .gitignore and is never committed to the repository).
4️⃣ Execution

Run the data pipeline:
Bash

python Ethereum_Data_Pipeline.py

🗺️ Institutional Roadmap

Future enhancements focused on expanding scalability and analysis capabilities:

    🗄️ TSDB Integration: Migrate from CSV to a specialized Time-Series Database (e.g., InfluxDB) for sub-second query performance.

    🔔 Real-Time Alerting: Implement automated triggers for volatility spikes and large transaction (whale) detections.

    📈 Stress Testing: Integrate Python models to simulate extreme market conditions and calculate Capital at Risk (CaR).
