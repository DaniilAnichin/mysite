from django.views import generic
from django.shortcuts import render, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from products.models import Production


class DetailView(generic.DetailView):
    model = Production
    template_name = 'products/detail.html'
    context_object_name = 'production'
    slug_field = 'production_id'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        return context


class CreateProductionView(generic.CreateView):
    model = Production
    template_name = 'products/edit_production.html'
    fields = ['name', 'price', 'price_old', 'production_id', 'delivery', 'kids',
              'kid_adult', 'free_porto', 'package', 'women', 'url', 'img_url']
    
    def form_valid(self, form):
        Production.objects.create(**form.cleaned_data)
        return HttpResponseRedirect('/products/')


def selection(request):
    results = Production.objects.all()
    if 'q' in request.GET:
        results = results.filter(name__contains=request.GET['q'])
    if 'hi' in request.GET:
        results = results.filter(price__lte=request.GET['hi'])
    if 'lo' in request.GET:
        results = results.filter(price__gt=request.GET['lo'])
    if 'k' in request.GET:
        if request.GET['k'] == 'on':
            results = results.filter(kids='True')
    if 'a' in request.GET:
        if request.GET['a'] == 'on':
            results = results.filter(kid_adult='True')
    if 'w' in request.GET:
        if request.GET['w'] == 'on':
            results = results.filter(women='True')

    paginator = Paginator(results.order_by('price'), 15)
    page = request.GET.get('page')
    try:
        paginated_results = paginator.page(page)
    except PageNotAnInteger:
        paginated_results = paginator.page(1)
    except EmptyPage:
        paginated_results = paginator.page(paginator.num_pages)
    return render(request, 'products/index.html', {'production_list': paginated_results})