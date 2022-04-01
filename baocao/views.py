from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'baocao/index.html')

def baoCaoMon(request):
    return HttpResponse("Day la trang bao cao mon!")

def taoBaoCaoMon(request):
    return render(request, 'baocao/taobaocaomon.html')

def baoCaoHocKy(request):
    return HttpResponse("Day la trang bao cao hoc ky!")

def taoBaoCaoHocKy(request):
    return render(request, 'baocao/taobaocaohocky.html')
