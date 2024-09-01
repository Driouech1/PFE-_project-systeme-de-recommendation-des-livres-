from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.http import HttpResponse
from . import views
from django.contrib.auth.models import User
from django.contrib import messages
import os
from django.conf import settings
from pfe_project.mood import get_recommendations
import pickle

# Load the model from the pickle file
with open('C:/Users/hajar/Desktop/word2vec_model_recommender.pkl', 'rb') as f:
    model = pickle.load(f)



def recommend_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        genre = request.POST.get('genre')
        recommendations = get_recommendations(title, genre, model)
        
        # Separate recommendations into variables        
        Autor0 = recommendations[0]['Book-Author']
        Autor1 = recommendations[1]['Book-Author']
        Autor2 = recommendations[2]['Book-Author']
        Autor3 = recommendations[3]['Book-Author']
        Autor4 = recommendations[4]['Book-Author']
        Autor5 = recommendations[5]['Book-Author']
        Autor6 = recommendations[6]['Book-Author']
        Autor7 = recommendations[7]['Book-Author']
        Autor8 = recommendations[8]['Book-Author']
        Autor9 = recommendations[9]['Book-Author']

        tit0 = recommendations[0]['Book-Title']
        tit1 = recommendations[1]['Book-Title']
        tit2 = recommendations[2]['Book-Title']
        tit3 = recommendations[3]['Book-Title']
        tit4 = recommendations[4]['Book-Title']
        tit5 = recommendations[5]['Book-Title']
        tit6 = recommendations[6]['Book-Title']
        tit7 = recommendations[7]['Book-Title']
        tit8 = recommendations[8]['Book-Title']
        tit9 = recommendations[9]['Book-Title']

        lien0 = recommendations[0]['Image-URL-M']
        lien1 = recommendations[1]['Image-URL-M']
        lien2 = recommendations[2]['Image-URL-M']
        lien3 = recommendations[3]['Image-URL-M']
        lien4 = recommendations[4]['Image-URL-M']
        lien5 = recommendations[5]['Image-URL-M']
        lien6 = recommendations[6]['Image-URL-M']
        lien7 = recommendations[7]['Image-URL-M']
        lien8 = recommendations[8]['Image-URL-M']
        lien9 = recommendations[9]['Image-URL-M']

        rat0 = recommendations[0]['Book-Rating']
        rat1 = recommendations[1]['Book-Rating']
        rat2 = recommendations[2]['Book-Rating']
        rat3 = recommendations[3]['Book-Rating']
        rat4 = recommendations[4]['Book-Rating']
        rat5 = recommendations[5]['Book-Rating']
        rat6 = recommendations[6]['Book-Rating']
        rat7 = recommendations[7]['Book-Rating']
        rat8 = recommendations[8]['Book-Rating']
        rat9 = recommendations[9]['Book-Rating']

        return render(request, 'authentication/home_page.html', {
            'tit0':tit0, 'tit1':tit1,'tit2':tit2,'tit3':tit3,'tit4':tit4,'tit5':tit5,'tit6':tit6,'tit7':tit7,'tit8':tit8,'tit9':tit9,
            'lien0':lien0,'lien1':lien1,'lien2':lien2,'lien3':lien3,'lien4':lien4,'lien5':lien5 ,'lien6':lien6,'lien7':lien7,'lien8':lien8,'lien9':lien9,
            'Autor0':Autor0,'Autor1':Autor1,'Autor2':Autor2,'Autor3':Autor3,'Autor4':Autor4,'Autor5':Autor5,'Autor6':Autor6,'Autor7':Autor7,'Autor8':Autor8,'Autor9':Autor9,
            'rat0':rat0,'rat1':rat1,'rat2':rat2,'rat3':rat3,'rat4':rat4,'rat5':rat5,'rat6':rat6,'rat7':rat7,'rat8':rat8,'rat9':rat9,
        })
    else:
        return render(request, 'authentication/recommend_form.html')

def home (request):
    return render(request,"authentication/index.html")
def signup(request):
    
    if request.method=="POST":
        #username=request.POST.get('username')
        username=request.POST['username']
        title=request.POST['title']
        genre=request.POST['genre']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        
        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name= title
        myuser.last_name= genre
        myuser.save()
        messages.success(request,"Your account has been succefully created.")
        return redirect('signin')    
    return render(request, "authentication/signup.html")


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home_page')  # Redirect to home_page on successful login
        else:
            messages.error(request, 'bad credentials')
            return redirect('home')  # Redirect to home if login fails

    return render(request, "authentication/signin.html")


def signout(request):
    logout(request)
    messages.success(request,'Logged Out Succefuly')
    return redirect('home')

