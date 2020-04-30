from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    # path('admin/', admin.site.urls),
    path('', views.author),
    path('', views.recipe),

    
]   