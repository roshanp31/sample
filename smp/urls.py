
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.homefun,name="homepage"),
    path('help/',views.helpfun,name="helppage"),
    
]
