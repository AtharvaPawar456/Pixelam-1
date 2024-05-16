from django import forms
from .models import MyModel
import base64

class MyModelForm(forms.ModelForm):
    image = forms.ImageField(required=True)

    class Meta:
        model = MyModel
        fields = ['name']

    def save(self, commit=True):
        instance = super(MyModelForm, self).save(commit=False)
        image = self.cleaned_data.get('image')

        if image:
            instance.image_data = base64.b64encode(image.read()).decode('utf-8')

        if commit:
            instance.save()
        return instance
