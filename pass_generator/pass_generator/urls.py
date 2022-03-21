from unicodedata import name
from django.urls import path
from generator import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.home),
    path('password', views.password, name="password"),
    path('about', views.about, name="about")
]
