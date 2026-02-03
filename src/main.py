from typing import cast
from utxo_manager import UTXOManager
from mempool import Mempool
from transaction import transaction
from mine_block import mine_block
from validation import validate_transaction
from test_scenarios import run_test_scenarios

def seed_genesis(utxo):
    genesis = [("genesis",0,50.0,"Alice"), ("genesis",1,30.0,"Bob"),
               ("genesis",2,20.0,"Charlie"), ("genesis",3,10.0,"David"),
               ("genesis",4,5.0,"Eve")]
    for tx_id, idx, amt, owner in genesis:
        utxo.add_utxo(tx_id, idx, amt, owner)

def create_tx_flow(utxo, mempool):
    sender = input("Enter sender: ").strip()
    balance = utxo.get_balance(sender)
    if balance is False or balance <= 0:
        print("Invalid sender or no balance.\n")
        return
    print(f"Available balance: {balance} BTC")
    recipient = input("Enter recipient: ").strip()

    while True:
        raw = input("Enter amount: ").strip()
        try:
            amount = float(raw)
        except ValueError:
            print("Invalid amount. Please enter a number.\n")
            continue

        if amount <= 0:
            print("Amount must be > 0.\n")
            continue

        break

    fee = 0.001

    utxos = utxo.get_utxos_for_owner(sender)
    if utxos is False or not utxos:
        print("No UTXOs for sender.\n")
        return
    chosen = []
    total_in = 0.0
    for (tx_id, idx), amt in utxos:
        chosen.append((tx_id, idx, amt))
        total_in += amt
        if total_in >= amount + fee:
            break
    if total_in < amount + fee:
        print("Insufficient funds.\n")
        return

    inputs = [{"prev_tx": tx_id, "index": idx, "owner": sender} for tx_id, idx, amt in chosen]
    change = total_in - amount - fee
    outputs = [{"amount": amount, "address": recipient}]
    if change > 0:
        outputs.append({"amount": round(change, 8), "address": sender})

    tx = transaction(inputs, outputs)
    ok, result = validate_transaction(tx, utxo, mempool)
    if not ok:
        print(result, "\n")
        return
    tx.fee = cast(float, result)
    ok, msg = mempool.add_transaction(tx, utxo)
    print(msg, "\n")

def main():
    utxo = UTXOManager()
    mempool = Mempool(max_size=50)
    seed_genesis(utxo)

    while True:
        print("Main Menu:\n1. Create new transaction\n2. View UTXO set\n3. View mempool\n4. Mine block\n5. Run test scenarios\n6. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            create_tx_flow(utxo, mempool)
        elif choice == "2":
            print(utxo)  
        elif choice == "3":
            print(mempool)  
        elif choice == "4":
            miner = input("Enter miner name: ").strip()
            n_in_mempool = len(mempool.transactions)
            print("Mining block...")
            included, total_fees, _ = mine_block(miner, mempool, utxo, num_txs=5)
            n = len(included)
            tx_word = "transaction" if n == 1 else "transactions"
            print(f"Mempool had {n_in_mempool} {tx_word}.")
            print(f"Selected {n} {tx_word} from mempool.")
            print(f"Total fees: {total_fees:.3f} BTC")
            print(f"Miner {miner} receives {total_fees:.3f} BTC")
            print("Block mined successfully!")
            print(f"Removed {n} {tx_word} from mempool.\n")
        elif choice == "5":
            run_test_scenarios(utxo, mempool)
        elif choice == "6":
            break
        else:
            print("Invalid choice.\n")

if __name__ == "__main__":
    main()
