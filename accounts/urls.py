from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('sign-up', views.sign_up, name='sign_up'),
    path('account/', views.accountSettings, name="account"),

    ]