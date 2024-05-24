from django.db.models import Count
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404, redirect
from .models import ForumPost, ForumPostComment, AutorPost
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import ForumPostForm

# Create your views here.

def home_view(request, *args,**kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "forum.html", {})

class ForumPostListView(ListView):
    model = ForumPost
    paginate_by = 6

    def get_queryset(self):
        queryset = ForumPost.objects.annotate(like_count=Count('likes')).order_by('-like_count', '-post_date')
        return queryset

class ForumListbyAuthorView(ListView):

    model = ForumPost
    template_name ='foruns/forum_list_by_author.html'
    
    def get_queryset(self):
        id = self.kwargs['pk']
        author=get_object_or_404(User, pk = id)
        return ForumPost.objects.filter(author=author)
        
    def get_context_data(self, **kwargs):
        context = super(ForumListbyAuthorView, self).get_context_data(**kwargs)
        context['author'] = get_object_or_404(User, pk = self.kwargs['pk'])
        return context
    
class ForumPostDetailView(DetailView):
    model = ForumPost

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.forumpostcomment_set.annotate(like_count=Count('likes')).order_by('-like_count', '-post_date')
        return context

    

class AutorListView(ListView):
    model = AutorPost

class ForumCommentCreate(LoginRequiredMixin, CreateView):
    model = ForumPostComment
    fields = ['description']

    def get_context_data(self, **kwargs):
        context = super(ForumCommentCreate, self).get_context_data(**kwargs)
        context["forumpost"] = get_object_or_404(ForumPost, pk = self.kwargs['pk']) 
        return context
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.ForumPost = get_object_or_404(ForumPost, pk = self.kwargs['pk'])
        return super(ForumCommentCreate ,self).form_valid(form)
    
    def get_success_url(self):
        return reverse('forumpost-detail', kwargs={'pk':self.kwargs['pk'],})
    
@login_required
def ForumPostCreate(request):
    if request.method == 'POST':
        form = ForumPostForm(request.POST)
        if form.is_valid():
            forum = form.save(commit=False)
            forum.author = request.user
            forum.save()
            return redirect('forumpost-detail', pk=forum.pk)
    else:
        form = ForumPostForm()
    return render(request, 'foruns/forumpost_form.html', {'form': form})

@login_required
def like_forum_post(request, pk):
    post = get_object_or_404(ForumPost, pk=pk)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('forumpost-detail', pk=pk)

@login_required
def like_forum_comment(request, pk):
    comment = get_object_or_404(ForumPostComment, pk=pk)
    if request.user in comment.likes.all():
        comment.likes.remove(request.user)
    else:
        comment.likes.add(request.user)
    return redirect('forumpost-detail', pk=comment.ForumPost.pk)


