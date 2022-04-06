from app.db import get_driver


class Accessor:

    def __init__(self):
        self.driver = get_driver()
