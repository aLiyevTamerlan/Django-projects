from django.contrib import admin
from .models import Product,Comment,Notice,Own,Contact
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['author','product_name','image','animal_type','animal_gender','animal_category']
class NoticeAdmin(admin.ModelAdmin):
    list_display = ['gonderen','qebul_eden','product','tesdiq','image']
class CommentAdmin(admin.ModelAdmin):
    list_display=['user_from','comment','parent','product','user_to']
class OwnAdmin(admin.ModelAdmin):
    list_display=['sahiblenen','mehsul_sahibi','product','timestamp']
admin.site.register(Product,ProductAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Notice,NoticeAdmin)
admin.site.register(Own,OwnAdmin)
admin.site.register(Contact) 




