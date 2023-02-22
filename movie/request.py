import requests


#! tmdb den film apilerini cekmek icin bir class tanımlarız.
#! class altında init function altında gereklilikleri tanımlarız. page bilgisini dışarıdan aliyoruz. örnk: Api(<page_number>).get_movie()
class Api:

    def __init__(self, page, query=None, category=None):
        self.headers = {'Accept':'application/json'}         #!kullanım zorunlu değil. Sadece json tipinde verileri kabul eder.
        self.api_key = "b3b9cd695e1c4a5f201741b55d4d4703"    #!tmdb api key
        self.page = page
        self.query = query
        self.category = category
    

    # rastgele filmleri almak için kullanılan function. api_key ve page bilgilerini init fonksiyonundan aldık.
    # request.get ile gelen bilgileri json methodu ile python un anlayabileceği hale getidik ve return ettik.
    # fonksiyonu kullanmak istediğimiz yerde class altında function olarak cağrılmalı. örn: Api(<page_number>).get_movie() -> movie/views.py de kullanımı mevcut
    #
    def get_movie(self):
        r = requests.get(f'https://api.themoviedb.org/3/discover/movie?api_key={self.api_key}&sort_by=popularity.desc&page={self.page}')
        return r.json()

    def get_trend_movies(self):
        r = requests.get(f'https://api.themoviedb.org/3/trending/movie/week?api_key={self.api_key}&page={self.page}')
        return r.json()

    def get_top_rated_movies(self):
        r = requests.get(f'https://api.themoviedb.org/3/movie/top_rated?api_key={self.api_key}&page={self.page}')   
        return r.json()

    def get_top_rated_tv(self):
        r = requests.get(f'https://api.themoviedb.org/3/tv/top_rated?api_key={self.api_key}&page={self.page}')
        return r.json()

    def get_coming_soon(self):
        r = requests.get(f'https://api.themoviedb.org/3/movie/upcoming?api_key={self.api_key}&page={self.page}')
        return r.json()

    def get_trend_tv(self):
        r = requests.get(f'https://api.themoviedb.org/3/trending/tv/week?api_key={self.api_key}&page={self.page}')
        return r.json()

    def get_popular_movie(self):
        r = requests.get(f'https://developers.themoviedb.org/3/movies/get-popular-movies?api_key={self.api_key}&page={self.page}')
        return r.json()

    def search_movie(self):
        r = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key={self.api_key}&query={self.query}')
        return r.json()

    def get_categories(self):
        r = requests.get(f'https://api.themoviedb.org/3/discover/movie?api_key={self.api_key}&page={self.page}&with_genres={self.category}&sort_by=vote_average.desc&vote_count.gte=10')
        return r.json()



#https://developers.themoviedb.org/3/discover/movie-discover
#https://api.themoviedb.org/3/movie/top_rated
#https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc
#https://api.themoviedb.org/3/discover/movie?primary_release_year=2022&sort_by=vote_average.desc
#https://api.themoviedb.org/3/discover/tv?with_genres=18
#https://api.themoviedb.org/3/genre/movie/list
#https://api.themoviedb.org/3/trending/all/week
#https://api.themoviedb.org/3/search/keyword?query=parasite
#https://developers.themoviedb.org/3/movies/get-popular-movies
