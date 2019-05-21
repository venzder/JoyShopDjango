from django.urls import path
from .views import (
    main, about, contacts, sale)

app_name = 'main'

urlpatterns = [
    path('', main, name='main'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('sale/', sale, name='sale'),
]
