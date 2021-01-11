from  Order import Order

class Invoice:
    # cálculo dos valores da nota:
    # feito a partir da lista de pedidos recebidos, referentes a carga de produtos solicitada
    # cada pedido é salva no array de lista de pedidos/carga

    def apply_discount(amount):
        if amount >= 200:
            return 4
        elif 100 <= amount >= 199:
            return 4.3
        else:
            return 4.5

    # cálculo de imposto do pedido geral
    def calculate_taxes(orders):
        calculated_orders_taxes =[]
        for order in orders:
            supermarket = order.supermarket
            product_amount = order.product_amount
            product_total_price = order.product_amount * Invoice.apply_discount(product_amount)
            icms = product_total_price * 0.18
            ipi = product_total_price * 0.04
            pis = product_total_price * 0.0186
            cofins = product_total_price * 0.0854
            total_taxes = icms + ipi + pis + cofins

            calculated_orders_taxes.append(Order(supermarket, product_amount, product_total_price, icms, ipi, pis, cofins, total_taxes))
            print()
        return calculated_orders_taxes

    # impressão da nota com valores individuais de pedidos e valor total da carga
    def print_invoice(loads):
        taxes_total_amount = 0
        invoice_total_amount = 0.0

        print("------NOTA FISCAL------")
        for load in loads:
            print(
                "\n ** ", load.get_supermarket(), " **"
                "\n Valor: R${:.2f}".format(load.get_product_total_price()) ,
                "\n ICMS: R${:.2f}".format(load.get_ICMS()),
                "\n IPI: R${:.2f}".format(load.get_IPI()),
                "\n PIS: R${:.2f}".format(load.get_PIS()),
                "\n COFINS: R${:.2f}".format(load.get_COFINS()),
                "\n Desconto: R${:.2f}".format(load.get_product_amount() * 4.5 - load.get_product_total_price()),
                "\n Impostos: R${:.2f}".format(load.get_total_taxes())
                )
            taxes_total_amount += (load.get_total_taxes())
            invoice_total_amount = invoice_total_amount + (load.get_product_total_price())

        print("--------------------------------")
        print("Total Impostos: R${:.2f}".format(taxes_total_amount))
        print("Total: R${:.2f}".format(invoice_total_amount))
