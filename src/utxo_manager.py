class UTXOManager():
    def __init__(self):
        self.utxo_set = {}

    def add_utxo(self, tx_id, index, amount, owner):

        if tx_id is None or tx_id == "":
            print("Error: Transaction ID cannot be empty")
            return False
        if isinstance(index, int) == False or index < 0:
            print("Error: Index must be a non-negative integer")
            return False
        if isinstance(amount, (int, float)) == False or amount <=0:
            print("Error: Amount must be a positive number")
            return False
        if owner is None or isinstance(owner, str) == False or owner.strip() == "":
            print("Error: Owner must be a non-empty string")
            return False

        tx_id = tx_id.strip()
        owner = owner.strip()

        key = (tx_id, index)
        if key in self.utxo_set:
            print(f"Error: UTXO already exists for (tx_id={tx_id}, index={index})")
            return False
        
        self.utxo_set[key] = (float(amount), owner)
        return True
    
    def remove_utxo(self, tx_id, index):

        if isinstance(tx_id, str) == False or tx_id.strip() == "":
            print("Error: Transaction ID must be a non-empty string")
            return False
        
        tx_id = tx_id.strip()

        if isinstance(index, int) == False or index < 0:
            print("Error: Index must be a non-negative integer")
            return False
        
        key = (tx_id, index)

        if key not in self.utxo_set:
            print(f"Error: UTXO set not found for (tx_id={tx_id}, index={index})")
            return False
        
        del self.utxo_set[key]
        return True

    def get_balance(self, owner):
        
        if isinstance(owner, str) == False or owner.strip() == "":
            print("Error: Owner must be a non-empty string")
            return False
        
        owner = owner.strip()

        total = 0.0
        for (amount, utxo_owner) in self.utxo_set.values():
            if utxo_owner == owner:
                total += float(amount)
        return total
    
    def exists(self, tx_id, index):
        
        if isinstance(tx_id, str) == False or tx_id.strip() == "":
            print("Error: Transaction ID must be a non-empty string")
            return False
        if isinstance(index, int) == False or index < 0:
            print("Error: Index must be a non-negative integer")
            return False
        
        if (tx_id, index) in self.utxo_set:
            return True
        return False
        
    def get_utxos_for_owner(self, owner):

        if isinstance(owner, str) == False or owner.strip() == "":
            print("Error: Owner must be a non-empty string")
            return False
        
        owner = owner.strip()
        output = []

        for (tx_id, index), (amount, utxo_owner) in self.utxo_set.items():
            if utxo_owner == owner:
                output.append(((tx_id, index), amount))
        
        return output
        
        
        

        