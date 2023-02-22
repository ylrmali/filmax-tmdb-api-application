from django.shortcuts import render, redirect
from django.http import HttpRequest
from. request import Api  # class import edilir. import Api class
from django.contrib.auth import authenticate, login, logout  #django authenticating methods
from django.contrib.auth.models import User  #django User model

# index-home sayfasımızı renderlayan function.
# movie/request.py deki apileri çekmek icin kullandığımız functionları import etmeliyiz.
# çekdiğimiz dataları context yardımıyla index.html sayfamıza gönderiyoruz.
# gönderdiğimiz datalarin dictionary şeklinde yollanması gerekiyor
# gönderiler bilgiler index.html sayfasında {{<name>.<value>}} şeklinde kullanılır.
# name -> datas , top_rated...  value ->  apiden gelen json içindeki keyler örn filme ait title bilgisi. title,name... (data['results'] u print edip gelen degerleri incele)
#----
# a function which is render index page
# u have to import a few function which there in movie/request.py
# send datas where we get they collected tmdb to index.html page with help of the context.
# you must have to use python-dictionary syntax
# use this datas in index.html page like this <if u are using for loop. -> {{movie.title}} else {{movie}}
def index(request):
    if request.GET.get('search'):
        query = request.GET.get('search', '')
        movie = Api(1, query).search_movie()
        type = request.POST['type']
        context = {
            'movie': movie['results'],
            'query': query,
            'type': type,
        }
        return render(request, 'movie/search.html', context)
    else:
        data = Api(1).get_movie()
        top_rated = Api(1).get_top_rated_movies()
        top_rated_tv = Api(1).get_top_rated_tv()
        coming_soon = Api(1).get_coming_soon()
        trend_tv = Api(1).get_trend_tv()
        trend_movies = Api(1).get_trend_movies()

        context = {
            'datas' : data['results'],
            'top_rated' : top_rated['results'],
            'top_rated_tv' : top_rated_tv['results'],
            'coming_soon' : coming_soon['results'],
            'trend_tv': trend_tv['results'],
            'trend_movies' : trend_movies['results'],
        }

        return render(request,'movie/index.html',context) # html page' ın render edilmesi ve context 'in index.html e yollanması ve fonksiyonun bunları return etmesi


# login islemini gerceklestiren fonksiyon
# login function
def login_section(request):
    
    if request.method == 'POST':

        # login işlemi
        username = request.POST['username']  # inputa verdigimiz name e göre cağırma islemi yapılır.
        password = request.POST['password']  
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/', kwargs={'username': username})
        else:
            return render(request, 'movie/login.html', {'error': 'Username or password is incorrect!'})
    
    return render(request,'movie/login.html')

# register islemini gerceklestiren function
# register function
# get the values of form and define
def register_section(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        password = request.POST['password']  
        repassword = request.POST['repassword']
        email = request.POST['email']

        if repassword == password:
            if User.objects.filter(username=username).exists():
                return render(request, 'movie/register.html', {
                    'error': f'{username} already exists!',
                })
            else:
                if User.objects.filter(email=email).exists():
                    return render(request, 'movie/register.html', {
                        'error': f'{email} already exists!',
                    })
                else:
                    user = User.objects.create_user(username=username, email=email, password=password,
                                                    first_name=first_name, last_name=last_name)
                    user.save()
                    return redirect('login')


        else:
            return render(request, 'movie/register.html', {'error': 'Your passwords are not match!'})

    return render(request, 'movie/register.html')


# logout function
def logout_section(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')



# film sayfasını renderlama ve apileri alma
# get movies and rendering movies page
def movies(request):
    if request.GET.get('search'):
        query = request.GET.get('search', '')
        movie = Api(1, query).search_movie()
        context = {
            'movie': movie['results'],
            'query': query,
        }
        return render(request, 'movie/search.html', context)
    else:
        url = request.GET.get('page', '')  # get url params (page number)
        movies = Api(url).get_movie()   # gelen page numarasına gore filmleri apiden cektik
        context = {
            'movies': movies['results'],
        }
        return render(request, 'movie/movies_page.html', context)



# diziler sayfasını renderlama ve apilerini alma
# get series' apis and rendering series page.
def series(request):
    if request.GET.get('search'):
        query = request.GET.get('search', '')
        movie = Api(1, query).search_movie()
        context = {
            'movie': movie['results'],
            'query': query,
        }
        return render(request, 'movie/search.html', context)
    else:
        url = request.GET.get('page', '')  # get url params (page number)
        series = Api(url).get_top_rated_tv()
        context = {
            'series': series['results'],
        }
        return render(request, 'movie/series_page.html', context)

# categories page function
# firstly, we get page param in url
# use page param as page number -> Api(<page>,
# then check which condition is true
# then send category number to Api class(init function)
def movie_categories(request):
    page = request.GET.get('page')

    if(request.GET.get('category') == 'action'):
        movies = Api(page, category=28).get_categories()
    elif (request.GET.get('category') == 'comedy'):
        movies = Api(page, category=35).get_categories()
    elif (request.GET.get('category') == 'drama'):
        movies = Api(page, category=18).get_categories()
    elif (request.GET.get('category') == 'crime'):
        movies = Api(page, category=80).get_categories()

    context = {
        'movies': movies['results'],
    }
    return render(request, 'movie/movies-category.html', context)

