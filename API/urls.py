from django.contrib import admin
from django.urls import path, include, re_path
from men.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/men/', MenAPIList.as_view()),
    path('api/v1/men/<int:pk>', MenAPIUpdate.as_view()),
    path('api/v1/mendelete/<int:pk>', MenAPIDestroy.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/v1/user/', include('men.user.urls'))
]
