from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from courses.urls import router

urlpatterns = [
    path('user-auth/', obtain_auth_token, name='user_auth'),
    path('api/v2/', include(router.urls)),
    path('api/v1/', include('courses.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls'))
]
