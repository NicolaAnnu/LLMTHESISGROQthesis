class MobileBankingUserLocation:
    def __init__(self, user_id):
        self.user_id = user_id
        self.last_known_location = None

    def update_location(self, latitude, longitude):
        self.last_known_location = (latitude, longitude)

    def get_location(self):
        return self.last_known_location