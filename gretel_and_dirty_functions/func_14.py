import threading
import requests
from queue import Queue

class APIManager:
    def __init__(self, api_url, max_threads=10):
        self.api_url = api_url
        self.max_threads = max_threads
        self.queue = Queue()
        self.threads = []
        self.lock = threading.Lock()

    def worker(self):
        while True:
            item = self.queue.get()
            if item is None:
                break
            self.process_item(item)
            self.queue.task_done()

    def process_item(self, item):
        with self.lock:
            response = requests.post(self.api_url, json=item)
            # Handle the response as needed
            print(f"Response for {item}: {response.status_code}")

    def add_task(self, item):
        self.queue.put(item)

    def start(self):
        for _ in range(self.max_threads):
            thread = threading.Thread(target=self.worker)
            thread.start()
            self.threads.append(thread)

    def stop(self):
        for _ in range(self.max_threads):
            self.queue.put(None)
        for thread in self.threads:
            thread.join()