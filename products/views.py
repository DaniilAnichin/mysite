from django.views import generic
from django.utils import timezone
from django.shortcuts import render, HttpResponseRedirect, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext

from products.models import production, search_form


class DetailView(generic.DetailView):
    model = production
    template_name = 'products/detail.html'
    context_object_name = 'production'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class CreateProductionView(generic.CreateView):
    model = production
    template_name = 'products/edit_production.html'
    succes_url = '/products/'
    fields = ['name', 'sizes', 'price', 'price_old', 'id', 'delivery', 'kids',
              'kid_adult', 'free_porto', 'package', 'women', 'url', 'img_url']
    
    def form_valid(self, form):
        production.objects.create(**form.cleaned_data)
        return HttpResponseRedirect('/products/')


def selection(request):
    results = production.objects.all()
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


def search_look(request):
    # Get the context from the request.
    context = RequestContext(request)

    # A HTTP POST?
    if request.method == 'POST':
        form = search_form(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return selection(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print(form.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        form = search_form()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render_to_response('products/search_form.html', {'form': form}, context)