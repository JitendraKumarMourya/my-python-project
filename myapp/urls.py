from . import views
from django.urls import path
urlpatterns = [
    path('welcome/',views.TextFun,name='welcome'),
    path('index',views.IndexFun,name='index'),
    path('login',views.LoginFun,name='login'),
    path('demoimage',views.DemoimageFun,name="demoimage"),
    path('project_demo/',views.ProjectFun,name="project_demo"),
    path('w3school/',views.W3schoolFun,name="w3school"),
    path('grid',views.GridFun,name="grid"),
    path('griddemo',views.GriddemoFun,name="griddemo"),
    path('demo',views.DemoFun,name="demo"),
    path('bootstrap',views.BootstrapFun,name="bootstrap"),
    path('bootgridpro',views.BootgridproFun,name="bootgridpro"),
    path('bootstrapproject',views.BootstrapprojectFun,name="bootstrapproject"),
    # path('facebook/',views.FacebookFun,name="facebook"),
    path('javascript',views.JavacriptsFun,name="javascript"),
    path('studentform/',views.StudentformFun,name="studentform"),
    path('facebookform/',views.FacebookformFun,name="facebookform"),
    path('facebook2/',views.Facebook2Fun,name="facebook2"),
    # path('facebook_home/',views.Facebook_homeFun,name="facebook_home"),
    path('facebook_editp/',views.Facebook_editpFun,name="facebook_editp"),
    path('facebook_changep/',views.Facebook_changepFun,name="facebook_changep"),
    path('login/',views.LoginFun,name="login"),
    path('logout/',views.LogoutFun,name='logout'),
    path('deleteuser/',views.DeleteuserFun,name='deleteuser'),
    path('imgfile/',views.ImgfileFun,name='imgfile'),
    path('ajax/',views.AjaxFun,name='ajax'),
    path('ajax2/',views.Ajax2Fun,name='ajax2'),




    path('loaddata/',views.fnloaddata,name="loaddata"),

# getting data from db in text field
    path('dataupdate/',views.fndataupdate,name='dataupdate'),

# update data fn
    path('updatedata/',views.fnupdatedata,name='updatedata'),

# delete data fn
    path('delete/',views.fndelete,name='delete'),
    

    # API 
    path('api/',views.apiFn, name="api"),

    path('api1/',views.api1, name="api1"),

    path('apidelete/',views.fnapidel,name="apidel"),


    path('dashboard/',views.dashboard, name="dashboard"),



    








    # -------------------------------------------------------------------------------------------------------------------

    path('bloger/',views.blogerFn, name="bloger"),



    
]
