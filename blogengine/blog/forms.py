from django import from .forms import 
from .models import Tag

class TagForm(forms.Form):
    title = forms.CharField(maxlength=50)
    slug = forms.CharField(maxlength=50)

    def save(self):
        new_tag = Tag.objects.create(
            title=self.cleaned_data['title'],
            slug = self.cleaned_data['slug']
        )
        return new_tag