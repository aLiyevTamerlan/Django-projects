# from curses.ascii import HT
# from email import message
# from tabnanny import check
#from os import PRIO_PGRP
from unicodedata import category
from django.db.models import Q
import re,json
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.urls import reverse
from django.contrib import messages,auth
from django.core import serializers
from product.models import Product,Comment,Notice,Own,Contact
from product.templatetags import extras
from product import urls as ur
from django.core.paginator import Paginator
def all(request):
    mehsul=Product.objects.all()
    ordering = request.GET.get('ordering')
    if ordering:
        mehsul = mehsul.order_by(ordering)
    paginator=Paginator(mehsul,6)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number) 
    return render(request,'all.html',context={'mehsullar':page_obj,'ordering':ordering})
def daxil_ol(request):
    if (request.method == 'POST'):
        username=request.POST.get("dusername")
        password=request.POST.get("dpassword")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        return render(request,'yoxlama.html')
    return render(request,'account-login.html')

def qeydiyyat(request):
    if (request.method == 'POST'):
        username = request.POST.get("qusername")
        password = request.POST.get("qpassword")
        confirm = request.POST.get("qpasswordagain")
        if password != confirm:
            print("sehvlik var")
            return redirect('register')
        new_user = User.objects.create_user(username=username, password=password)
        new_user.save()
        print("Her sey duzdur")
        return render(request,'account-login.html')
    return render(request,'account-register.html')
def home(request):
    mehsul=Product.objects.all()
    return render(request, 'index.html',context={'mehsullar':mehsul})
def  fill(query):
    return query["animal_category"]
def logout(request):
    auth.logout(request)
    return redirect('home')
def contact(request):
    if(request.method=='POST'):
        user_email=request.POST.get("user_email")
        user_message=request.POST.get("user_message")
        us_message=Contact(author=request.user,email=user_email,message=user_message)
        us_message.save()
    return render(request, 'contact.html')
def elave(request): 
    dogCategorys=Product.objects.filter(animal_type="it")
    catCategorys=Product.objects.filter(animal_type="pisiy")
    birdCategorys=Product.objects.filter(animal_type="qus")
    dogCategorys = serializers.serialize('json', dogCategorys,fields=('animal_category',))
    catCategorys=serializers.serialize('json', catCategorys,fields=('animal_category',)) 
    birdCategorys = serializers.serialize('json', birdCategorys,fields=('animal_category',))
    if (request.method == 'POST'):
        heyvan_novu=request.POST.get('animal_type')
        mehsul_ad=request.POST.get('animal_name')
        mehsul_haqqinda=request.POST.get('animal_content')
        mehsul_sekil=request.FILES.get('animal_image')
        mehsul_kategoriyası=request.POST.get('animal_category')
        mehsul_cinsi=request.POST.get('animal_gender')
        mehsul=Product(author=request.user,animal_type=heyvan_novu, image=mehsul_sekil, product_name=mehsul_ad, product_content=mehsul_haqqinda,
                        animal_gender=mehsul_cinsi,animal_category=mehsul_kategoriyası)
        mehsul.save()
        return render(request,'mehsul_elave.html',context={'dogCategorys':dogCategorys,'catCategorys':catCategorys,'birdCategorys':birdCategorys})
    return render(request,'mehsul_elave.html',context={'dogCategorys':dogCategorys,'catCategorys':catCategorys,'birdCategorys':birdCategorys})
def about(request):
    return render(request,'about.html')
def share(request):
    if request.user.is_authenticated:
        animal_count=4
        mehsul=Product.objects.filter(author=request.user)
        paginator=Paginator(mehsul,animal_count)
        page_number=request.GET.get('page')
        page_obj=paginator.get_page(page_number) 
        return render(request,'paylasma.html',context={"mehsullar":page_obj})
    else: return HttpResponse('qeydiyyat')
    
def owned(request):
    owned=Notice.objects.filter(gonderen=request.user)
    animal_count=4
    paginator=Paginator(owned,animal_count)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number) 
    print(owned)
    return render(request,'sahiblenme.html',context={'owns':page_obj})
def blog(request):
    return render(request,'blog-right-sidebar.html')
def animal(request,slug):
    mehsul=Product.objects.filter(animal_type=slug)
    animal_count=6
    ordering = request.GET.get('ordering')
    cat=request.GET.get('animal_category')
    gen=request.GET.get('animal_gender')
    categorys=Product.objects.filter(animal_type=slug).values('animal_category').distinct()
    if cat and gen:
        mehsul = Product.objects.filter(animal_category=cat).filter(animal_gender=gen)
    elif gen:
        mehsul = Product.objects.filter(animal_gender=gen) 
    elif cat:
        mehsul = Product.objects.filter(animal_category=cat)
    if ordering:
        mehsul = mehsul.order_by(ordering)
    paginator=Paginator(mehsul,animal_count)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number) 
    return render(request,'animal.html',context={'mehsullar':page_obj,'categorys':categorys,'ordering':ordering,'animal_count':animal_count})

def yoxlama(request):
    return render(request,'yoxlama.html')

