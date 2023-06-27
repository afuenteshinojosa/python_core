class CuentaBancaria:
    nombre_banco = "Primer Dojo Nacional"
    todas_las_cuentas = []

    def __init__(self, balance, tasa_int):
        self.balance_cuenta = balance
        self.tasa_int = tasa_int
        CuentaBancaria.todas_las_cuentas.append(self)

    def generar_interes(self):
        interes_generado = self.balance_cuenta * self.tasa_int
        self.balance_cuenta += interes_generado
        print("Se realizó un interés de:", self.tasa_int)
        return self

class Usuario:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.cuenta = CuentaBancaria(balance=0, tasa_int=0.01)

    def hacer_depósito(self, amount):
        self.cuenta.balance_cuenta += amount
        print("Depósito realizado. Balance:", self.cuenta.balance_cuenta)
        return self

    def hacer_retiro(self, monto):
        if monto <= self.cuenta.balance_cuenta:
            self.cuenta.balance_cuenta -= monto
            print("Retiro realizado. Balance:", self.cuenta.balance_cuenta)
        else:
            print("Saldo insuficiente. Balance:", self.cuenta.balance_cuenta)
        return self

    def mostrar_info_cuenta(self):
        print("Balance final:", self.cuenta.balance_cuenta)
        return self

# Instancias cuenta
cuenta1 = CuentaBancaria(balance=5000, tasa_int=0.05)
cuenta2 = CuentaBancaria(balance=3000, tasa_int=0.19)
cuenta3 = CuentaBancaria(balance=4000, tasa_int=0.09)
