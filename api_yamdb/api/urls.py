from django.urls import path

from .views import issue_a_token, signup_to_api

urlpatterns = [
    path('v1/auth/signup/', signup_to_api),
    path('v1/auth/token/', issue_a_token),
]
