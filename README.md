# CS 216: Assignment 2 — UTXO Simulator

A local simulation of a Bitcoin-style transaction system using the UTXO model: transaction validation, mempool management, and block mining with double-spend prevention.

---

## 1. Team

- **Team name:** [Merkle Minds]
- **Members:**
  1. [Velpula Vikram Varma] — [240001078]
  2. [Sreyan Reddy Regatte] — [240051018]
  3. [K Manas Joel] — [240004025]
  4. [Chinnakondu Hemanth Royal] — [240041010]

---

## 2. How to run

- **Requirements:** Python 3.8+ (standard library only; no extra packages).
- **Steps:**
  1. Clone or download the repository.
  2. Open a terminal in the project folder.
  3. Run the program from the `src` directory:
     ```bash
     cd src
     python main.py
     ```
  4. Use the menu (1–6) to create transactions, view UTXO set/mempool, mine blocks, run test scenarios, or exit.

---

## 3. Design (brief)

- **UTXO Manager (`utxo_manager.py`):** Holds the set of unspent outputs `(tx_id, index) → (amount, owner)`. Supports add, remove, balance, and listing UTXOs per owner.
- **Transactions (`transaction.py`, `validation.py`):** A transaction has inputs (UTXOs to spend) and outputs (new UTXOs). Validation checks: inputs exist, no duplicate inputs, no mempool conflict, sum(inputs) ≥ sum(outputs), no negative amounts.
- **Mempool (`mempool.py`):** Stores unconfirmed transactions and tracks which UTXOs are already spent in the mempool to prevent double-spend before mining.
- **Mining (`mine_block.py`):** Picks top-fee transactions from the mempool, applies them to the UTXO set (remove inputs, add outputs), pays total fees to the miner as a coinbase UTXO, and removes mined transactions from the mempool.

---

## 4. Bonus

- **Bonus attempted:** No.

---

## 5. Dependencies / installation

- No installation beyond Python 3.8+ is required.
- The project uses only the Python standard library (no `pip install` needed).  
  If you add dependencies later, list them in `requirements.txt` and run: `pip install -r requirements.txt`.
