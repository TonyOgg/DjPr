from django.urls import path
from App1.views import starter, sl

urlpatterns = [
    path('start_page', starter),
    path('second', sl)
]
