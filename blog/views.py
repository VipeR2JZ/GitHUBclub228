from django.views.generic import ListView, DetailView,TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView  # новое
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import EditProfileForm
from .models import Post
from django.db.models import Q


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'



class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']


class BlogDeleteView(DeleteView):  # Создание нового класса
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

@login_required
def edit_profile(request):
    user = request.user
    form = EditProfileForm(request.POST or None, instance=user)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('profile')

    context = {
        'form': form,
    }
    return render(request, 'edit_profile.html', context)

@login_required
def profile(request):
    user = request.user
    context = {'user': user}
    return render(request, 'profile.html', context)



class HomePageView(TemplateView):
    template_name = 'home.html'


class SearchResultsView(ListView):
    model = Post
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(Q(body__icontains=query) | Q(title__icontains=query))

        return object_list






