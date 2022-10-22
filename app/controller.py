class Controller:
    def __init__(self, db_session):
        self.flights = []

    def update(self):
        return self.flights