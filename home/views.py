from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# home テンプレート呼び出し
def index(request):
    return render(request,'home.html',{})
