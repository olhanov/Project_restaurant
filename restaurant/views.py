from django.shortcuts import render, redirect

# Create your views here.

from .models import MenuItem
from django.http import JsonResponse
from .models import Reservation
from .forms import ReservationForm
from .models import Testimonial
from .models import SpecialDish
from .models import GalleryImage
from .forms import ContactForm
from django.contrib import messages

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserProfile

from .forms import ProfilePhotoForm
from django.contrib.auth import logout

from .models import UserComment




def menu(request):
    return render(request, 'restaurant/menu.html')

def test(request):
    return render(request, 'restaurant/test.html')

def menu_view(request):
    entradas = MenuItem.objects.filter(category='entradas')
    carne = MenuItem.objects.filter(category='carne')
    peixe = MenuItem.objects.filter(category='peixe')
    sobremesas = MenuItem.objects.filter(category='sobremesas')
    bebidas = MenuItem.objects.filter(category='bebidas')

    form = ReservationForm()  # Load the reservation form
    reservation_success = False

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            reservation_success = True  # Reservation is successful

    return render(request, 'restaurant/menu.html', {
        'entradas': entradas,
        'carne': carne,
        'peixe': peixe,
        'sobremesas': sobremesas,
        'bebidas': bebidas,
        'form': form,
        'reservation_success': reservation_success
    })

def reservation_view(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False})

def index_view(request):
    testimonials = Testimonial.objects.all()
    special_dishes = SpecialDish.objects.all()
    return render(request, 'restaurant/index.html', {
        'testimonials': testimonials,
        'special_dishes': special_dishes,
    })

def search_view(request):
    query = request.GET.get('q')
    results = []

    if query:
        results = SpecialDish.objects.filter(name__icontains=query) | SpecialDish.objects.filter(description__icontains=query)

    return render(request, 'restaurant/search_results.html', {'query': query, 'results': results})


def gallery_view(request):
    images = GalleryImage.objects.all()
    return render(request, 'restaurant/galeria.html', {'images': images})

def sobre_nos_view(request):
    return render(request, 'restaurant/sobre-nos.html')



def contactos_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Зберігає повідомлення у базу даних
            messages.success(request, 'Obrigado! A mensagem foi enviada!')
            return redirect('contactos')  # Повертає на ту ж сторінку після успішного збереження
    else:
        form = ContactForm()
    
    return render(request, 'restaurant/contactos.html', {'form': form})


def reservas_view(request):
    return render(request, 'restaurant/reservas.html')

def login_view(request):
    if request.method == 'POST':
        form_type = request.POST.get('form_type')  # Отримання типу форми
        
        if form_type == 'login':  # Це логін
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Ви успішно увійшли у систему!')
                return redirect('personal_account')  # Перенаправлення до персональної сторінки
            else:
                messages.error(request, 'Невірне ім’я користувача або пароль')

        elif form_type == 'register':  # Це реєстрація
            register_username = request.POST['register-username']
            register_email = request.POST['register-email']
            register_password = request.POST['register-password']
            register_address = request.POST.get('address')
            register_telemovel = request.POST.get('telemovel')

            if User.objects.filter(username=register_username).exists():
                messages.error(request, 'Цей користувач вже існує')
            else:
                # Створення нового користувача
                user = User.objects.create_user(
                    username=register_username, 
                    email=register_email, 
                    password=register_password
                )
                # Створення запису у профілі користувача
                UserProfile.objects.create(
                    user=user, 
                    address=register_address, 
                    telemovel=register_telemovel
                )
                login(request, user)
                messages.success(request, 'Ви успішно зареєструвалися та увійшли у систему!')
                return redirect('personal_account')

    return render(request, 'restaurant/my_account.html')



@login_required
def personal_account(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    photo_form = ProfilePhotoForm(instance=user_profile)

    if request.method == 'POST':
        if 'photo_upload' in request.POST:
            photo_form = ProfilePhotoForm(request.POST, request.FILES, instance=user_profile)
            if photo_form.is_valid():
                photo_form.save()
                return redirect('personal_account')
        
        elif 'comment' in request.POST:
            comment_text = request.POST.get('comment')
            if comment_text:
                UserComment.objects.create(
                    user=request.user,
                    comment=comment_text,
                    photo=user_profile.profile_photo if user_profile.profile_photo else None
                )
                return redirect('personal_account')
    
    context = {
        'full_name': request.user.get_full_name(),
        'email': request.user.email,
        'telemovel': user_profile.telemovel,
        'address': user_profile.address,
        'photo_form': photo_form,
        'user_profile': user_profile,
    }

    return render(request, 'restaurant/personal_account.html', context)



def logout_view(request):
    logout(request)
    return redirect('index')  # Повернення на головну сторінку після виходу


def get_user_comment_data(request, comment_id):
    try:
        user_comment = UserComment.objects.get(id=comment_id)
        data = {
            'name': user_comment.user.username,
            'comment': user_comment.comment,
            'photo': user_comment.photo.url if user_comment.photo else None,
        }
        return JsonResponse(data)
    except UserComment.DoesNotExist:
        return JsonResponse({'error': 'Comment not found'}, status=404)