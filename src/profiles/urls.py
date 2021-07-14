from django.urls import path
from django.urls.resolvers import URLPattern
from .views import my_profile_view

app_name = 'profiles'

urlpatterns = [
    path('', my_profile_view, name='my')
]