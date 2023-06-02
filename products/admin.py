from django.contrib import admin
from .models import Product,Category,Comment,Question,Answer,Image,ProductOption,ProductPrice

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','slug','parent']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass

@admin.register(ProductOption)
class ProductOptionAdmin(admin.ModelAdmin):
    pass

@admin.register(ProductPrice)
class ProductPriceAdmin(admin.ModelAdmin):
    pass

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass