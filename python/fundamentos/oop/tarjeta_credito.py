class TarjetaCredito:
    tarjetas = []  

    def __init__(self, saldo_pagar=0, limite_credito=10000, intereses=0.05):
        self.saldo_pagar = saldo_pagar
        self.limite_credito = limite_credito
        self.intereses = intereses
        TarjetaCredito.tarjetas.append(self)  

    def compra(self, monto):
        if self.saldo_pagar + monto > self.limite_credito:
            print("Tarjeta Rechazada, has alcanzado tu limite de credito")
        else:
            self.saldo_pagar += monto
        return self  

    def pago(self, monto):
        self.saldo_pagar -= monto
        return self

    def mostrar_info_tarjeta(self):
        print(f"Saldo a Pagar: ${self.saldo_pagar}")
        return self

    def cobrar_interes(self):
        self.saldo_pagar += self.saldo_pagar * self.intereses
        return self

    @classmethod
    def mostrar_todas_las_tarjetas(cls):
        print("Informacion de todas las tarjetas:")
        for tarjeta in cls.tarjetas:
            tarjeta.mostrar_info_tarjeta()


# Tarjetas 
Tarjeta1 = TarjetaCredito(0, 30000, 0.05)
Tarjeta2 = TarjetaCredito(0, 20000, 0.04)
Tarjeta3 = TarjetaCredito(0, 10000, 0.03)

# encadenamiento
Tarjeta1.compra(5000).compra(7000).pago(2000).cobrar_interes().mostrar_info_tarjeta()
Tarjeta2.compra(3000).compra(4000).compra(5000).pago(2000).pago(1000).cobrar_interes().mostrar_info_tarjeta()
Tarjeta3.compra(2000).compra(3000).compra(4000).compra(3000).compra(2000).mostrar_info_tarjeta()

# BONUS
TarjetaCredito.mostrar_todas_las_tarjetas()
