from tarjeta_credito import TarjetaCredito

class Usuario:

    def __init__(self, nombre, apellido, email):

        self.nombre = nombre

        self.apellido = apellido

        self.email = email

        self.tarjetas = []

    def hacer_compra(self, monto):
        self.tarjeta.compra(monto) 
        return self

    def pagar_tarjeta(self, monto):
        self.tarjeta.pago(monto)
        return self
    
    def mostrar_saldo_usuario(self, monto):
        self.tarjeta.mostrar_info_tarjeta(monto)
        return self

    def transferir_deuda(self, otro_usuario, monto):
        if monto > self.saldo_pagar:
            print(f"{self.nombre} {self.apellido} {self.email} ya pagaste tu deuda.")
        else:
            self.saldo_pagar -= monto
            otro_usuario.saldo_pagar += monto

    def agregar_tarjeta(self, saldo_pagar=0, limite_credito=30000, intereses=0.19):
        nueva_tarjeta = TarjetaCredito(saldo_pagar, limite_credito, intereses) 
        self.tarjetas.append(nueva_tarjeta)
    

# Crear instancias de Usuario
usuario1 = Usuario("Nariyoshi", "Miyagi", "miyagi@email.com")(0, 20000, 0.015)
usuario2 = Usuario("Daniel", "LaRusso", "daniel@email.com")(0, 20000, 0.015)
usuario3 = Usuario("Johnny", "Lawrence", "johnny@email.com")(0, 20000, 0.015)


# Punto 1
usuario1.hacer_compra(100)
usuario1.hacer_compra(50)
usuario1.pagar_tarjeta(80)
usuario1.mostrar_saldo_usuario()

# Punto 2
usuario2.hacer_compra(200)
usuario2.pagar_tarjeta(50)
usuario2.pagar_tarjeta(100)
usuario2.mostrar_saldo_usuario()

# Punto 3
usuario3.hacer_compra(500)
usuario3.hacer_compra(300)
usuario3.hacer_compra(200)
usuario3.pagar_tarjeta(400)
usuario3.pagar_tarjeta(200)
usuario3.pagar_tarjeta(100)
usuario3.pagar_tarjeta(50)
usuario3.mostrar_saldo_usuario()