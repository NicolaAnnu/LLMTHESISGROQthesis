import threading
from collections import deque

class TransactionQueue:
    def __init__(self):
        self.queue = deque()
        self.lock = threading.Lock()

    def enqueue(self, transaction):
        with self.lock:
            self.queue.append(transaction)

    def dequeue(self):
        with self.lock:
            if self.queue:
                return self.queue.popleft()
            return None

    def update_status(self, transaction_id, new_status):
        with self.lock:
            for i, transaction in enumerate(self.queue):
                if transaction['id'] == transaction_id:
                    self.queue[i]['status'] = new_status
                    return True
            return False

    def get_transaction(self, transaction_id):
        with self.lock:
            for transaction in self.queue:
                if transaction['id'] == transaction_id:
                    return transaction
            return None

    def get_all_transactions(self):
        with self.lock:
            return list(self.queue)

# Example usage:
if __name__ == "__main__":
    transaction_queue = TransactionQueue()
    transaction_queue.enqueue({'id': 1, 'amount': 100, 'status': 'pending'})
    transaction_queue.enqueue({'id': 2, 'amount': 200, 'status': 'pending'})

    print(transaction_queue.get_all_transactions())
    transaction_queue.update_status(1, 'processed')
    print(transaction_queue.get_transaction(1))
    print(transaction_queue.dequeue())
    print(transaction_queue.get_all_transactions())