from django.shortcuts import render, redirect
from order.forms import OrderForm
from order.models import Order

def order(request):
  if request.method == "POST":
    form = OrderForm(request.POST)
    if form.is_valid():
      try:
        form.save()
        return redirect('/show')
      except:
        pass
  else:
    form = OrderForm()
  return render(request,'index.html',{'form':form})
def show(request):
  orders = Order.objects.all()
  return render(request,"show.html",{'orders':orders})

def edit(request, id):
  order = Order.objects.get(id=id)
  return render(request,'edit.html', {'order':order})

def update(request, id):
  order = Order.objects.get(id=id)
  form = OrderForm(request.POST, instance = order)
  if form.is_valid():
    form.save()
    return redirect("/show")
  return render(request, 'edit.html', {'order': order})

def destroy(request, id):
  order = Order.objects.get(id=id)
  order.delete()
  return redirect("/show")
