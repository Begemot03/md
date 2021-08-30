from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import Widget

class ClientForm(forms.Form):
    secondName = forms.CharField(max_length=20, label='Фамилия', widget=forms.TextInput(attrs={'placeholder':'Фамилия'}))
    firstName = forms.CharField(max_length=20, label='Имя', widget=forms.TextInput(attrs={'placeholder':'Имя'}))
    middleName = forms.CharField(max_length=20, label='Отчество', widget=forms.TextInput(attrs={'placeholder':'Отчество'}))
    age = forms.IntegerField(min_value=0, label='Возраст', widget=forms.NumberInput(attrs={'placeholder':'Возраст'}))
    address = forms.CharField(max_length=150, label='Адрес', widget=forms.TextInput(attrs={'placeholder':'Адрес'}))
    mail = forms.EmailField(label='Почта', widget=forms.TextInput(attrs={'placeholder':'Email'}))
    imgBefore = forms.ImageField(label='До')
    imgAfter = forms.ImageField(label='После')
    comment1 = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Комментарий'}), label='Первый комментарий')
    comment2 = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Комментарий'}), label='Второй комментарий')
    comment3 = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Комментарий'}), label='Третий комментарий')
    sel1 = forms.ChoiceField(choices=(
        (1, 'One'),
        (2, 'Two'),
        (3, 'Three'),
    ), label='Первый выпадающий список', widget=forms.Select(attrs={'class':'custom-select'}))
    sel2 = forms.ChoiceField(choices=(
        (1, 'One'),
        (2, 'Two'),
        (3, 'Three'),
    ), label='Второй выпадающий список', widget=forms.Select(attrs={'class':'custom-select'}))
    sel3 = forms.ChoiceField(choices=(
        (1, 'One'),
        (2, 'Two'),
        (3, 'Three'),
    ), label='Третий выпадающий список', widget=forms.Select(attrs={'class':'custom-select'}))
    #date_register = forms.DateField(label='Дата')