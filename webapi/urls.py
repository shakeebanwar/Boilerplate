from django.urls import path,include
from webapi.views import *


urlpatterns = [

#web urls  home
path('registration',registration.as_view()),

]
