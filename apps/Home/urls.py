from django.urls import path as p
from . import views as v

app_name="home"

urlpatterns = [
    p('',v.Home.as_view()),
]
