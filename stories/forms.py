from django import forms
from .models import Contact
from .models import Stories
from tinymce import TinyMCE



class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class AddStoryForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )
    class Meta:
        model = Stories
        fields = ('student_name', 'student_overview', 'band_score', 'writing_score',
        'reading_score', 'speaking_score', 'listening_score', 'thumbnail')



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        # fields = ("first_name", "last_name", "e_mail")
        # exclude = ("first_name",)

        widgets = {
            "first_name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your first name'}),
            "last_name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your last name'}),
            "e_mail": forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            "phone_number": forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}),
            "contact_message": forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your message'})
        }