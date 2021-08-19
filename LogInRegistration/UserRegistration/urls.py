from django.urls import path
from UserRegistration import views

urlpatterns=[
    path('',views.Index.as_view(),name='home')
]