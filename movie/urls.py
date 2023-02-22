from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('movies', views.movies, name='movies'),
    path('series', views.series, name='series'),
    path('movies/categories', views.movie_categories, name='category'),
    path('user/login', views.login_section, name='login'),
    path('user/register', views.register_section, name='register'),
    path('user/logout', views.logout_section, name='logout'),

]
