from django import forms


class ProdSearchForm(forms.Form):
    # Search field
    q = forms.CharField(label='Type to find', max_length=100, required=False)
    # Highest price field
    hi = forms.IntegerField(label='Highest price limit', initial=10000,
                            min_value=0, required=False)
    # Lowest price field
    lo = forms.IntegerField(label='Lowest price limit', initial=1,
                            min_value=0, required=False)
    # Kids field
    k = forms.BooleanField(label='Include kids models?', required=False)
    # Adult field
    a = forms.BooleanField(label='Include teen models?', required=False)
    # Women field
    w = forms.BooleanField(label='Include women models?', required=False)