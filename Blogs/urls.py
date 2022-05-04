from django.urls import path
from . import views



urlpatterns = [
    path('<str:website_name>/likes', views.likes),
    path('<str:website_name>/awards',views.awards),
    path('<str:website_name>/created',views.created),
    path('<str:website_name>/count',views.count_keys)
]