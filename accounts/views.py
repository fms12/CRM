from accounts.decorators import unauthenticated_user
from django.contrib.auth.models import Group
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from django.contrib.auth import authenticate,login,logout
from django.views.decorators.csrf import csrf_protect

# create your views here
from .filters import OrderFilter
from .models import *
from .forms import CreateUserForm, CustomerForm, OrderForm
from .decorators import admin_only, allowed_users, unauthenticated_user

@unauthenticated_user
def loginpage(request):
    # if request.user.is_authenticated:
    #     return redirect('home')
    # else:
        if request.method == 'POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user = authenticate(request, username = username, password = password)
           
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.info(request,'Username OR Password is incorrect')
        context ={}
        return render(request,'accounts/login.html',context)
@unauthenticated_user
def registerpage(request):
        form = CreateUserForm()
        if request.method == 'POST':
            form  = CreateUserForm (request.POST)
            if form.is_valid():
                user=form.save()
              
                # this give the 
                username = form.cleaned_data.get('username')
                # group = Group.objects.get(name='customer')

                # user.groups.add(group)
                # Customer.objects.create(user=user)

                messages.success(request,'Account was created for ' + username)
                return redirect('login')
        context ={'form': form}
        return render(request,'accounts/register.html',context)

def logoutUser(request):

    logout(request)
    return redirect('login')

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userPage(request):
        orders = request.user.customer.order_set.all()
        total_order = orders.count()
        delivered = orders.filter(status='Delivered').count()
        pending = orders.filter(status='Pending').count()

        print('ORDERS:', orders)
        context = {'orders':orders,'total_order':total_order,'delivered':delivered,'pending':pending}
        return render(request, 'accounts/user.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def accountSettings(request):
	customer = request.user.customer
	form = CustomerForm(instance=customer)

	if request.method == 'POST':
		form = CustomerForm(request.POST, request.FILES,instance=customer)
		if form.is_valid():
			form.save()


	context = {'form':form}
	return render(request, 'accounts/account_settings.html', context)




@login_required(login_url='login')
@admin_only
def home(request):

    customer=Customer.objects.all()
    order = Order.objects.all()
    total_customer = customer.count()
    total_order = order.count()
    delivered = order.filter(status='Delivered').count()
    pending = order.filter(status='Pending').count()


    context = {'order':order,'customer':customer,'total_order':total_order,'delivered':delivered,'pending':pending,'total_customer':total_customer,}
    return render(request,'accounts/dashboard.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def products(request):
    product = Product.objects.all()
    return render(request,'accounts/products.html',{'product':product})

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customers(request, pk):

    customer = Customer.objects.get(id=pk)

    orders = customer.order_set.all()
    order_count = orders.count()
    myFilter = OrderFilter(request.GET, queryset = orders)
    orders=myFilter.qs
    context = {'customer':customer,'orders':orders,'myFilter':myFilter,'order_count':order_count}
    return render(request,'accounts/customers.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createOrder(request, pk):
    OrderFormset = inlineformset_factory(Customer,Order, fields=('product','status'),extra=10)
    customer = Customer.objects.get(id=pk)
    formset = OrderFormset(queryset=Order.objects.none(), instance=customer)
    # form = OrderForm(initial={'customer':customer,})
    # this form save method 
    if request.method == 'POST':
        formset = OrderFormset(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context = {'formset':formset,}
    return render(request,'accounts/order_form.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def UpdateOrder(request,pk):

    order = Order.objects.get(id = pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request,'accounts/order_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteOrder(request,pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')

    context = {'item':order}
    return render(request,'accounts/delete.html',context)

   
