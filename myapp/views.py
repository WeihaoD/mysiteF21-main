# Create your views here.
# Import necessary classes
import datetime

from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .forms import OrderForm, InterestForm, RegisterForm, UploadPhoto
from .models import Category, Product, Client, Order
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test


# Create your views here.
def index(request):
    cat_list = Category.objects.all().order_by('id')[:10]
    msg = ''
    last_login = ''
    if 'last_login' not in request.session:
        msg = 'Your last login was more than one hour ago'
    else:
        last_login = 'Last login time is ' + request.session.get('last_login')
    return render(request, 'myapp/index.html', {'cat_list': cat_list,
                                                'msg': msg,
                                                'last_login': last_login})


def about(request):
    about_visits = request.session.get('about_visits', 0)
    request.session['about_visits'] = about_visits + 1
    request.session.set_expiry(300)
    return render(request, 'myapp/about.html', {'about_visits': about_visits})


def detail(request, cat_no):
    # category = Category.objects.get(id=cat_no)
    category = get_object_or_404(Category, id=cat_no)
    warehouse = category.warehouse
    product_list = Product.objects.filter(category=cat_no)

    return render(request, 'myapp/detail.html',
                  {'category': category,
                   'warehouse': warehouse,
                   'product_list': product_list})


def products(request):
    prodlist = Product.objects.all().order_by('id')[:50]
    return render(request, 'myapp/products.html', {'prodlist': prodlist})


def place_order(request):
    msg = ''
    prodlist = Product.objects.all()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if order.num_units <= order.product.stock:
                order.product.stock = order.product.stock - order.num_units
                if order.product.stock == 0:
                    order.product.available = False
                order.product.save()
                order.save()
                msg = 'Your order has been placed successfully.'
            else:
                msg = 'We do not have sufficient stock to fill your order.'
            return render(request, 'myapp/order_response.html', {'msg': msg})
    else:
        form = OrderForm()
    return render(request, 'myapp/placeorder.html', {'form': form, 'msg': msg, 'prodlist': prodlist})


def productdetail(request, prod_id):
    # prod = Product.objects.get(id=prod_id)
    prod = get_object_or_404(Product, pk=prod_id)
    prodname = prod.name
    prodprice = prod.price
    prodinterested = prod.interested
    prodavailable = prod.available

    if request.method == 'POST':
        form = InterestForm(request.POST)
        print('post')
        if form.is_valid():
            print('valid')
            interested = form.cleaned_data['interested']
            # https://docs.djangoproject.com/en/3.2/ref/forms/api/
            if interested == 1:
                prod.interested += 1
                prod.save(update_fields=['interested'])
                return render(request, 'myapp/index.html')
            else:
                return render(request, 'myapp/productsdetail.html')
    else:
        form = InterestForm()
        print('not post')
    return render(request, 'myapp/productsdetail.html', {'form': form,
                                                         'prod': prod,
                                                         'prodname': prodname,
                                                         'prodprice': prodprice,
                                                         'prodinterested': prodinterested,
                                                         'prodavailable': prodavailable})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                last_login = datetime.datetime.now().strftime('%c')
                request.session['last_login'] = str(last_login)
                request.session.set_expiry(3600)
                return HttpResponseRedirect(reverse('myapp:myorders'))
            else:
                return HttpResponse('Your account is disabled.')
        else:
            return HttpResponse('Invalid login details.')
    else:
        return render(request, 'myapp/login.html')


def user_register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("myapp:index")
    else:
        form = RegisterForm()

    return render(response, 'myapp/register.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('myapp:index'))


@login_required(login_url='/myapp/login/')
def myorders(request):
    username = request.user.username

    if Client.objects.get(username__contains=username):
        try:
            order_product = Order.objects.filter(client__first_name__contains=username)
        except:
            return HttpResponse('You did not order anything')
    else:
        return HttpResponse('You are not a registered client!')
    return render(request, 'myapp/myorders.html', {'username': username,
                                                   'order_product': order_product})



@login_required(login_url='/myapp/login/')
def upload_photo(request):
    username = request.user.username
    instance = get_object_or_404(Client, username=username)
    if request.method == 'POST':
        form = UploadPhoto(request.POST, request.FILES,instance=instance)

        if form.is_valid():
            instance = form.save()
            instance.save()
            return redirect('myapp:index')
    else:
        form = UploadPhoto()
    return render(request, 'myapp/upload_photo.html', {'form': form})


def display_profile(request):
    if request.method == 'GET':
        # getting all the objects of hotel.
        username = request.user.username
        print(username)
        instance = get_object_or_404(Client, username=username)
        return render(request, 'myapp/index.html',{'profile_images': instance})
