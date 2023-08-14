from django.contrib import admin
from .models import Product,Category,Brand,ProductImage,Product_Alternative,Product_Accessories,Order_product

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(ProductImage)
admin.site.register(Product_Alternative)
admin.site.register(Product_Accessories)
admin.site.register(Order_product)

