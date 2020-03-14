from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.http import urlencode
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from webapp.forms import SimpleSearchForm, FileForm
from webapp.models import File


class IndexView(ListView):
    model = File
    template_name = 'index.html'
    ordering = ['-created_at']
    paginate_by = 10
    paginate_orphans = 1


    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context


    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(caption__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset


    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)


    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None

class FileView(DetailView):
    model = File
    template_name = 'detail.html'


class FileCreateView(CreateView):
    model = File
    template_name = 'create.html'
    form_class = FileForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        if self.request.user.is_authenticated:
            self.object.author = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('webapp:index')

class FileUpdateView(UpdateView):
    model = File
    form_class = FileForm
    context_object_name = 'file'
    template_name = 'update.html'

    def get_success_url(self):
        return reverse('webapp:file_detail', kwargs={'pk': self.object.pk})

class FileDeleteView(DeleteView):
    model = File
    context_object_name = 'file'
    template_name = 'delete.html'
    success_url = reverse_lazy('webapp:index')
