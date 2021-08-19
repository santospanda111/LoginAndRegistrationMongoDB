from django.urls import path
from Note import views


urlpatterns = [
    path('note',views.Notes.as_view(),name='notes')
]