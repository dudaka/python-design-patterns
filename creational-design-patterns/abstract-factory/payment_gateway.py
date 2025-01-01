from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def make_payment(self, amount: float) -> str:
        pass
    
class CreditCard(PaymentMethod):
    def make_payment(self, amount: float) -> str:
        return f"Paid ${amount} using Credit Card"
    
class DebitCard(PaymentMethod):
    def make_payment(self, amount: float) -> str:
        return f"Paid ${amount} using Debit Card"
    
class Remita(PaymentMethod):
    def make_payment(self, amount: float) -> str:
        return f"Paid ${amount} using Remita"
    
class NetBanking(PaymentMethod):
    def make_payment(self, amount: float) -> str:
        return f"Paid ${amount} using Net Banking"
    
# ================== Payment Factory ==================

class PaymentFactory(ABC):
    @abstractmethod
    def create_payment(self, payment_method) -> PaymentMethod:
        pass
    
class USPaymentFactory(PaymentFactory):
    def __init__(self):
        self.payments = dict(credit=CreditCard, debit=DebitCard, net_banking=NetBanking)

    def create_payment(self, payment_method) -> PaymentMethod:
        if payment_method in self.payments:
            return self.payments.get(payment_method)()
        return None
    
class CanadaPaymentFactory(PaymentFactory):
    def __init__(self):
        self.payments = dict(credit=CreditCard, net_banking=NetBanking)

    def create_payment(self, payment_method) -> PaymentMethod:
        if payment_method in self.payments:
            return self.payments.get(payment_method)()
        return None
    

class NigeriaPaymentFactory(PaymentFactory):
    def __init__(self):
        self.payments = dict(remita=Remita, net_banking=NetBanking, credit=CreditCard)

    def create_payment(self, payment_method) -> PaymentMethod:
        if payment_method in self.payments:
            return self.payments.get(payment_method)()
        return None
    
