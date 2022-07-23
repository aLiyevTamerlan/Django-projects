from django.contrib import admin
from django.urls import path,include
from product import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('cixmaq/',views.logout,name='logout'),
    path('register/',views.qeydiyyat,name='register'),
    path('sign_in/',views.daxil_ol,name='sign_in'),
    path('mehsul_elavesi/',views.elave,name='elave'),
    path('heyvan/<int:id>',views.heyvan_haqqinda,name='heyvan_haqqinda'),
    path('animals/<slug:slug>',views.animal),
    path('yoxlama/',views.yoxlama),
    path('paylasmam/',views.paylasmam),
    path('heyvan/productComment/',views.product_comment,name="productComment"),
    path('search/',views.search,name='search'),
    path('sahiblenme/',views.sahiblenme),
    path('tesdiqle/legv/',views.tesdiq_legv,name='tesdiq_legv'),
    path('kabinet/',views.kabinet,name='kabinet'),
    path('contact/',views.contact),
    path('about/',views.about),
    path('blog/',views.blog), 
    path('sahiblenme_page/',views.owned),
    path('share/',views.share),    
    path('all/',views.all)
]