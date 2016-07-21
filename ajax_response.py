import sys,traceback
from django.http import HttpResponse
from django.utils import simplejson

def response_error():
    
    output  = ":: Unexpected Error ::\n"
    output += "Description : " + str(sys.exc_info()[1]) + "\n"
    output += "File    : " + str(traceback.extract_tb(sys.exc_info()[2])[0][0]) + "\n"
    output += "Line no : " + str(traceback.extract_tb(sys.exc_info()[2])[0][1]) + "\n"
    output += "Function: " + str(traceback.extract_tb(sys.exc_info()[2])[0][2]) + "\n"
    output += "Command : " + str(traceback.extract_tb(sys.exc_info()[2])[0][3]) + "\n"
    
    message = {}
    message["status"] = "error"
    message["data"] = output
    
    return HttpResponse(simplejson.dumps(message))

def get_error_message():
    
    output  = ":: Unexpected Error ::\n"
    output += "Description : " + str(sys.exc_info()[1]) + "\n"
    output += "File    : " + str(traceback.extract_tb(sys.exc_info()[2])[0][0]) + "\n"
    output += "Line no : " + str(traceback.extract_tb(sys.exc_info()[2])[0][1]) + "\n"
    output += "Function: " + str(traceback.extract_tb(sys.exc_info()[2])[0][2]) + "\n"
    output += "Command : " + str(traceback.extract_tb(sys.exc_info()[2])[0][3]) + "\n"
    
    message = {}
    message["status"] = "error"
    message["data"] = output
    return output

def response_success(output):
    message = {}
    message["status"] = "success"
    message["data"] = output
    return HttpResponse(simplejson.dumps(message))