# -*- coding:utf-8 -*-
# Create your views here.

from django.http import HttpResponse
from django.template import Template,Context,loader,RequestContext
from django.shortcuts import render_to_response
import os
from ajax_response import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required


#from django.views.decorators.csrf import csrf_exempt
import cgi

def read_dir(path,id="browser",level=0):
    if level==0:
        output = """
        <ul id="browser" class="filetree">
            <li><span class="folder">Project Files</span>
            <ul>
        """
    else:
        output = """
        <ul>
        """
    list_dir = os.listdir(path)
    count = 0
    temp = ""
    list_dir.sort()
    for i in list_dir:
        count = 1
        if i != "django":
            if os.path.isdir(path+"/"+i):
                output += """
          <li><span class="folder">%s</span>
          """%(i)
                output += read_dir(path+"/"+i,"",1)
                output += "</li>"
            else:
                if i.split(".")[-1].strip() not in ["pyc","py~"]:
                    temp += """
              <li><span class="file" onclick="load_file('%s');">%s</span></li>
          """%(path+"/"+i,i)
    output += temp
    if count == 0:
        return ""
    if level == 0:
        output += "</ul></li></ul>"
    else:
        output += "</ul>"
    return output

def read_only_dir(path,id="browser1",level=0):
    if level==0:
        output = """
        <ul id="browser1" class="filetree">
            <li><span class="folder" onclick="select_dir('%s');">Project Files</span>
            <ul>
        """%(path+"/")
    else:
        output = """
        <ul>
        """
    list_dir = os.listdir(path)
    count = 0
    for i in list_dir:
        if os.path.isdir(path+"/"+i):
            count = 1
            output += """
                <li><span class="folder" onclick="select_dir('%s');">%s</span>
            """%((path+"/"+i).replace("//","/"),i)
            if level==0:
                output += read_only_dir(path+i,"",1)
            else:
                output += read_only_dir(path+"/"+i,"",1)
            output += "</li>"
        else:
            pass
    if count == 0:
        return ""
    if level == 0:
        output += "</ul></li></ul>"
    else:
        output += "</ul>"
    return output


def read_only_dir2(path,id="browser2",level=0):
    if level==0:
        output = """
        <ul id="browser2" class="filetree">
            <li><span class="folder" onclick="select_dir2('%s');">Project Files</span>
            <ul>
        """%(path+"/")
    else:
        output = """
        <ul>
        """
    list_dir = os.listdir(path)
    count = 0
    for i in list_dir:
        if os.path.isdir(path+"/"+i):
            count = 1
            output += """
                <li><span class="folder" onclick="select_dir2('%s');">%s</span>
            """%((path+"/"+i).replace("//","/"),i)
            if level==0:
                output += read_only_dir2(path+i,"",1)
            else:
                output += read_only_dir2(path+"/"+i,"",1)
            output += "</li>"
        else:
            pass
    if count == 0:
        return ""
    if level == 0:
        output += "</ul></li></ul>"
    else:
        output += "</ul>"
    return output

@permission_required('webbuilder.can_view',login_url='/app/authentication/access_denied' )
def page(request):
    dir = read_dir(".")
    dir2 = read_only_dir("./","bb",0)
    dir3 = read_only_dir2("./","bb",0)
    dir4 = read_only_dir2("./","bb",0).replace("select_dir2","select_dir3").replace("browser2","browser3")
    return render_to_response("./webbuilder/page.html",Context({"directory_tree" : dir, "folder_tree" : dir2
    ,"folder_tree2" : dir3,"folder_tree3" : dir4}))
    
#@csrf_exempt
@permission_required('webbuilder.can_view',login_url='/app/authentication/access_denied' )
def new_folder(request):
    os.makedirs(request.POST["folder"],0777)
    return response_success("Completed !")

#@csrf_exempt
@permission_required('webbuilder.can_view',login_url='/app/authentication/access_denied' )
def new_file(request):
    try:
        file1 = request.POST["filename"]
        fp = open(file1,"w")
        fp.writelines(" ")
        fp.close()
    except:
        respose_error()
    return response_success("hello")
    
