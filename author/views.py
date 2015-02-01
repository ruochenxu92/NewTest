from django.shortcuts import render


from django.views.generic import ListView, DetailView
from .models import Publisher, Book
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from .models import Book, Publisher

class PublisherBookList(ListView):

    def get_queryset(self):
        self.publisher = get_object_or_404(Publisher, name=self.args[0])
        return Book.objects.filter(publisher=self.publisher)


class PublisherList(ListView):
    model = Publisher
    context_object_name = 'my_favorite_publishers'




class PublisherDetail(DetailView):

    model = Publisher

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PublisherDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['book_list'] = Book.objects.all()
        return context


class BookList(ListView):
    queryset = Book.objects.order_by('-publication_date')
    context_object_name = 'book_list'


#
# # Create your views here.
# from .forms import ContactForm
# from django.views.generic.edit import FormView
#
# class ContactView(FormView):
#     template_name = 'author/author_form.html'
#     form_class = ContactForm
#     success_url = '/thanks/' #need a thanks
#
#     def form_valid(self, form):
#         # This method is called when valid form data has been POSTed.
#         # It should return an HttpResponse.
#         form.send_email()
#         return super(ContactView, self).form_valid(form)
#
#
#
# from django.views.generic.edit import CreateView
# from .models import Author
#
# class AuthorCreate(CreateView):
#
#     model = Author
#
#     fields = ['name']
#
#
#
#
#
# from django.views.generic.edit import UpdateView
# from .models import Author
#
# class AuthorUpdate(UpdateView):
#     model = Author
#     fields = ['name']
#     template_name_suffix = '_update_form'
#
# from django.views.generic.edit import DeleteView
# from django.core.urlresolvers import reverse_lazy
# from .models import Author
#
# class AuthorDelete(DeleteView):
#     model = Author
#     success_url = reverse_lazy('author-list')
#
# #author create will automatically save the results
# #
#
# from django.views.generic.detail import DetailView
# class AuthorDetailView(DeleteView):
#     model = Author
#
#     def get_context_data(self, **kwargs):
#         context = super(AuthorDetailView, self).get_context_data(**kwargs)
#         return context
#
#
# from django.views.generic.list import ListView
# from django.utils import timezone
#
#
#
# #it will automatically give the html a list of objects with particular model
# #model as input, list of model as output, the name should be author_list
# class AuthorTestView(ListView):
#     model = Author  #should be author_list.html because the name of model is author
#     def get_context_data(self, **kwargs):
#         context = super(AuthorTestView, self).get_context_data(**kwargs)
#         return context