from django.contrib import admin
from review.models import Review, Category

class ReviewAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Review, ReviewAdmin)
admin.site.register(Category, CategoryAdmin)