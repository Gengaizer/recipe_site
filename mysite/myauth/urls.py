from django.contrib.auth.views import LoginView

from myauth.views import RegisterView, MyLogoutView
from django.urls import path

app_name = 'myauth'

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(
        template_name='myauth/login.html',
        redirect_authenticated_user=True
    ), name='login'),
    path("logout", MyLogoutView.as_view(), name="logout")
]
