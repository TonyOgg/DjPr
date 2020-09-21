from django.urls import path
from App1.views import starter, sl, current_datetime, page

urlpatterns = [
    path('start_page', starter),
    path('second', current_datetime),
    path('thrd', sl),
    path('htm', page)
]
