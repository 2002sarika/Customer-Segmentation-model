from django.shortcuts import render,redirect 
from .forms import Customerform 
from .models import Customer

# Create your views here.
def index(request):
    if request.method=="POST":
      form=Customerform(request.POST)
      if form.is_valid():
          form.save()
          return redirect('result-predict')
    else:
        form=Customerform()
    context={'form':form}
    return render(request,'result/index.html',context)

def predict(request):
    score=Customer.objects.all()
    context={'score':score}
    return render(request,"result/predict.html",context)