@permission_required('webbuilder.can_view',login_url='/app/authentication/access_denied' )
def save_file3(request):
    try:
        #return response_success(request.POST["file"])
        if request.POST.has_key("test5"):
            import cgi
            filename = request.POST["txtFilename1"]
            text = request.POST["test5"].encode("utf-8")
      
            filename = filename.split(":")[1].replace("]","").strip()
            fp = open(filename,"w")
            fp.writelines(text.strip())
            fp.close()
      
            return HttpResponse("""
        <script>
          parent.save_completed();
        </script>
      """)
        else:
            return HttpResponse("Hello")
    except Exception:
        return response_error()
        
@permission_required('webbuilder.can_view',login_url='/app/authentication/access_denied' )
def load(request):
    try:
        if request.GET.has_key("path"):
            filename = request.GET["path"]
        else:
            filename = "a.py"
        fp = open(filename,"r").read()
        fp = cgi.escape(fp)
    except Exception:
        return reponse_error()
    return HttpResponse("""    
    <textarea id="example_4" style="margin:0px; height: 100%; width: 100%;" name="test_4">""" + fp + """</textarea>
    
    """)

#@csrf_exempt
@permission_required('webbuilder.can_view',login_url='/app/authentication/access_denied' )
def run(request):
    try:
        code = request.POST["code"].encode("utf-8")
        fp = open("code.py","w")
        fp.writelines(code)
        fp.close()
        os.system("python code.py > code.out")
        output = open("code.out","r").read()
        return response_success(output.decode("utf-8"))
    except Exception:
        return response_error()

#@csrf_exempt
@permission_required('webbuilder.can_view',login_url='/app/authentication/access_denied' )
def save_file(request):
    try:
        #return response_success(request.POST["file"])
        filename = request.POST["file"]
        filename = filename.split(":")[1].replace("]","").strip()
        fp = open(filename,"w")
        fp.writelines(request.POST["text"].strip())
        fp.close()
        return response_success("Success")
    except Exception:
        return response_error()
        
#@csrf_exempt
@permission_required('webbuilder.can_view',login_url='/app/authentication/access_denied' )
def upload_file(request):
    try:
        file = request.FILES["file"]
        destination = request.POST["destination"]
        output = destination + "/" + file.name
        
        ftype = file.name.split(".")[-1]

        
        fp = open(destination + "/" + file.name,"wb")
        for chunk in file.chunks():
            fp.write(chunk)
        fp.close()
        
        
        if ftype == "zip":
            import zipfile
            k = zipfile.ZipFile(destination + "/" + file.name)
            k.extractall(destination + "/")
            os.remove(destination + "/" + file.name)
            
        output = """
        <script>
            parent.upload_completed();
        </script>
        """
    except:
        return response_error()
    return HttpResponse(output)
    
#@csrf_exempt
@permission_required('webbuilder.can_view',login_url='/app/authentication/access_denied' )
def del_file(request):
    try:
        os.remove(request.POST["file"].strip())
        
    except:
        return response_error()
    return response_success("Success !")

@permission_required('webbuilder.can_view',login_url='/app/authentication/access_denied' )
def index(request):
    output = """
    <html>
    <head>
    <script src='/site_media/js/edit_area/edit_area_full.js' ></script>
    <script language="Javascript" type="text/javascript">
        editAreaLoader.init({
            id: "example_4" // id of the textarea to transform      
            ,start_highlight: true  // if start with highlight
            ,font_size: "10"    
            ,allow_resize: "no"
            ,allow_toggle: false
            ,language: "en"
            ,syntax: "python"
            ,load_callback: "my_load"
            ,save_callback: "my_save"
            ,replace_tab_by_spaces: 4
            ,min_height: 500
        });
    </script>
    
    </head>
    
    
    
    <body>
<textarea id="example_4" style="height: 50px; width: 100%;" name="test_4">
import Blender
 
class Python:
    # Instancie un objet
    def __new__(cls):
        pass
    
    def __init__(self):
        self.items = [1, 2, 3]
    
    # Destructeur
    def __del__(self):
        print "Pourquoi tant de haine ?"
    

    def __len__(self):
        return len(self.items)
    

    def __getitem__(self, key):
        return self.items[key]


    def __contains__(self, value):

        return (value in self.items)

    def __iter__(self):
        for x in self.items:
            yield x
</textarea>
    </body>
    </html>
    """

    return HttpResponse(output)
