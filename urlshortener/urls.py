from django.urls import path
from .views import home_view, register_request,login_request, logout_request, password_reset_request

app_name = "shortener"

urlpatterns = [
    # Home view
    path('', register_request, name='register'),
    path('home_view', home_view, name='home'),
    #path('<str:shortened_part>', redirect_url_view, name='redirect'),
    path("login",login_request, name="login"),
    path("logout",logout_request, name= "logout"),
    path("password_reset",password_reset_request, name="password_reset")
]
