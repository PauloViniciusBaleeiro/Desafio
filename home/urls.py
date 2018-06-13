from django.urls import path
from .views import logout_sys, home


urlpatterns = [
    path('', home, name='home'),
    path('logout/', logout_sys, name='logout_sys'),

]
