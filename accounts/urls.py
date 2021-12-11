from django.urls import path

app_name='accounts'

from .views import(
    user_login_view,
    user_create_view,
    user_logout_view,
    user_profile_view
)


urlpatterns = [
    path('create/',user_create_view,name='create'),
    path('login/',user_login_view,name='login'),
    path('logout/',user_logout_view,name='logout'),
    path('profile/<str:username>/',user_profile_view,name='profile')
]
