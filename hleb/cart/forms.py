from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(initial=1, min_value=1, max_value=100)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)



class AdressForm(forms.Form):
    phonenumber = forms.CharField(label='Телефон', widget=forms.TextInput(attrs={'class': 'form-input'}))
    delivery = forms.BooleanField(label='Доставка', required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'width: 20px; height: 20px;'}))
    adress = forms.CharField(label='Адрес', widget=forms.TextInput(attrs={'class': 'form-input'}))
    time_date = forms.DateTimeField(label='Дата и время', widget=forms.DateTimeInput(attrs={'class': 'form-input', 'type': 'datetime-local'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['delivery'].widget.attrs['onclick'] = "toggleAddressField()"