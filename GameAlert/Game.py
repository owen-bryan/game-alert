class Game:

    def __init__(self, title, releaseDate):
        self.title = title
        self.releaseDate = releaseDate
    
    def __str__(self):
        return "{0} Release Date: {1}".format(self.title, self.releaseDate)