'''import datetime

from django.utils import timezone
from django.test import TestCase

from friends_mapping.models import friend

class FriendMethodTests(TestCase):

    def test_was_met_recently_with_future_friend(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is in the future
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_friend = friend_(meeting_date = time)
        self.assertEqual(future_friend.was_met_recently(), False)
'''
