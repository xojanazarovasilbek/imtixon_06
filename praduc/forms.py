from django import forms
from .models import News, Contact, Comment, User
class CategoryForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['user','category','title', 'desc', 'price',  'image']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'info', 'text']

from django import forms
from .models import News

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['user','category','title', 'desc', 'price',  'image'] 

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['pos_text']  
        widgets = {
            'pos_text': forms.Textarea(attrs={
                'rows': 3,
                'class': 'form-control',
                'placeholder': 'Fikringizni yozing...'
            })
        }


class ProfilForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email']