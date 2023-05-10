from django.http import HttpResponse
from django.shortcuts import render

#
# Create your views here.
# def sample(request):
#     return HttpResponse("Hey django")



#
# from django.http import HttpResponse
# from django.shortcuts import render
#
#



#
# from django.http import HttpResponse
# from django.shortcuts import render
#
#
#
# def home(request):
#      return HttpResponse("welcome to my home page")
#
#
# def about(request):
#      return render(request,"home.html")
#
# def contact(request):
#      return HttpResponse("this is contact page")
#
# def detail(request):
#      return render(request,"link.html")
#
# def thanks(request):
#      return HttpResponse("this is thanks page")









# from django.http import HttpResponse
# from django.shortcuts import render
#
#
# def home(request):
#     name="home"
#     return render(request,"home.html",{'obj_name':name})
#



# from django.shortcuts import render
#
#
# def home(request):
#
#     return render(request,"home.html")
#
# def calculation(request):
#     x=int(request.GET['number1'])
#     y = int(request.GET['number2'])
#     add_res=x+y
#     sub_res=x-y
#     mult_res=x*y
#     div_res=x/y
#
#     response = {'result_add':add_res ,'result_sub':sub_res ,'result_mult':mult_res ,'result_div':div_res}
#     return render(request,"result.html" , response)










from .models import Destination
from .models import Person
from django.shortcuts import render


def home(request):
    obj=Destination.objects.all()
    obj1=Person.objects.all()
    return render(request,"index.html",{'result':obj,'res':obj1})