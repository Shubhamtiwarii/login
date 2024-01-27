from django.urls import path,include
from login import views
urlpatterns = [
    path('',views.signup,name="signup"),
    path('login/',views.login,name="login"),
]
