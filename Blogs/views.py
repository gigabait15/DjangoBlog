from django.urls import reverse_lazy, reverse
from django.views import generic
from Blogs.forms import BlogForm
from Blogs.models import Blog


class BlogListView(generic.ListView):
    model = Blog
    template_name = 'Blogs/blog_list.html'

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = 'Blogs/blog_detail.html'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_of_views += 1
        self.object.save()
        return self.object

    def get_context_data(self, **kwargs):
        # Получаем текущий контекст
        context = super().get_context_data(**kwargs)
        # Получаем текущую статью
        current_blog = self.object
        # Получаем следующую статью, если она есть
        next_blog = Blog.objects.filter(id__gt=current_blog.id).order_by('id').first()
        # Получаем предыдущую статью, если она есть
        previous_blog = Blog.objects.filter(id__lt=current_blog.id).order_by('-id').first()
        # Добавляем в контекст как следующую, так и предыдущую статью
        context['next_blog'] = next_blog
        context['previous_blog'] = previous_blog
        # получение списка тегов
        context['tags_list'] = current_blog.tags.split(",") if current_blog.tags else []
        # получение количетсва страниц
        current_blog = self.object
        total_blog_count = Blog.objects.count()  # Общее количество статей
        current_blog_index = Blog.objects.filter(id__lte=current_blog.id).count()  # Номер текущей статьи
        context['current_blog_index'] = current_blog_index
        context['total_blog_count'] = total_blog_count

        return context


class BlogCreateView(generic.CreateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blog:blog_list')


class BlogUpdateView(generic.UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = 'Blogs/blog_form.html'

    # def has_permission(self):
    #     """Проверка на суперпользователя или автора публикации """
    #     if self.request.user == self.request.user:
    #         return True
    #     return super().has_permission()

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:blog_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(generic.DeleteView):
    model = Blog

