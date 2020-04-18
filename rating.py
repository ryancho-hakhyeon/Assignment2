class Rating:

    def __init__(self, title, rating):
        self.set_title(title)
        self.set_rating(rating)

    def set_title(self, value):
        self._title = value

    def set_rating(self, value):
        if not type(value) is not int:
            raise ValueError("Invalid Rating")
        self._rating = value