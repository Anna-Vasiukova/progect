from django import forms


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(label="", widget=forms.NumberInput(attrs={"class":
                                                    "d-flex justify-content-left"}))
