from django.shortcuts import render
from django.views import generic
from .models import blog
from django.contrib.auth.mixins import LoginRequiredMixin

class blogCreateView(LoginRequiredMixin, generic.CreateView):
    model = blog
    fields = ['title','image','description']
    template_name = "create.html"
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug= self.request.POST.get('title').replace(' ','-')
        return super().form_valid(form)
    
class blogListView(generic.ListView):
    model = blog
    template_name = "home.html"

class blogDetailView(generic.DetailView):
    model = blog
    template_name = "detail.html"
    context_object_name = "tag"
