class Usuario:	
    nombre_banco = "Banco Dojo Internacional"
    def __init__(self, nombre, email, balance):
        self.name = nombre
        self.email = email
        self.balance_cuenta = balance

    def hacer_depósito(self, amount):	# toma un argumento que es el monto del depósito
        self.balance_cuenta += amount	# la cuenta del usuario específico aumenta en la cantidad del valor recibido
        print("Depósito realizado. Balance: ", self.balance_cuenta)
    
    def hacer_retiro(self, monto):
        if monto <= self.balance_cuenta:
            print( "Retiro realizado. Balance: ", self.balance_cuenta)
        else:
            print( "Saldo insuficiente. Balance: ", self.balance_cuenta)
    
    def mostrar_balance_usuario(self):
        print("Nombre del usuario: ", self.name)
        print( "Balance: ", self.balance_cuenta)
    
    
guido = Usuario("Guido van Rossum", "guido@python.com", 5000 )
monty = Usuario("Monty Python", "monty@python.com", 6000 )
martin = Usuario("Martin Vargas", "martin@python.com", 4000)
print(guido.name)	
print(monty.name)	
print(martin.name)

guido.hacer_depósito(100)
guido.hacer_depósito(200)
guido.hacer_depósito(700)
guido.hacer_retiro(500)
monty.hacer_depósito(500)
monty.hacer_depósito(50)
monty.hacer_retiro(100)
martin.hacer_depósito(700)
martin.hacer_retiro(500)
martin.hacer_retiro(200)
martin.hacer_retiro(100)

guido.mostrar_balance_usuario()
monty.mostrar_balance_usuario()
martin.mostrar_balance_usuario()



