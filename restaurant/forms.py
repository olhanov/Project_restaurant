from django import forms
from .models import Reservation
from .models import ContactMessage
from .models import UserProfile
from .models import Testimonial


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['date', 'time', 'people']


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nome*'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email*'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Telefone*'}),
            'message': forms.Textarea(attrs={'placeholder': 'A Sua mensagem'}),
        }

class ProfilePhotoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_photo']


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['name', 'photo', 'quote', 'user_comment']
        widgets = {
            'name': forms.TextInput(attrs={'id': 'id_name'}),
            'quote': forms.Textarea(attrs={'id': 'id_quote'}),
            'photo': forms.ClearableFileInput(attrs={'id': 'id_photo'}),
        }


