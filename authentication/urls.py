
from django.urls import path,include
# import djoser.urls.jwt
urlpatterns = [
    path('',include('djoser.urls')),
    path('',include('djoser.urls.jwt')),
]

"""
You can check the djoser documentation 
at the time of building this app these are the available endpoints for the djoser.urls
send this as the body for the /users/ URL to create new User
{
    "username": "your_username",
    "password": "your_password"
}

/users/
/users/me/
/users/confirm/
/users/resend_activation/
/users/set_password/
/users/reset_password/
/users/reset_password_confirm/
/users/set_username/
/users/reset_username/
/users/reset_username_confirm/
/token/login/ (Token Based Authentication)
/token/logout/ (Token Based Authentication)
/jwt/create/ (JSON Web Token Authentication)
/jwt/refresh/ (JSON Web Token Authentication)
/jwt/verify/ (JSON Web Token Authentication)
"""