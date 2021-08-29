from django.shortcuts import render
from django.http import JsonResponse
from firstApp.models import Employee
# Create your views here.

def employeeView(request):
    """
    emp = {
    'id':12345,
    'name':'Dadasaheb Sawant',
    'sal':90000
    }
    """
    data = Employee.objects.all()
    print(data,type(data))
    response = {'employees':list(data.values('name','sal'))}
    print(response,type(response))
    return JsonResponse(response)#python object(dictonary) to json
