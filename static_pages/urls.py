#i created
from django.urls import path
from .views import home_view
app_name='static_pages'

urlpatterns = [
    path('', home_view, name='home'),# work for localhost:8000
    #path('home', home_view, name='home'), work for local host:8000/home
]
