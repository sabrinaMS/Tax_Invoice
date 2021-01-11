from Order import Order

# recebe o nome do estabelecimento
def get_Supermarket():
    supermarket = input("Qual o nome do Estabelecimento? ")
    return supermarket

# recebe uma quantidade (int) de produtos.
def get_amount():
    while True:
        try:
            amount = int(input("Qual a quantidade de produtos neste pedido? "))
        except:
            continue
        else:
            return amount

# cria um pedido, que é composto por nome do estabelecimento e pela quantidade de produto
def create_order():
    supermarket = get_Supermarket()
    amount = get_amount()
    order = Order(supermarket, amount)

    return order

# recebe novos pedidos, é possível inserir quantos pedidos/estabelecimentos quiser
def receive_order():
    orders = []
    add_more_orders = "S"

    print("NOTA FISCAL DE CARGA")
    print("Cadastre aqui os pedidos referentes a esta carga")
    print("")

    while add_more_orders == "S" or add_more_orders == "s":
        order = create_order()
        orders.append(order)
        add_more_orders = input("Deseja inserir mais algum pedido? (S/N)")

    return orders

