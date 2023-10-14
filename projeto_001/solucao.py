class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class PointOfSale:
    def __init__(self):
        self.products = []
        self.cart = []
    
    def add_product(self, product, quantity=1):
        for _ in range(quantity):
            self.cart.append(product)
    
    def calculate_total(self):
        total = sum(product.price for product in self.cart)
        return total
    
    def process_payment(self, amount_paid):
        total = self.calculate_total()
        if amount_paid >= total:
            change = amount_paid - total
            return f"Payment successful. Change: ${change:.2f}"
        else:
            return "Insufficient payment. Please pay the full amount."

# Criar produtos
product1 = Product("Item 1", 10.00)
product2 = Product("Item 2", 20.00)
product3 = Product("Item 3", 15.00)

# Inicializar o PDV
pos = PointOfSale()

# Adicionar produtos ao carrinho
pos.add_product(product1)
pos.add_product(product2, quantity=2)
pos.add_product(product3)

# Calcular o total
total = pos.calculate_total()
print(f"Total: ${total:.2f}")

# Processar pagamento
amount_paid = float(input("Enter the amount paid: "))
result = pos.process_payment(amount_paid)
print(result)

