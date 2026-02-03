def mine_block(miner_address, mempool, utxo_manager, num_txs=5, block_id=None):
    candidates = mempool.get_top_transactions(num_txs)

    included = []
    block_spent = set()
    total_fees = 0

    for tx in candidates:
        
        valid = True
        for inp in tx.inputs:
            utxo_key = (inp["prev_tx"], inp["index"])

            if utxo_key in block_spent:
                valid = False
                break

            if not utxo_manager.exists(inp["prev_tx"], inp["index"]):
                valid = False
                break

        if not valid:
            continue

        
        for inp in tx.inputs:
            utxo_key = (inp["prev_tx"], inp["index"])
            utxo_manager.remove_utxo(inp["prev_tx"], inp["index"])
            block_spent.add(utxo_key)

       
        for out_index, out in enumerate(tx.outputs):
            utxo_manager.add_utxo(tx.tx_id, out_index, out["amount"], out["address"])

        included.append(tx)
        total_fees += getattr(tx, "fee", 0)

    
    for tx in included:
        mempool.remove_transaction(tx.tx_id)

   
    if block_id is None:
        block_id = len(included) 
    coinbase_tx_id = f"coinbase_{block_id}"
    utxo_manager.add_utxo(coinbase_tx_id, 0, total_fees, miner_address)

    return included, total_fees, (coinbase_tx_id, 0)