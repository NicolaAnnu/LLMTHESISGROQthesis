import threading
import time

class Order:
    def __init__(self, order_id, quantity, price):
        self.order_id = order_id
        self.quantity = quantity
        self.price = price

class OrderBook:
    def __init__(self):
        self.orders = []
        self.lock = threading.Lock()

    def add_order(self, order):
        with self.lock:
            self.orders.append(order)
            print(f"Order {order.order_id} added. Total orders: {len(self.orders)}")

    def process_orders(self):
        while True:
            with self.lock:
                if self.orders:
                    order = self.orders.pop(0)
                    print(f"Processing order {order.order_id}")
                    # Simulate order processing time
                    time.sleep(0.1)
                else:
                    time.sleep(0.1)

def main():
    order_book = OrderBook()
    processing_thread = threading.Thread(target=order_book.process_orders)
    processing_thread.daemon = True
    processing_thread.start()

    for i in range(1, 11):
        order = Order(i, 10, 100 + i)
        order_book.add_order(order)

    processing_thread.join()

if __name__ == "__main__":
    main()