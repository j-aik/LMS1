from django.shortcuts import render
# Create your views here.
from django.shortcuts import render,redirect
from django.shortcuts import render,redirect, get_object_or_404
from LMSapp.models import CustomUser,ClassST,Parent,Staff,Student,Subject,Assigned
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from LMSapp.forms import UserEditForm,ParentEditForm,StaffEditForm,StudentEditForm
from django.http import JsonResponse
import re
# Create your views here.

def librarey(request):
    return render(request,'library.html')