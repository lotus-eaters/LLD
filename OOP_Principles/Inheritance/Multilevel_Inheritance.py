class Payment:
    def __init__(self, amount, transaction_id):
        self.amount = amount
        self.transaction_id = transaction_id
    
    def process(self):
        print(f"Processing ${self.amount} for TXN {self.transaction_id}")

class DigitalPayment(Payment):
    def __init__(self, amount, transaction_id, wallet_id):
        super().__init__(amount, transaction_id)
        self.wallet_id = wallet_id
    
    def verify_wallet(self):
        print(f"Verifying wallet {self.wallet_id}")

class CreditCardPayment(DigitalPayment):
    def __init__(self, amount, transaction_id, wallet_id, card_number):
        super().__init__(amount, transaction_id, wallet_id)
        self.card_number = card_number
    
    def charge_card(self):
        self.verify_wallet()  # Calls parent
        print(f"Charging card ****{self.card_number[-4:]}")

payment = CreditCardPayment(150.00, "TXN789", "WALLET_XYZ", "1234-5678-9012-3456")
payment.process()       # Processing $150.0 for TXN TXN789 (grandparent)
payment.charge_card()   # Verifying wallet WALLET_XYZ \n Charging card ****3456
