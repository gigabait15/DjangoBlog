from django import forms
from Blog.models import Posts


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"


class PostForm(forms.ModelForm):
    model = Posts


class CreatePostForm(forms.ModelForm):
    model = Posts
    fields = ('title', 'content', 'image')
