class Usuario:	
    nombre_banco = "Banco Dojo Internacional"
    def __init__(self, nombre, email, balance):
        self.name = nombre
        self.email = email
        self.balance_cuenta = balance

    def hacer_depósito(self, amount):	# toma un argumento que es el monto del depósito
        self.balance_cuenta += amount	# la cuenta del usuario específico aumenta en la cantidad del valor recibido
        print("Depósito realizado. Balance: ", self.balance_cuenta)
        return self
        
    def hacer_retiro(self, monto):
        if monto <= self.balance_cuenta:
            print( "Retiro realizado. Balance: ", self.balance_cuenta)
        else:
            print( "Saldo insuficiente. Balance: ", self.balance_cuenta)
        return self
    
    def mostrar_balance_usuario(self):
        print("Nombre del usuario: ", self.name)
        print( "Balance: ", self.balance_cuenta)
        return self
    
    
guido = Usuario("Guido van Rossum", "guido@python.com", 5000 )
monty = Usuario("Monty Python", "monty@python.com", 6000 )
martin = Usuario("Martin Vargas", "martin@python.com", 4000)
print(guido.name)	
print(monty.name)	
print(martin.name)

guido.hacer_depósito(100).hacer_depósito(200).hacer_depósito(700).hacer_retiro(500).mostrar_balance_usuario()

monty.hacer_depósito(500).hacer_depósito(50).hacer_retiro(100).mostrar_balance_usuario()

martin.hacer_depósito(700).hacer_retiro(500).hacer_retiro(200).hacer_retiro(100).mostrar_balance_usuario()