def platformes (request):
    return render(request,"authentication/platformes.html")

def course (request):
    return render(request,"authentication/course.html")


def home_page(request):
    category = 'age'
    statistic = 'max'
    plot_file = f'plotly_plots/{category}_{statistic}.html'

    plot_data = None
    for static_dir in settings.STATICFILES_DIRS:
        file_path = os.path.join(static_dir, plot_file)
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                plot_data = file.read()
            break

    if plot_data is None:
        plot_data = f"File '{plot_file}' not found"

    map_names = [
        "No education", "Higher education", "Rural", "Urban", "15-24", 
        "25-34", "35-49", "Max", "No education Max", "Higher education Max"
    ]
    map_files = [f"map_{name.replace(' ', '_').lower()}.html" for name in map_names]
    map_paths = [os.path.join(settings.STATIC_ROOT, 'plotly_plots', file) for file in map_files]

    
    user = request.user
    if user.is_authenticated:
        username = user.username
        title = user.first_name
        genre = user.last_name
        
        # Now you can use title and genre variables in this function
        recommendations = get_recommendations(title, genre, model)
        
            # Separate recommendations into variables        
        Autor0 = recommendations[0]['Book-Author']
        Autor1 = recommendations[1]['Book-Author']
        Autor2 = recommendations[2]['Book-Author']
        Autor3 = recommendations[3]['Book-Author']
        Autor4 = recommendations[4]['Book-Author']
        Autor5 = recommendations[5]['Book-Author']
        Autor6 = recommendations[6]['Book-Author']
        Autor7 = recommendations[7]['Book-Author']
        Autor8 = recommendations[8]['Book-Author']
        Autor9 = recommendations[9]['Book-Author']

        tit0 = recommendations[0]['Book-Title']
        tit1 = recommendations[1]['Book-Title']
        tit2 = recommendations[2]['Book-Title']
        tit3 = recommendations[3]['Book-Title']
        tit4 = recommendations[4]['Book-Title']
        tit5 = recommendations[5]['Book-Title']
        tit6 = recommendations[6]['Book-Title']
        tit7 = recommendations[7]['Book-Title']
        tit8 = recommendations[8]['Book-Title']
        tit9 = recommendations[9]['Book-Title']

        lien0 = recommendations[0]['Image-URL-M']
        lien1 = recommendations[1]['Image-URL-M']
        lien2 = recommendations[2]['Image-URL-M']
        lien3 = recommendations[3]['Image-URL-M']
        lien4 = recommendations[4]['Image-URL-M']
        lien5 = recommendations[5]['Image-URL-M']
        lien6 = recommendations[6]['Image-URL-M']
        lien7 = recommendations[7]['Image-URL-M']
        lien8 = recommendations[8]['Image-URL-M']
        lien9 = recommendations[9]['Image-URL-M']

        rat0 = recommendations[0]['Book-Rating']
        rat1 = recommendations[1]['Book-Rating']
        rat2 = recommendations[2]['Book-Rating']
        rat3 = recommendations[3]['Book-Rating']
        rat4 = recommendations[4]['Book-Rating']
        rat5 = recommendations[5]['Book-Rating']
        rat6 = recommendations[6]['Book-Rating']
        rat7 = recommendations[7]['Book-Rating']
        rat8 = recommendations[8]['Book-Rating']
        rat9 = recommendations[9]['Book-Rating']
        
        context = {
        'plot_data': plot_data,
        'category': category,
        'statistic': statistic,
        'map_names': map_names,
        'map_paths': map_paths,
        'tit0': tit0, 'tit1': tit1, 'tit2': tit2, 'tit3': tit3, 'tit4': tit4, 'tit5': tit5, 'tit6': tit6, 'tit7': tit7, 'tit8': tit8, 'tit9': tit9,
        'lien0': lien0, 'lien1': lien1, 'lien2': lien2, 'lien3': lien3, 'lien4': lien4, 'lien5': lien5, 'lien6': lien6, 'lien7': lien7, 'lien8': lien8, 'lien9': lien9,
        'Autor0': Autor0, 'Autor1': Autor1, 'Autor2': Autor2, 'Autor3': Autor3, 'Autor4': Autor4, 'Autor5': Autor5, 'Autor6': Autor6, 'Autor7': Autor7, 'Autor8': Autor8, 'Autor9': Autor9,
        'rat0': rat0, 'rat1': rat1, 'rat2': rat2, 'rat3': rat3, 'rat4': rat4, 'rat5': rat5, 'rat6': rat6, 'rat7': rat7, 'rat8': rat8, 'rat9': rat9,
        'username': username
        }

        return render(request, 'authentication/home_page.html',context)
    else:
        return redirect('signin')  # For example, redirect to the signin page