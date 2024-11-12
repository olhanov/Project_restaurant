from django.db import models
from django.contrib.auth.models import User


class MenuItem(models.Model):
    category_choices = [
        ('entradas', 'Entradas'),
        ('carne', 'Carne'),
        ('peixe', 'Peixe'),
        ('sobremesas', 'Sobremesas'),
        ('bebidas', 'Bebidas'),
    ]
    category = models.CharField(max_length=20, choices=category_choices)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
    

class Reservation(models.Model):
    date = models.DateField()
    time = models.TimeField()
    people = models.IntegerField()

    def __str__(self):
        return f"Reservation for {self.people} people on {self.date} at {self.time}"    


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100, blank=True, null=True)
    photo = models.ImageField(upload_to='testimonials/')
    quote = models.TextField()

    user_comment = models.ForeignKey('UserComment', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name
    


class SpecialDish(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    rating = models.IntegerField(default=5)
    image = models.ImageField(upload_to='special_dishes/')
    menu_items = models.ManyToManyField(MenuItem, blank=True, related_name="special_dishes")  # зв'язок з MenuItem

    def __str__(self):
        return self.name
    

class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery/')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"


class UserProfile(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, blank=True, null=True)
    telemovel = models.CharField(max_length=15, blank=True, null=True)
    
    profile_photo = models.ImageField(upload_to='user_profiles/', blank=True, null=True)  # Додаємо поле фото


    def __str__(self):
        return self.user.username
    

class UserComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    photo = models.ImageField(upload_to='user_comments/', blank=True, null=True)  # Додатково для фото користувача
    approved = models.BooleanField(default=False)  # Поле для статусу затвердження адміністратором
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username}"
    

