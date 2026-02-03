import utxo_manager

class Mempool:
    def __init__(self, max_size=50):
        self.transactions = []
        self.spent_utxos = set()
        self.max_size = max_size

    def add_transaction(self, tx, utxo_manager):
        if len(self.transactions) >= self.max_size:
            return False, "Mempool full"

        for inp in tx.inputs:
            utxo_key = (inp["prev_tx"], inp["index"])

            if utxo_key in self.spent_utxos:
                return False, f"UTXO {utxo_key} already spent in mempool"

            if not utxo_manager.exists(inp["prev_tx"], inp["index"]):
                return False, f"UTXO {utxo_key} does not exist"
            print("UTXO exists (mempool check)")

        self.transactions.append(tx)

        for inp in tx.inputs:
            self.spent_utxos.add((inp["prev_tx"], inp["index"]))

        return True, "Transaction added to mempool"

    def remove_transaction(self, tx_id):
        for tx in self.transactions:
            if tx.tx_id == tx_id:
                for inp in tx.inputs:
                    self.spent_utxos.discard(
                        (inp["prev_tx"], inp["index"])
                    )
                self.transactions.remove(tx)
                return

    def get_top_transactions(self, n):
        return sorted(
            self.transactions,
            key=lambda tx: getattr(tx, "fee", 0),
            reverse=True
        )[:n]

    def clear(self):
        self.transactions.clear()
        self.spent_utxos.clear()