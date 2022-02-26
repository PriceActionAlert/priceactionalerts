
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dailycandle.urls', namespace='dailycandle')),
    path('account/', include('users.urls', namespace='users')),
    path('', include('django.contrib.auth.urls')),
]
