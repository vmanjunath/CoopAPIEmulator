__author__ = 'vikramm'
from models import UserData
import requests


# Settings that need to figured out from the Coop:
coop_shifts_url = "http://foodcoop.likescandy.com:8045/shift_exchange/shifts/"
# For now, we're working with naive datetime so even though the Coop sends us timezone aware ISO strings
# we strip the timezone. For the Coop this will be fine. But for future applications we'll have to address this.
datetime_format = "%Y-%m-%dT%H:%M:%S"
date_format = "%Y-%m-%d"


coop_post_url = "http://foodcoop.likescandy.com:8045/shift_exchange/registerSwaps"
#coop_post_url = "http://requestb.in/udh1hkud"


def fetch_member_dets(member_id):
    url = "%s%s" % (coop_shifts_url, member_id)
    resp = requests.get(url)
    return resp.json()
