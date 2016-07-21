# -*- coding:utf-8 -*-
# Create your views here.

from django.http import HttpResponse
from django.template import Template,Context,loader,RequestContext
from django.shortcuts import render_to_response
import os,json
from ajax_response import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

def index(request):
    return HttpResponse("HELLO WORLD From Search")