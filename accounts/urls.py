from crm.settings import TEMPLATES
from django.contrib import auth
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from django.urls import path
from django.contrib.auth import views as auth_views

from .import views


urlpatterns = [
    path('',views.home,name='home'),
    # user authentication
    path('register/',views.registerpage,name='register'),
    path('login/',views.loginpage,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('user-page/',views.userPage,name='user-page'),
    path('account/',views.accountSettings,name='account'),
    # navabar urls 
    path('products/',views.products,name='products'),
    path('customers/<str:pk>/',views.customers,name='customers'),
    # orders urls
    path('create_order/<str:pk>/',views.createOrder,name='create_order'),
    path('update_order/<str:pk>/',views.UpdateOrder,name='update_order'),
    path('update_order/<str:pk>/',views.UpdateOrder,name='update_order'),
    path('delete_order/<str:pk>/',views.deleteOrder,name='delete_order'),
    # real change the eamil password for the app

    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'),name = 'reset_password'),

    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_sent.html'),name = 'password_reset_done'),

    path('reset/<uid64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_form.html'),name= 'password_reset_confirm'),

    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_done.html'),name= 'password_reset_complete'),

]
