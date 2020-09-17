from django.urls import path
from App1.views import starter

urlpatterns = [
    path('start_page', starter),
]
