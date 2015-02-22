from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic

from friends_mapping.models import friend, location


class IndexView(generic.ListView):
    template_name = 'friends_mapping/index.html'
    context_object_name = 'friends_list'

    def get_queryset(self):
        return friend.objects.order_by('-age')


class DetailView(generic.DetailView):
    model = friend
    template_name = 'friends_mapping/detail.html'


class ResultsView(generic.DetailView):
    model = friend
    template_name = 'friends_mapping/results.html'


def popularize(request, friend_id):
    local_friend = get_object_or_404(friend, pk = friend_id)
    try:
        selected_location = local_friend.location_set.get(pk = request.POST['location'])
    except (KeyError, location.DoesNotExist):
        # Redisplay the friend voting form.
        return render(request, 'friends_mapping/detail.html', {
            'friend': local_friend,
            'error_message': "You didn't select a location.",
        })
    else:
        selected_location.votes += 1
        selected_location.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('friends:results', args = (local_friend.id,)))
