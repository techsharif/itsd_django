from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View


class HomeView(View):

    def get(self,request):
        return render(request,'index.html',{'name':'Rofi','Dept':'CSE'})