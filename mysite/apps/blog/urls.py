from django.urls import path
from . import views

app_name='templates'
urlpatterns=[
    path('r^$', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/', views.post_detail, name='post_detail'),
]
