class OrderBook():
    def __init__(self, orders):
        self.orders = []
    
    def add_order(self, order : Order):
        self.orders.append(order)


class Order:
    def __init__(self, order_id : int, side : str, quantity : int, price : float):
        self.order_id = order_id 
        self.side = side
        self.quantity = quantity
        self.price = price

        def __repr__(self):
            return f"Order({self.order_id}, {self.side}, {self.quantity}@{self.price})"

order = Order(order_id=1, side='buy', quantity=100, price=10.5)

print(order.price)