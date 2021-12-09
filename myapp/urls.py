from django.urls import path, include
from myapp import views

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
    path('register/', views.user_register, name='register')
 ]
