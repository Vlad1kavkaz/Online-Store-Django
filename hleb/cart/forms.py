from django import forms
from datetime import datetime

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(initial=1, min_value=1, max_value=100)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)



class AdressForm(forms.Form):
    phonenumber = forms.CharField(label='Телефон', widget=forms.TextInput(attrs={'class': 'form-input'}), initial='+7')
    delivery = forms.BooleanField(label='Доставка', required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'width: 20px; height: 20px;'}))
    adress = forms.CharField(label='Адрес', widget=forms.TextInput(attrs={'class': 'form-input'}))
    time_date = forms.DateTimeField(label='Дата и время', widget=forms.DateTimeInput(attrs={'class': 'form-input', 'type': 'datetime-local'}))
    comment = forms.CharField(label='Комментарий', required=False, widget=forms.Textarea(attrs={'class': 'form-input', 'placeholder': 'Введите комментарий к заказу, ваши пожелания, уточнения и прочее'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['delivery'].widget.attrs['onclick'] = "toggleAddressField()"
        self.fields['time_date'].widget.attrs['min'] = datetime.now().strftime('%Y-%m-%dT%H:%M')

