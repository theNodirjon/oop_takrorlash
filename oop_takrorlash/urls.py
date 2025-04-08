from django.contrib import admin
from django.urls import path, include

import files

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("files.urls")),
]
