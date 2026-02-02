
class Movie:
    def __init__(self, title: str, good_ending: bool, year: int):
        self.title = title
        self.good_ending = good_ending
        self.year = year


# A class representing a movie with title, good ending status, and release year.
    def get_info(self):
        ending = "Good Ending" if self.good_ending else "Bad Ending"
        return f"{self.title} ({self.year}), {ending}"
# Method to get formatted information about the movie.


if __name__ == '__main__':
    inception = Movie("Inception", good_ending=True, year=2010)
    print(inception.get_info())