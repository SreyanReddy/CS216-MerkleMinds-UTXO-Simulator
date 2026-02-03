def validate_transaction(tx, utxo_manager, mempool):
    
    input_sum = 0.0
    output_sum = 0.0
    used_inputs = set()

  
    for inp in tx.inputs:
        key = (inp["prev_tx"], inp["index"])

        
        if key in used_inputs:
            return False, "Duplicate input in transaction"
        used_inputs.add(key)

        
        if not utxo_manager.exists(*key):
            return False, "UTXO does not exist"
        print("UTXO exists (transaction validation)")

        
        amount, owner = utxo_manager.utxo_set[key]

        
        if owner != inp["owner"]:
            return False, "Owner mismatch"

        
        if key in mempool.spent_utxos:
            return False, "UTXO already spent in mempool"

        input_sum += float(amount)

   
    for out in tx.outputs:
        
        if out["amount"] < 0:
            return False, "Negative output amount"
        output_sum += float(out["amount"])

    
    if input_sum < output_sum:
        return False, "Insufficient balance"

    fee = input_sum - output_sum
    return True, fee