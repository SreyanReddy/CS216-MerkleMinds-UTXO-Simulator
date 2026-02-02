# Implement transaction logic
import time
import random

class transaction:
    def __init__(self,inputs,outputs):
        self.tx_id = self._generate_tx_id()
        self.inputs=inputs
        self.outputs=outputs

        def _generate_tx_id(self):
            return f"tx_{int(time.time())}_{random.randint(1000,9999)}"



