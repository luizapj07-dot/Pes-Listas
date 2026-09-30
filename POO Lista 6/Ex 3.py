class contaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self):
        valor = int(input("Digite um valor: "))
        self.saldo = self.saldo + valor

    def sacar(self):
        saque = int(input("Digite um saque: "))
        self.saldo = self.saldo - saque

    def mostrar_saldo(self):
        print(self.saldo)

contaBancaria1 = contaBancaria("Zan", 0)

contaBancaria1.depositar()
contaBancaria1.sacar()
contaBancaria1.mostrar_saldo()