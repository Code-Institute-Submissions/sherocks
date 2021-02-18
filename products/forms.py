from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Review


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'rounded-0'


class ProductSelect(forms.Select):
    def create_option(
            self, name, value, label, selected,
            index, subindex=None, attrs=None):
        option = super().create_option(
            name, value, label, selected, index, subindex, attrs)
        if value:
            option['attrs']['name'] = value.instance.name
        return option


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['product', 'review']
        widgets = {'product': ProductSelect}
