from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'baocao/index.html')

def baoCaoMon(request):
    return render(request, 'baocao/baocaomon.html')

def taoBaoCaoMon(request):
    return render(request, 'baocao/taobaocaomon.html')

def baoCaoHocKy(request):
    return render(request, 'baocao/baocaohocky.html')

def taoBaoCaoHocKy(request):
    return render(request, 'baocao/taobaocaohocky.html')
