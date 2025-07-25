import heapq
import time

class FraudAlert:
    def __init__(self, alert_id, priority, message, timestamp):
        self.alert_id = alert_id
        self.priority = priority
        self.message = message
        self.timestamp = timestamp

    def __lt__(self, other):
        return self.priority < other.priority

class FraudAlertManager:
    def __init__(self):
        self.alert_queue = []
        self.alert_map = {}

    def insert_alert(self, alert):
        heapq.heappush(self.alert_queue, alert)
        self.alert_map[alert.alert_id] = alert

    def delete_alert(self, alert_id):
        if alert_id in self.alert_map:
            alert = self.alert_map[alert_id]
            self.alert_queue.remove(alert)
            heapq.heapify(self.alert_queue)
            del self.alert_map[alert_id]

    def update_alert(self, alert_id, new_priority, new_message):
        if alert_id in self.alert_map:
            alert = self.alert_map[alert_id]
            alert.priority = new_priority
            alert.message = new_message
            self.alert_queue.remove(alert)
            heapq.heapify(self.alert_queue)
            heapq.heappush(self.alert_queue, alert)

    def get_next_alert(self):
        if self.alert_queue:
            return heapq.heappop(self.alert_queue)
        return None

    def trigger_notifications(self, alert):
        print(f"Alert ID: {alert.alert_id}, Priority: {alert.priority}, Message: {alert.message}, Timestamp: {alert.timestamp}")

# Example usage
if __name__ == "__main__":
    manager = FraudAlertManager()
    alert1 = FraudAlert(1, 3, "Potential fraud detected", time.time())
    alert2 = FraudAlert(2, 1, "High-risk transaction", time.time())
    alert3 = FraudAlert(3, 2, "Suspicious activity", time.time())

    manager.insert_alert(alert1)
    manager.insert_alert(alert2)
    manager.insert_alert(alert3)

    while True:
        next_alert = manager.get_next_alert()
        if next_alert:
            manager.trigger_notifications(next_alert)
        else:
            break