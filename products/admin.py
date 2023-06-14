from django.contrib import admin
from .models import Product,Category,Comment,Question,Answer,Image,ProductOption,ProductPrice

# Register your models here.

    
class ProductImageInline(admin.TabularInline):
    model = Image


class ProductOptionInline(admin.TabularInline):
    model = ProductOption
    
class ProductPriceInline(admin.TabularInline):
    model = ProductPrice
    
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','en_name',"name","category"]
    list_filter = ["category"]
    search_fields = ["en_name,name"]
    inlines = [ProductImageInline,ProductOptionInline,ProductPriceInline]

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','slug','parent']
    list_filter = ['parent']
    search_fields = ['name','description']
    fieldsets =(
        ("details",{
            "fields":("name","slug",
                      "parent",
                     "description",)
        }),
        ("images",{
            "fields":("icon","image",)
        })
    )

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
