import Controller as Controller
from Invoice import Invoice

# Fazer um pedido
order = Controller.receive_order()

# Calcular os impostos deste pedido/carga
order_taxes = Invoice.calculate_taxes(order)

# Imprimir a nota da carga
Invoice.print_invoice(order_taxes)

