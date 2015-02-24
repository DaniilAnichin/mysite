from products.forms import prod_search_form

def search_form(request):
    return {'search_form': prod_search_form()}