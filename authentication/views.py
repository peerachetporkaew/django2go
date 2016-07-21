# -*- coding: utf-8 -*-
G_PATH = "/".join(__file__.split("/")[:-1]) + "/"

if __name__ == "__main__":
        print G_PATH
        exit()

from django.http import HttpResponse
from django.template import Template,Context
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render_to_response
import json,settings
from ajax_response import *

def index(request):
    #t1 = Template(open(G_PATH + "html/main_form.html").read())
    #content = t1.render(Context())
    #t2 = Template(default_theme())
    #return HttpResponse(t2.render(Context({"content" : content})))
    
    return render_to_response('authentication/login_main.html')

def access_denied(request):
    return render_to_response('authentication/access_denied.html')
    
def access_denied2(request):
    return render_to_response('authentication/access_denied2.html')

def login_request(request):
    try:
        usernameStr = request.POST["username"]
        passwordStr = request.POST["password"]
        if request.POST.has_key("username") and request.POST.has_key("password"):
            user = authenticate(username=usernameStr, password=passwordStr)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return response_success("Success")
                else:
                    return response_success("This username is not activated.")
            else:
                return response_success("Invalid Username and Password.")
        else:
            return response_success("Command not found.")
    except:
        return response_error()

def logout_request(request):
    logout(request)
    return HttpResponse("You have successfully logged out.")

if __name__ == "__main__":
    pass