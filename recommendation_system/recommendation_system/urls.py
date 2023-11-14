

from django.contrib import admin
from django.urls import include, path


from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jobs/', include('jobs.urls')),
    path('', include('accounts.urls')),
]
