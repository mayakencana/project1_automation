from modules.library_item import LibraryItem

class Dvd(LibraryItem):
    def __init__(self, title, subject, upc, actors, director, genre):
        LibraryItem.__init__(self, title, subject, upc)
        self.actors=actors
        self.director=director
        self.genre=genre