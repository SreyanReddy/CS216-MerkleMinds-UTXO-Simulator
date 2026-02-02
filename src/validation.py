# Implement validator logic

class Mempool2:
    def __init__(self):
        self.spent_utxos = set()   # {(tx_id, index)}

    def add_transaction(self, tx):
        for inp in tx.inputs:
            self.spent_utxos.add((inp["prev_tx"], inp["index"]))

            
def validate_transaction(tx, utxo_manager, mempool):
   

    input_sum = 0.0
    output_sum = 0.0
    used_inputs = set()

  
    for inp in tx.inputs:
        key = (inp["prev_tx"], inp["index"])

        #  No duplicate inputs in same transaction
        if key in used_inputs:
            return False, "Duplicate input in transaction"
        used_inputs.add(key)

        # UTXO must exist
        if not utxo_manager.exists(*key):
            return False, "UTXO does not exist"

        # Get UTXO data from friend's UTXOManager
        amount, owner = utxo_manager.utxo_set[key]

        # Ownership check
        if owner != inp["owner"]:
            return False, "Owner mismatch"

        #  No mempool conflict
        if key in mempool.spent_utxos:
            return False, "UTXO already spent in mempool"

        input_sum += float(amount)

   
    for out in tx.outputs:
        #  No negative outputs
        if out["amount"] < 0:
            return False, "Negative output amount"
        output_sum += float(out["amount"])

    # Inputs must cover outputs
    if input_sum < output_sum:
        return False, "Insufficient balance"

    fee = input_sum - output_sum
    return True, fee