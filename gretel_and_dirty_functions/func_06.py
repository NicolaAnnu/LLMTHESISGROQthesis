import threading
import uuid

class AccountIDMeta(type):
    _account_ids = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._account_ids:
                cls._account_ids[cls] = 0
            account_id = cls._account_ids[cls]
            cls._account_ids[cls] += 1
            return f"{cls.__name__}-{account_id}-{uuid.uuid4().hex[:8]}"

class MobileBankingAccount(metaclass=AccountIDMeta):
    pass

# Example usage
if __name__ == "__main__":
    acc1 = MobileBankingAccount()
    acc2 = MobileBankingAccount()
    print(acc1)  # Output: MobileBankingAccount-0-xxxxxxxx
    print(acc2)  # Output: MobileBankingAccount-1-xxxxxxxx