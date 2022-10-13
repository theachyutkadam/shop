from django.shortcuts import render, redirect
from django.http import HttpResponse
from products.models import Product
# from products.forms import ProductCreate
from django.contrib import messages

# Create your views here.
def welcome(request):
  return render(request, 'welcome.html')

def index(request):
  shelf = Product.objects.all()
  return render(request, 'products/index.html', {'shelf': shelf})

def new(request):
  return render(request, 'products/form.html')

def show(request, id):
  product_id = int(id)
  product = Product.objects.get(id= product_id)
  return render(request, 'products/show.html', {'product': product})

def create(request):
  if request.method == "POST":
    product = Product(
      name = request.POST.get('name'),
      price = request.POST.get('price'),
      is_available = request.POST.get('is_available'),
      expiry_date = request.POST.get('expiry_date'),
      desc = request.POST.get('desc'),
    )
    product.save()
    messages.success(request, 'Product created successfully.')
    # messages.success(request, 'product create Successfully!')
  return render(request, 'welcome.html')

def edit(request, id):
  product_id = int(id)
  product = Product.objects.get(id= product_id)
  return render(request, 'products/form.html', {'shelf': product})

def update(request):
  # product_id = int(id)
  # product = Product.objects.get(id= product_id)
  return render(request, 'welcome.html')
  # try:
  #   product_id = Product.objects.get(id = product_id)
  # except Product.DoesNotExist:
  #   return redirect('index')
  # product_form = ProductCreate(request.POST or None, instance = product_id)
  # if product_form.is_valid():
  #   product_form.save()
  #   return redirect('index')
  # return render(request, 'product/form.html', {'form':product_form})


def delete(request, id):
  product_id = int(id)
  try:
    product = Product.objects.get(id= product_id)
  except Product.DoesNotExist:
    return redirect(request, 'products/index.html')

  product.delete()
  return redirect(request, '/')
