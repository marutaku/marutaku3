import logging

from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

from django.views import generic

from .forms import InquiryForm

from django.contrib import messages

logger = logging.getLogger(__name__)

from .models import Article

class IndexView(generic.TemplateView):
    template_name = "index.html"

class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('article:inquiry')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'Sent a message.')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)

class ArticleListView(LoginRequiredMixin, generic.ListView):
    model = Article
    template_name = 'article_list.html'
    paginate_by = 5

    def get_queryset(self):
        articles = Article.objects.order_by('-created_at')
        return articles

class ArticleDetailView(LoginRequiredMixin, generic.DetailView):
    model = Article
    template_name = 'article_detail.html'