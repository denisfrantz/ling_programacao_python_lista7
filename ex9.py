class ContaExcessao(Exception):
    pass

class Conta:
    def __init__(self, saldo, limite):
        self.saldo = saldo
        self.limite = limite
        
    def setLimite(self):
        return self.limite
    
    def deposita(self,deposita):
        self.saldo = self.saldo + deposita
    
    def saca(self, saca):
        try:
            self.saldo = self.saldo - saca
            if not self.saldo > 0:
                raise ContaExcessao
            
        except ContaExcessao:
            print("Não é possível sacar esse valor pois seu saldo irá ficar negativo!")

c = Conta(1000, 10000)
c.saca(1000)