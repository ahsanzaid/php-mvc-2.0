import os.path

def Automate(file,data):
    f = open(file,'a')
    f.write(data)
    #if os.stat(file).st_size == 0:
        
def RM():
    #M
    global View2
    View2 = View2.replace("METHOD",method)
    #RMV
    global proute
    global Route
    global pcontroller
    Automate(proute,Route)
    f = open(pcontroller,"r")
    data = f.read()
    flag = data.find("{")
    temp = data[:flag+1]+View2+data[flag+1:]
    f.close()
    f = open(pcontroller,"w")
    f.write(temp)
    f.close()


# In[63]:


def RMV():
    view = input("view:")
    pview='app\\views\\'+view+'.view.php'
    #M
    global View
    View = View.replace("METHOD",method)
    View = View.replace("VIEW",view)
    #V
    global Layout
    Layout = Layout.replace("METHOD",method)
    Layout = Layout.replace("URL",url)
    Layout = Layout.replace("CONTROLLER",controller)
    Layout = Layout.replace("VIEW",view)
    Layout = Layout.replace("REQUEST",request)
    #RMV
    Automate(proute,Route)
    f = open(pcontroller,"r")
    data = f.read()
    flag = data.find("{")
    temp = data[:flag+1]+View+data[flag+1:]
    f.close()
    f = open(pcontroller,"w")
    f.write(temp)
    f.close()
    Automate(pview,Layout)
    


# In[64]:


def RCM():
    #M
    global View2
    View2 = View2.replace("METHOD",method)
    #C
    global Controller
    Controller = Controller.replace("CONTROLLERMETHOD",View2)
    Controller = Controller.replace("CONTROLLER",controller)
    #RCM
    Automate(proute,Route)
    Automate(pcontroller,Controller)


# In[65]:


def RCMV():
    view = input("view:")
    pview='app\\views\\'+view+'.view.php'
    global View
    View = View.replace("METHOD",method)
    View = View.replace("VIEW",view)
    #C
    global Controller
    Controller = Controller.replace("CONTROLLERMETHOD",View)
    Controller = Controller.replace("CONTROLLER",controller)
   
    global Layout
    Layout = Layout.replace("METHOD",method)
    Layout = Layout.replace("URL",url)
    Layout = Layout.replace("CONTROLLER",controller)
    Layout = Layout.replace("VIEW",view)
    Layout = Layout.replace("REQUEST",request)
    #RCMV
    Automate(proute,Route)
    Automate(pcontroller,Controller)
    Automate(pview,Layout)
    

while(True):
    Route = """
$router->REQUEST('URL','CONTROLLERController@METHOD');

"""
    View = """
 public function METHOD(){
        return view('VIEW');
    }
"""
    Layout = """
<!-- 
  controller : CONTROLLERController
  method : METHOD
  uri : URL
  view : VIEW
  request : REQUEST
  
 -->
<?php require 'partials/header.php'; ?>
<h1>This is system generated Text via MVC 2.0 Shell </h1>
<?php require_once 'partials/footer.php' ;?>

"""
    Controller="""<?php
namespace App\Controllers;
use App\Core\App;
class CONTROLLERController{
        CONTROLLERMETHOD
}
"""
    View2 = """
 public function METHOD(){
    }
"""
    num = input(
    """
    1.NEW(route,controller,method,view)
    2.NEW(route,controller,method)
    3.NEW(route,method,view)
    4.NEW (route,method)""")
    url = input("uri e.g application/viewcustomers :")
    controller = input("controller:")
    request = input("request e.g get or post :")
    method = input("method  inside controller : ")
    Route = Route.replace("REQUEST",request)
    Route = Route.replace("URL",url)
    Route = Route.replace("CONTROLLER",controller)
    Route = Route.replace("METHOD",method)
    pcontroller='app\\controllers\\'+controller+'Controller.php'
    proute = 'routes.php'
    if(num == '1'):
        RCMV()
    if(num == '2'):
        RCM()
    if(num == '3'):
        RMV()
    if(num == '4'):
        RM()
