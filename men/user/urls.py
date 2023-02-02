
from django.urls import path, include, re_path

from men.user.views import UserByToken

urlpatterns = [
   path('user/by/token', UserByToken.as_view())
]
