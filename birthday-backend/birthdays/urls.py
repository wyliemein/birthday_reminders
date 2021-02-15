from django.urls import path, include
from django.conf.urls import url, include
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns
from birthdays import views

urlpatterns = [
    path('contacts/', views.ContactList.as_view()),
    path('contacts/<int:pk>/', views.ContactDetail.as_view()),
    path('register/', views.CreateUserView.as_view(), name="register"),
    path('api-token-auth/', views.CustomAuthToken.as_view(), name="api-token-auth"),
]