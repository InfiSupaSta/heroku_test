from django.urls import path, include

from new_app.views import *

urlpatterns = [
    path('', hello)
]
#  /hello
