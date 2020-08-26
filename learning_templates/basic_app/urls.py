from django.urls import path
from . import views

# TEMPALTE TAGGING - we need to set a global app_name variable with our app's name
app_name = 'basic_app'  # This is the name that should appear in the {% url 'app_name:path_name_kwarg' %} tag in our templates

urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),
]