from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path, include, reverse_lazy
from django.views.static import serve

from myapp import views
from django.conf import settings
from django.contrib.auth import views as auth_views

app_name = 'myapp'

urlpatterns = [
    path(r'', views.index, name='index'),
    # What is r in Django?
    # This is a prefix for raw strings (escape sequences are ignored) which is useful for sane regular expressions.
    # Excerpt from the docs: When an r' or R' prefix is present,
    # backslashes are still used to quote the following character,
    # but all backslashes are left in the string.
    path('about/', views.about, name='about'),
    path('<int:cat_no>/', views.detail, name='cat_no'),
    path('products/', views.products, name='products'),
    path('place_order/', views.place_order, name='place_order'),
    path('<int:prod_id>', views.productdetail, name='prod_id'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('myorders/', views.myorders, name='myorders'),
    path('register/', views.user_register, name='register'),
    path('upload_photo/', views.upload_photo, name='upload_photo'),

    path('password_reset/',
         auth_views.PasswordResetView.as_view(template_name='myapp/password_reset.html'),
         name='password_reset'),

    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='myapp/password_reset_sent.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),

    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='myapp/password_reset_done.html'),
         name='password_reset_complete')
]
