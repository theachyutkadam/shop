from django.shortcuts import render, redirect
from django.http import HttpResponse
from customers.models import Customer
from customers.forms import CustomerCreate
from django.contrib import messages
# Create your views here.
def welcome(request):
  return render(request, 'welcome.html')

def index(request):
  shelf = Customer.objects.all()
  return render(request, 'customers/index.html', {'shelf': shelf})

def new(request):
  return render(request, 'customers/form.html')

def show(request, id):
  customer_id = int(id)
  customer = Customer.objects.get(id= customer_id)
  return render(request, 'customers/show.html', {'customer': customer})

def create(request):
  if request.method == "POST":
    contact = Customer(
      first_name = request.POST.get('first_name'),
      last_name = request.POST.get('first_name'),
      email = request.POST.get('email'),
      contact = request.POST.get('contact'),
      desc = request.POST.get('desc'),
    )
    contact.save()
    messages.success(request, 'Customer created successfully.')
    # messages.success(request, 'Customer create Successfully!')
  return render(request, 'welcome.html')

def edit(request, id):
  customer_id = int(id)
  customer = Customer.objects.get(id= customer_id)
  return render(request, 'customers/form.html', {'shelf': customer})

def update(request):
  # customer_id = int(id)
  # customer = Customer.objects.get(id= customer_id)
  return render(request, 'welcome.html')
  # try:
  #   customer_id = Customer.objects.get(id = customer_id)
  # except Customer.DoesNotExist:
  #   return redirect('index')
  # customer_form = CustomerCreate(request.POST or None, instance = customer_id)
  # if customer_form.is_valid():
  #   customer_form.save()
  #   return redirect('index')
  # return render(request, 'customer/form.html', {'form':customer_form})


def delete(request, id):
  customer_id = int(id)
  try:
    customer = Customer.objects.get(id= customer_id)
  except Customer.DoesNotExist:
    return redirect(request, 'index.html')

  customer.delete()
  return redirect(request, '/')
