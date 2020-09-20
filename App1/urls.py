from django.urls import path
from App1.views import starter, sl, current_datetime

urlpatterns = [
    path('start_page', starter),
    path('second', current_datetime),
    path('thrd', sl)
]
