# TradeConnect: Robust Distributed Trading System

TradeConnect is a Python-based distributed trading system that simulates a robust market environment. It's designed with multi-threaded operations and uses the xmlrpc library for remote method invocation, making it an efficient system for handling multiple transactions simultaneously.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Code Structure](#code-structure)

## Features

- **Distributed System**: TradeConnect utilizes the xmlrpc library, enabling various components of the system to communicate over the network, establishing a distributed environment.
- **Multi-threaded Operations**: Leveraging Python's threading capabilities, TradeConnect can handle multiple transactions simultaneously, providing performance and efficiency.
- **Transaction Logging**: Every transaction is meticulously logged, and completed transactions are marked as served, providing a traceable transaction history.

## Getting Started

### Prerequisites

Ensure you have Python installed on your machine, along with the necessary Python packages listed in the `requirements.txt` file in the repository.

To install these prerequisites, navigate to the project directory and run:

```bash
pip install -r requirements.txt
```

### Installation
- Clone the repo
```bash
git clone https://github.com/pranay-ar/TradeConnect.git
```
- Install Python packages
```bash
pip install -r requirements.txt
```

## Usage
Navigate to the project directory and execute the run.sh script using the bash command:

```bash
bash run.sh
```
This script sets up the necessary environment and initiates the trading system.

## Code Structure
- `run.sh`: A bash script to launch the system.
- `market.py`: Contains the core classes and methods that handle the trading mechanism.
- `data_ops.py`: Contains functions for logging transactions, marking transactions as complete, and retrieving unserved requests.
- `requirements.txt`: Lists the Python packages necessary for running the project.
- `output.txt`: Demonstrates a sample output from one of the runs.
