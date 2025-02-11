from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/books/', include('books.urls')),
    path('api/members/', include('members.urls')),
    path('api/circulation/', include('circulation.urls')),
]
