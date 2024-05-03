from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from .models import ForumPost, ForumPostComment, AutorPost
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse

# Create your views here.

def home_view(request, *args,**kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "forum.html", {})

class ForumPostListView(ListView):
    model = ForumPost

class ForumListbyAuthorView(ListView):

    model = ForumPost
    template_name ='foruns/forum_list_by_author.html'
    
    def get_queryset(self):
        id = self.kwargs['pk']
        target_author=get_object_or_404(AutorPost, pk = id)
        return ForumPost.objects.filter(author=target_author)
        
    def get_context_data(self, **kwargs):
        context = super(ForumListbyAuthorView, self).get_context_data(**kwargs)
        context['Autor do post'] = get_object_or_404(AutorPost, pk = self.kwargs['pk'])
        return context
    
class ForumPostDetailView(DetailView):
    model = ForumPost

class AutorListView(ListView):
    model = AutorPost

class ForumCommentCreate(LoginRequiredMixin, CreateView):
    model = ForumPostComment
    fields = ['description']

    def get_context_data(self, **kwargs):
        context = super(ForumCommentCreate, self).get_context_data(**kwargs)
        context["forum"] = get_object_or_404(ForumPost, pk = self.kwargs['pk']) 
        return context
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.forum = get_object_or_404(ForumPost, pk = self.kwargs['pk'])
        return super(ForumCommentCreate ,self).form_valid(form)
    
    def get_success_url(self) -> str:
        return reverse('forum-detail', kwargs={'pk':self.kwargs['pk'],})
    
    
