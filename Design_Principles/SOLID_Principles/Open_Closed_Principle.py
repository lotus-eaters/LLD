# This principle states that "Software entities (classes, modules, functions, etc.) should be open for "
# "extension, but closed for modification" which means you should be able to extend a class behavior, 
# without modifying it.

from abc import ABC,abstractmethod
class ProcessPayment:
    @abstractmethod #Pure Virtual Function
    def processpayment(self,amount):
        pass
class CreditCardPayment(ProcessPayment):
    def processpayment(self,amount):
        print(f'Payment processed via a Credit Card {amount}')
#Extended Functionality
class PayPalPayment(ProcessPayment):
    def processpayment(self, amount):
        print(f'Payment processed via a Paypal {amount}')

def processpayment(paymentmode,amount):
    paymentmode.processpayment(amount)

if __name__=='__main__':
    CreditCardProccessor=CreditCardPayment()
    PayPalProcessor=PayPalPayment()
    processpayment(CreditCardProccessor,100.0)
    processpayment(PayPalProcessor,150.0)

# Explanation of the above code:

# Base Class (PaymentProcessor): This is an abstract base class with a pure virtual function processPayment(). It defines a common interface for all payment processors.
# CreditCardPaymentProcessor: This class implements the payment processing logic for credit card payments.
# PayPalPaymentProcessor: This new class extends the functionality by implementing the payment processing for PayPal payments.
# Main Function: The processPayment function takes a pointer to a PaymentProcessor and calls the processPayment() method. This allows you to use any processor that implements the PaymentProcessor interface without changing existing code.
        