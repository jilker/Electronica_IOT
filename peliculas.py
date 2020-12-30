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
    def search(self):
        discover = tmdb.Discover()       
        return discover.movie(primary_release_date_gte = self.year, language = self.language , region = self.region , sort_by = 'popularity.desc')

    def show_image(self,url):
        url = 'https://image.tmdb.org/t/p/w500' + url
        response = requests.get(url,stream=True) 
        img = Image.open(response.raw)
        img.show()

    def list_res(self,response):
        max = 5
        for s in response['results']:
            print(s['title'],s['id'], s['release_date'])


def test():
    peliculas = Peliculas()
    res = peliculas.search()
    peliculas.list_res(res)
    print('pause')
if __name__ == "__main__":
    test() 