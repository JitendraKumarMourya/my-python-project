from django.core import exceptions
from django.http import response
from django.http.response import ResponseHeaders
from django.shortcuts import redirect, render
from django.http import HttpResponse,JsonResponse
from django.contrib import messages
from . models import *
from random import random
from django.core.files.storage import FileSystemStorage

from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
def TextFun(request):
    return HttpResponse('this my views page')
def IndexFun(request):
    return render(request,'index.html')
def LoginFun(request):
    return render(request,'login.html')
def DemoimageFun(request):
    return render(request,'demoimage.html')
def ProjectFun(request):
    return render(request,'project_demo.html')
def W3schoolFun(request):
    return render(request,'w3school.html')
def GridFun(request):
    return render(request,'grid.html')
def GriddemoFun(request):
    return render(request,'griddemo.html')
def DemoFun(request):
    return render(request,'demo.html')
def BootstrapFun(request):
    return render(request,'bootstrap.html')
def BootgridproFun(request):
    return render(request,'bootgridpro.html')
def BootstrapprojectFun(request):
    return render(request,'bootstrapproject.html')
def JavacriptsFun(request):
    return render(request,'javascript.html')
    
    # student form
def StudentformFun(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        age=request.POST['age']
        address=request.POST['address']
        dob=request.POST['dob']
        print(fname,lname,age,address,dob)
        obj=Student_Table(firstname=fname,lastname=lname,age=age,place=address,dob=dob)
        obj.save()
    return render(request,'studentform.html')

    # facebook form
def FacebookformFun(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        mobile=request.POST['mob']
        email=request.POST['eml']
        password=request.POST['pass']
        day=request.POST['d']
        month=request.POST['m']
        year=request.POST['y']
        dob=year+'-'+month+'-'+day
        gender=request.POST['gen']
        print(fname,lname,mobile,email,password,dob,gender)
        obj=facebookform(firstname=fname,lastname=lname,mobile=mobile,email=email,password=password,dob=dob,gender=gender)
        obj.save()
    return render(request,'facebookform.html')

        # facebook2
def Facebook2Fun(request):
    try:
        email=request.POST['eml']
        obj=facebook2.objects.filter(email_mobile=email).exists()
        print(obj)
        
        if obj==False:
            first_name=request.POST['fname']
            last_name=request.POST['lname']
            password=request.POST['pass']
            day=request.POST['d']
            month=request.POST['m']
            year=request.POST['y']
            dob=year+'-'+month+'-'+day
            gen=request.POST['gender']
            print(first_name,last_name,email,password,dob,gen)
            obj=facebook2(firstname=first_name,lastname=last_name,email_mobile=email,password=password,dob=dob,gender=gen)
            obj.save()
            return render(request,"facebook2.html",{"mgs":"user saved successfully..."})
        return render(request,"facebook2.html",{"msg":"user alredy exist"})
    except Exception as e:print(e)       
    return render(request,'facebook2.html')


            # Update PROFILE CODE
def Facebook_editpFun(request):
    user_id=request.session['facebooksession']
    user_data=facebook2.objects.get(id=user_id)
    if request.method=='POST':

        first_name=request.POST['fname']
        last_name=request.POST['lname']
        email_mobile=request.POST['eml']
        day=request.POST['d']
        month=request.POST['m']
        year=request.POST['y']
        dob=year+'-'+month+'-'+day
        # gen=request.POST['gender']
        #// file code //
        file_1=request.POST['fl']
        file_2=str(random())+file_1.name
        print(file_2)
        imgobj=FileSystemStorage()
        imgobj.save(file_2,file_1)
        obj1=facebook2(file=file_2)
        obj1.save()
        print(obj1)
        objshow=facebook2.objects.all()
        
        facebook2.objects.filter(id=user_id).update(firstname=first_name,lastname=last_name,email_mobile=email_mobile,dob=dob,file=file_2)
        print(user_data.firstname,user_data.lastname,user_data.email_mobile,user_data.dob)
        return render(request,'facebook_editp.html',{'showing':objshow})
    return render(request,'facebook_editp.html',{'user':user_data})




    # other editp
        # user_data.firstname=first_name
        # user_data.lastname=last_name
        # user_data.email_mobile=email_mobile
        # user_data.dob=dob
        # user_data.save()

                # CHANAGE PASSWORD CODE
def Facebook_changepFun(request):
    try:
        userid=request.session['facebooksession']
        userobj=facebook2.objects.get(id=userid)
        oldpass=request.POST['oldpass']
        newpass=request.POST['newpass']
        if(userobj.password==oldpass):
            userobj.password=newpass
            userobj.save()
            return render(request,'facebook_changep.html',{'passmsg':'password change successfully !!'})
        return render(request,'facebook_changep.html',{'passmsg':'password change successfully !!'})
    except Exception as e:print(e)
    return render(request,'facebook_changep.html')


            # LOGIN CODE
def LoginFun(request):
    try:
        user=request.POST['email']
        passw=request.POST['password']
        obj=facebook2.objects.get(email_mobile=user,password=passw)
        print(obj)
        # session
        # request.session['facebooksession']=obj.id
        # return render(request,'facebook_home.html',{'user':obj.firstname})
    except Exception as e:print(e)
    return render(request,'facebook2.html',{"msg1":"invalid usernema or password"})

            # LOGOUT CODE
def LogoutFun(request):
    del request.session['facebooksession']
    return render(request,'facebook2.html')

            # DELETE USER CODE
def DeleteuserFun(request):
    u_id=request.session['facebooksession']
    delobj= facebook2.objects.get(id=u_id).delete()
    return render(request,'facebook2.html')


        # image file code
def ImgfileFun(request):
    if(request.method=='POST'):
    
        name1=request.POST['n1']
        file1=request.FILES['f1']
        file2=str(random())+file1.name
        print(file1)
        objimg=FileSystemStorage()
        objimg.save(file2,file1)
        obj=imgfile(name=name1,file=file2)
        obj.save()
    objshow=imgfile.objects.all()
    print(objshow)
    return render(request,'imgfile.html',{'show':objshow}) #key name show


def AjaxFun(request):
    return render(request,'ajax.html')


def Ajax2Fun(request):
    if(request.method=='POST'):
        name=request.POST['name']
        age=request.POST['age']
        place=request.POST['place']
        print(name,age,place)
        objajax=ajax2(name=name,age=age,place=place)
        objajax.save()
        return JsonResponse({'msg':'saved successfully....'})
    return render(request,'ajax2.html')

# getting data from database(table)
def fnloaddata(request):
    obj=ajax2.objects.all()
    obj1=[{'id':i.id,'name':i.name,'age':i.age,'place':i.place} for i in obj ]
    return JsonResponse({'data':obj1})


# getting data from db in textfeild
def fndataupdate(request):
    if(request.method=='POST'):
        upid=request.POST['id']
        print(upid)
        obj=ajax2.objects.get(id=upid)
        print(obj)
        objup1=[{'id':obj.id,'name':obj.name,'age':obj.age,'place':obj.place}]
        return JsonResponse({'userObj':objup1})

   

# chnaging value in text
def fnupdatedata(request):
    if(request.method=='POST'):
        upid=request.POST['id']
        name=request.POST['name']
        age=request.POST['age']
        place=request.POST['place']
        ajax2.objects.filter(id=upid).update(name=name,age=age,place=place)
        return JsonResponse({'msg1':'successfully updated ...'})


def fndelete(request):
    uid=request.POST['id']
    ajax2.objects.get(id=uid).delete()
    return JsonResponse({'delmsg':'delete successfully....'})






@api_view(['GET'])
def apiFn(request):
    msg='hello api'
    return Response(msg)


@api_view(['POST'])
def api1(request):
    username=request.data['username']
    print(username)
    password=request.data['password']
    print(password)
    obj=api(username=username,password=password)
    obj.save()
    return Response({'msg':'data inserted successfully'})


@api_view(['DELETE'])
def fnapidel(request):
    userid=request.data['id']
    print(userid)
    api.objects.get(id=userid).delete()
    return Response({'msg1':'deleted successfully'})

    
def dashboard(request):
    return render(request,'registration/dashboard.html')
# ***************************************************************************************************************




def blogerFn(request):
    return render(request,'bloger.html')






    

