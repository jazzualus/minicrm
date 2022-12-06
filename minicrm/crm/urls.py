from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('activities/', views.ActivityListView.as_view(), name='activities'),
    path('customers/', views.CustomerListView.as_view(), name="customers"),
    path('activities/<int:pk>', views.ActivityDetailView.as_view(), name='activity-detail'),
    path('register/', views.register, name='register'),
    #path('new_activity/', views.new_activity, name='new_activity'),
    path('new_activiry/', views.NewActivity.as_view(), name='new_activity'),
    path('new_customer/', views.new_customer, name='new_customer'),
    path('profile/', views.profile, name='profile'),
    #path('profile/', views.profile, name='profile'),
]