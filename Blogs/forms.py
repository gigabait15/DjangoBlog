from django import forms
from Blogs.models import Blog

class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Настраиваем атрибуты каждого поля формы
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': (
                    'w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm '
                    'focus:outline-none focus:border-blue-500 dark:bg-gray-800 dark:border-gray-700 '
                    'dark:text-white'
                ),
                'placeholder': field.label
            })

class BlogForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'image', 'tags']
        labels = {
            'title': 'Заголовок',
            'content': 'Содержание',
            'image': 'Изображение',
            'tags': 'Теги'
        }


