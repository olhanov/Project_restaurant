from django.contrib import admin
from .models import MenuItem
from .models import Reservation
from .models import Testimonial
from .models import SpecialDish
from .models import GalleryImage
from .models import ContactMessage
from .models import UserProfile
from .models import UserComment


admin.site.register(MenuItem)
admin.site.register(Reservation)

admin.site.register(SpecialDish)
admin.site.register(GalleryImage)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('created_at',)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'telemovel', 'address']
   
@admin.register(UserComment)
class UserCommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment', 'approved', 'created_at')
    list_filter = ('approved',)
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
    approve_comments.short_description = "Approve selected comments"


class TestimonialAdmin(admin.ModelAdmin):
    
    list_display = ['name', 'profession', 'quote']
    fields = ['name', 'profession', 'photo', 'quote', 'user_comment']  # додаємо поле user_comment


    def save_model(self, request, obj, form, change):
        # Перевірка перед збереженням для заповнення даних з user_comment
        if obj.user_comment:
            obj.name = obj.user_comment.user.username  # Ім'я користувача
            obj.photo = obj.user_comment.photo         # Фото
            obj.quote = obj.user_comment.comment       # Текст коментаря
        super().save_model(request, obj, form, change)

admin.site.register(Testimonial, TestimonialAdmin)

