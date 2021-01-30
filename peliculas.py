import tmdbsimple as tmdb
import matplotlib.pyplot as plt
from PIL import Image
import requests
class Peliculas():
    def __init__(self):
        tmdb.API_KEY = tmdb.API_KEY = '3651998862dca081be4b935c5292cf51'
        self.genre_list = self.get_genres()
        self.language = 'es'
        self.region = 'es'
        self.year = '2000-01-01'
    def get_genres(self):
        genre = tmdb.Genres()
        genre = genre.movie_list()
        genre = genre['genres']
        for it in range(0,genre.__len__()):
            genre[it]['Allow'] = 1
        return genre
    def search(self,page):
        discover = tmdb.Discover()
        without=self.set_genre()
        return discover.movie(primary_release_date_gte = self.year, language = self.language, region = self.region , sort_by = 'popularity.desc' ,page=page,without_genres=without)
    def list_res(self,response):
        max = 5
        for s in response['results']:
            print(s['title'],s['id'], s['release_date'])
    def set_genre(self):
        without=""
        for genre in self.genre_list:
            if genre['Allow'] == 0:
                without=without+','+str(genre['id'])
        return without
    def genre_ids2names(self,ids):
        return [genre['name'] for genre in self.genre_list if genre["id"] in ids]


def test():
    peliculas = Peliculas()
    res = peliculas.search('1')
    peliculas.list_res(res)
if __name__ == "__main__":
    test() 