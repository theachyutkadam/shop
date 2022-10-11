from django.shortcuts import render, redirect
from django.http import HttpResponse
from customers.models import Customer
from customers.forms import CustomerCreate

# Create your views here.
def welcome(request):
  return render(request, 'welcome.html')

def index(request):
  shelf = Customer.objects.all()
  return render(request, 'customers/index.html', {'shelf': shelf})

def new(request):
  return render(request, 'customers/form.html')

def create(request):
  if request.method == "POST":
    # first_name = request.POST.get('first_name'),
    # last_name = request.POST.get('first_name'),
    # email = request.POST.get('email'),
    # contact = request.POST.get('contact'),
    # desc = request.POST.get('desc'),

    contact = Customer(
      first_name = request.POST.get('first_name'),
      last_name = request.POST.get('first_name'),
      email = request.POST.get('email'),
      contact = request.POST.get('contact'),
      desc = request.POST.get('desc'),
    )
    contact.save()
    # messages.success(request, 'Customer create Successfully!')

  return render(request, 'welcome.html')
