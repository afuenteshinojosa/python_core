class Usuario:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.cuenta = CuentaBancaria(tasa_int=0.02, balance=0)	# añadió esta línea

class CuentaBancaria:
    nombre_banco = "Primer Dojo Nacional"
    todas_las_cuentas = []
    def __init__(self, balance, tasa_int):
        self.balance_cuenta = balance
        self.tasa_int = tasa_int
        CuentaBancaria.todas_las_cuentas.append(self)
        
    def hacer_depósito(self, amount):
        self.balance_cuenta += amount
        print("Depósito realizado. Balance: ", self.balance_cuenta)
        return self
        
    def hacer_retiro(self, monto):
        if monto <= self.balance_cuenta:
            print( "Retiro realizado. Balance: ", self.balance_cuenta)
        else:
            print( "Saldo insuficiente. Balance: ", self.balance_cuenta)
        return self
    
    def mostrar_info_cuenta(self):
        print( "Balance final: ", self.balance_cuenta)
        return self


    def generar_interes(self):
        interes_generado = self.balance_cuenta * self.tasa_int
        self.balance_cuenta += interes_generado
        print( "Se realizó un interés de:", self.tasa_int)
        return self

guido = Usuario("Guido van Rossum", "guido@python.com" )
monty = Usuario("Monty Python", "monty@python.com")
martin = Usuario("Martin Vargas", "martin@python.com")
print(guido.name)	
cuenta1 = CuentaBancaria(1500, 0.07).hacer_depósito(500).hacer_depósito(500).hacer_depósito(500).generar_interes().mostrar_info_cuenta()

print(monty.name)	
cuenta2 = CuentaBancaria(3000, 0.09).hacer_depósito(1000).hacer_depósito(350).hacer_retiro(400).hacer_retiro(800).generar_interes().mostrar_info_cuenta()

print(martin.name)
cuenta3 =  CuentaBancaria(4000, 0.15).hacer_depósito(1000).hacer_depósito(350).hacer_retiro(400).hacer_retiro(800).generar_interes().mostrar_info_cuenta()


