from products.forms import ProdSearchForm


def search_form(request):
    return {'search_form': ProdSearchForm}