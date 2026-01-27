class UTXOManger():
    def __init__(self):
        self.utxo_set = {}

    def add_utxo(self, tx_id, index, amount, owner):

        if tx_id is None or tx_id == "":
            print("Error: Transaction ID cannot be empty")
            return False
        if isinstance(index, int) == 0 or index < 0:
            print("Error: Index must be a non-negative integer")
            return False
        if isinstance(amount, int or float) or amount <=0:
            print("Error: Amount must be a positive integer")
            return False
        if owner is None or isinstance(owner, str) == 0 or owner.strip() == "":
            print("Error: Owner must be a non-empty string")
            return False
        
        key = (tx_id, index)
        if key in self.utxo_set:
            print(f"Error: UTXO already exists for (tx_id={tx_id}, index={index})")
            return False
        
        self.utxo_set[key] = (float(amount), owner)
        return True
    
    def remove_utxo(self, tx_id, index):
        pass

    def get_balance(self, owner):
        pass

    def exists(self, tx_id, index):
        pass

    def get_utxos_for_owner(self, owner):
        pass
        

        