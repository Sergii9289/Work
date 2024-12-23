from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.views import View
from .forms import BookForm
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .models import Book


class BookRecordFormView(FormView):  # The FormView class allows us to easily create views that deal with forms
    template_name = 'book_form.html'  # name of the template
    form_class = BookForm  # the form class that it should use to render the form
    success_url = '/book_management/entry_success'

    def form_valid(self,
                   form):  # method provided by FormView class, which is called when form successfully finished validation
        form.save()
        return super().form_valid(form)  # call the form_valid() method of FormMixin class,
    # which redirect us to success_url


class FormSuccessView(View):
    def get(self, request, *args,
            **kwargs):  # Render a template. Pass keyword arguments from the URLconf to the context
        return HttpResponse('Book record saved successfully')


class BookCreateView(CreateView):
    model = Book
    fields = ['name', 'author']
    template_name = 'book_form.html'
    success_url = '/book_management/entry_success'


class BookRecordDetailView(DetailView):  # must be called with object's PK imported from URL
    model = Book
    template_name = 'book_detail.html'


class BookUpdateView(UpdateView):
    model = Book
    fields = ['name', 'author']
    template_name = 'book_form.html'
    success_url = '/book_management/entry_success'


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_delete_form.html'
    success_url = '/book_management/delete_success'


class FormDeleteSuccessView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Book record deleted')
