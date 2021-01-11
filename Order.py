class Order:
    supermarket = str
    product_amount = int
    product_total_price = float
    ICMS = float
    IPI = float
    PIS = float
    COFINS= float
    total_taxes = float

    def __init__(self, supermarket, product_amount, product_total_price = 0.0, ICMS = 0.0, IPI = 0.0, PIS = 0.0, COFINS= 0.0, total_taxes = 0.0):
        self.supermarket = supermarket
        self.product_amount = product_amount
        self.product_total_price = product_total_price
        self.ICMS = ICMS
        self.IPI = IPI
        self.PIS = PIS
        self.COFINS= COFINS
        self.total_taxes= total_taxes

    def set_supermarket(self, supermarket):
        self.supermarket = supermarket

    def get_supermarket(self):
        return self.supermarket

    def set_product_amount(self, product_amount):
        self.product_amount = product_amount

    def get_product_amount(self):
        return self.product_amount

    def set_product_total_price(self, product_total_price):
        self.product_total_price = product_total_price

    def get_product_total_price(self):
        return self.product_total_price

    def set_ICMS(self, ICMS):
        self.ICMS = ICMS

    def get_ICMS(self):
        return self.ICMS

    def set_IPI(self, IPI):
        self.IPI = IPI

    def get_IPI(self):
        return self.IPI

    def set_PIS(self, PIS):
        self.PIS = PIS

    def get_PIS(self):
        return self.IPI

    def set_COFINS(self, COFINS):
        self.IPI = COFINS

    def get_COFINS(self):
        return self.COFINS

    def set_total_taxes(self, total_taxes):
        self.IPI = total_taxes

    def get_total_taxes(self):
        return self.total_taxes
