from django.urls import path

from . import views

app_name = ("calen")

urlpatterns = [
    path("", views.index, name="index"),
    path("kolo", views.kolo, name="kolo"),
    path("udalosti", views.udalosti, name="udalosti"),
    path("detail/<int:udalost_id>", views.detail, name="detail"),
    path("register", views.RegisterView.as_view(), name="register"),
    path("logout", views.log_out, name="logout"),
    path("login", views.log_in, name="login"),
]
