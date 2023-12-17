from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 10)]
PRODUCT_SIZE_CHOICES = [
        ('35', '35'),
        ('36', '36'),
        ('37', '37'),
        ('38', '38'),
        ('39', '39'),
        ('40', '40'),
        ('41', '41'),
]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
#     quantity = forms.IntegerField()
    size = forms.TypedChoiceField(choices=PRODUCT_SIZE_CHOICES,widget=forms.RadioSelect())
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
