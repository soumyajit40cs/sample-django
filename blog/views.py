from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import Settings
from django.conf.urls.static import static
from blog.models import Post, Comment
from django.utils import timezone
from django.views.generic import View, TemplateView, ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import connection
from django.db.models import Count, Q
#from django.db.models.expressions import DateTime
# Create your views here.

def index(request):
    fetch_post_data = Post.objects.filter(published_date__lte=timezone.now()).order_by('-created_date')[:5]
    #fetch_pgraph_data = Post.objects.raw("select count(title) as uno,published_date from blog_post group by DATE(published_date)")
    #fetch_pgraph_data = Post.objects.raw("select * from blog_post")
    fetch_pgraph_data = Post.objects.extra({'published_date' : "date(published_date)"}).values('published_date').annotate(created_count=Count('id'))
    template_var = {'postodj':fetch_post_data,'userdataobj':fetch_pgraph_data}
    return render(request,'home.html',context=template_var)

def contact(request):
    template_var = {'body_text':''}
    return render(request,'contact.html',context=template_var)

class AllPostList(ListView):
    context_object_name = 'topic_list'
    queryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('-created_date')
    paginate_by = 10

class PostDetails(DetailView):
    context_object_name = 'topic_details'
    queryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('-created_date')
