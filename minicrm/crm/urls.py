from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('activities/', views.activities, name='activities'),
    path('customers/', views.customers, name="customers"),
    path('activities/<int:pk>', views.ActivityDetailView.as_view(), name='activity-detail'),
    path('register/', views.register, name='register')
]