


from movie.movie import Movie
def main():
    inception = Movie("Inception", good_ending=True, year=2010)
    print(inception.get_info())