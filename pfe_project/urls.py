from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home, name="home"),
    path('signup', views.signup,name="signup"),
    path('signin', views.signin,name="signin"),
    path('signout', views.signout,name="signout"),
    path('platformes', views.platformes, name="platformes"),
    path('home_page', views.home_page, name="home_page"),
    path('admin/', admin.site.urls, name='admin'),
    path('recommend_book/', views.recommend_book, name='recommend_book'),
    path('course', views.course, name="course"),
]
 
# Add static files serving only during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

