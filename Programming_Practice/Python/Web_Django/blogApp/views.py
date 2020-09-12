from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, FormView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView
from django.views.generic.dates import MonthArchiveView, DayArchiveView, TodayArchiveView
from tagging.views import TaggedObjectList
from blogApp.models import Post
from tagging.models import Tag, TaggedItem
from blogApp.forms import PostSearchForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from Web_Django.views import LoginRequiredMixin
from django.urls import reverse_lazy


# Create your views here.


class PostLV(ListView):
    model = Post
    template_name = "blogApp/post_all.html"
    context_object_name = "posts"
    paginate_by = 2


class PostDV(DetailView):
    model = Post


class PostAV(ArchiveIndexView):
    model = Post
    date_field = "modify_date"


class PostYAV(YearArchiveView):
    model = Post
    date_field = "modify_date"
    make_object_list = True


class PostMAV(MonthArchiveView):
    model = Post
    date_field = "modify_date"


class PostDAV(DayArchiveView):
    model = Post
    date_field = "modify_date"


class PostTAV(TodayArchiveView):
    model = Post
    date_field = "modify_date"


class TagTV(TemplateView):
    template_name = 'tagging/tagging_cloud.html'


class PostTOL(TaggedObjectList):
    model = Post
    template_name = 'tagging/tagging_post_list.html'


class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'blogApp/post_search.html'

    def form_valid(self, form):
        search_word = f"{self.request.POST['search_word']}"
        post_list = Post.objects.filter(Q(title__icontains=search_word) \
                                        | Q(description__icontains=search_word) \
                                        | Q(content__icontains=search_word)).distinct

        context = dict()
        context['form'] = form
        context['search_term'] = search_word
        context['object_list'] = post_list

        return render(self.request, self.template_name, context)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'slug', 'description', 'content', 'tag']
    initial = {'slug': 'auto-filling-do-not-input'}
    #fields = ['title, 'description', 'content', 'tag']
    success_url = reverse_lazy('blogApp:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(PostCreateView, self).form_valid(form)


class PostChangeLV(LoginRequiredMixin, ListView):
    template_name = 'blogApp/post_change_list.html'

    def get_queryset(self):
        return Post.objects.filter(owner=self.request.user)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'slug', 'description', 'content', 'tag']
    success_url = reverse_lazy('blogApp:index')


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blogApp:index')
