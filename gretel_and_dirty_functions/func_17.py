import threading

class AccountLockManager:
    def __init__(self):
        self.locks = {}
        self.lock = threading.Lock()

    def lock_account(self, user_id):
        with self.lock:
            if user_id not in self.locks:
                self.locks[user_id] = threading.Lock()
            self.locks[user_id].acquire()

    def unlock_account(self, user_id):
        with self.lock:
            if user_id in self.locks:
                self.locks[user_id].release()
                if not self.locks[user_id].locked():
                    del self.locks[user_id]

    def is_account_locked(self, user_id):
        with self.lock:
            return user_id in self.locks and self.locks[user_id].locked()