def paylasmam(request):
    qeydiyyat(request)
    mehsul=Product.objects.filter(author=request.user)
    if request.user.is_authenticated:
        bildiris = Notice.objects.filter(qebul_eden=request.user)
        return render(request,'paylasmalarim.html',{'mehsullar':mehsul,'bildirisler':bildiris})
    
    return render(request,'paylasmalarim.html',{'mehsullar':mehsul})
# Create your views here.
def heyvan_haqqinda(request,id):
    mehsullar = Product.objects.filter(id=id)
    mehsul=Product.objects.filter(id=id).first()
    animal_related_category=list(map(lambda x:x.animal_category,mehsullar))[0]
    animal_relateds=Product.objects.filter(animal_category= animal_related_category)
    comments_count=Comment.objects.filter(product=id)
    comments=Comment.objects.filter(product=mehsul,parent=None)
    replies = Comment.objects.filter(product=mehsul).exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.id not in replyDict.keys():
            replyDict[reply.parent.id] = [reply]
        else:
            replyDict[reply.parent.id].append(reply)
    return render(request,'mehsul_haqqinda.html',{'mehsullar':mehsullar,'comments':comments,'mehsul':mehsul,
                                                  'replyDict':replyDict,'comments_count':comments_count,'animal_relateds':animal_relateds})

def product_comment(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            comment = request.POST.get('comment')
            user = request.user
            product_id = int(request.POST.get('productId'))
            product = Product.objects.get(id=product_id)
            parent_id=request.POST.get('parentId')
            if parent_id=="":
                comment = Comment(comment=comment, user_from=user, product=product)
                comment.save()
            else:
                parent=Comment.objects.get(id=parent_id)
                comment = Comment(comment=comment, user_from=user, product=product,parent=parent,user_to=user)
                comment.save()
        else: return HttpResponse('qeydiyyat')
    return redirect(f"/heyvan/{product.id}")

def search(request):
    search=request.POST.get('search')
    if search.capitalize() in list(map(fill,Product.objects.all().values('animal_category').distinct())):
        mehsul=Product.objects.filter(animal_category=search.capitalize())
    elif search.lower() in ['it','pisiy','qus']:
        mehsul=Product.objects.filter(animal_type=search.lower())
    return render(request,'search.html',context={'mehsullar':mehsul})
    


def sahiblenme(request):
    if (request.method=='POST'):
        product_id=request.POST.get('mehsul_id')
        product =Product.objects.get(id=product_id)
        gonderen=request.user
        qebul_eden=product.author
        new_messages=Notice(gonderen=gonderen,qebul_eden=qebul_eden,product=product,image=product.image)
        new_messages.save()
        message=Notice.objects.filter(qebul_eden=request.user)
        return redirect(f"/heyvan/{product_id}")

def tesdiq_legv(request):
    a = request.META['HTTP_REFERER']
    if (request.method == 'POST') and ('tesdiq' in request.POST):
        bildiris_id=request.POST["bildiris_id"]
        bildiris=Notice.objects.get(id=bildiris_id)
        bildiris.tesdiq=True
        bildiris.save()
    elif (request.method == 'POST') and ('legv' in request.POST):
        bildiris_id=request.POST["bildiris_id"]
        bildiris=Notice.objects.get(id=bildiris_id)
        bildiris.tesdiq=False
        bildiris.save()
    return redirect(a)
def kabinet(request):
    checkNullVariable={}
    bildirisler=Notice.objects.all()
    if request.user.is_authenticated:
        comments=Comment.objects.filter(user_from=request.user)
        mehsul=Product.objects.filter(author=request.user)
        if(request.GET.get('comment')=="Comment"):
            comments=Comment.objects.filter(parent=None,user_from=request.user)
            return render(request,'own_cabinet.html',{'comments':comments,'checkNullVariable':checkNullVariable,'mehsullar':mehsul})
        elif(request.GET.get('comment')=="Yanit"):
            comments=Comment.objects.filter(user_from=request.user).exclude(parent=None)
            return render(request,'own_cabinet.html',{'comments':comments,'checkNullVariable':checkNullVariable,'mehsullar':mehsul})
        elif(request.GET.get('comment')=="Comments"):
            comments=Comment.objects.filter(user_from=request.user)

        if(request.GET.get('notification')=="Notifications"):
            bildirisler=Notice.objects.all()
            return render(request,'own_cabinet.html',{'bildirisler':bildirisler,'checkNullVariable':checkNullVariable,'mehsullar':mehsul})
        elif(request.GET.get('notification')=="Approved"):
            bildirisler=Notice.objects.filter(tesdiq=True)
        elif(request.GET.get('notification')=="Canceled"):
            bildirisler=Notice.objects.filter(tesdiq=False)
        elif(request.GET.get('notification')=="Unanswered"):
            bildirisler=Notice.objects.filter(tesdiq=None)
    else:
        return HttpResponse('qeydiyyat')
    return render(request,'own_cabinet.html',{'comments':comments,'bildirisler':bildirisler,'checkNullVariable':checkNullVariable,'mehsullar':mehsul})
