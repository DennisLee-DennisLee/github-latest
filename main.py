import sys
import json

import requests

# Use Like python main.py JASchilz
# (or another user name)

if __name__ == "__main__":
    username = sys.argv[1]

    # Getting the timestamp for the first event for the user specified.
    # By first event, I'm interpreting that as the earliest event.
    # Since the events in the API response appear to be ordered from newest to
    # oldest, I'm picking out the timestamp for the event at the very end of the
    # JSON output. (Although it appears that the list of events is restricted
    # to a certain number and doesn't go to the very beginning of the user
    # history.)
    response = requests.get("https://api.github.com/users/{}/events".format(username))
    tstamp = response.json()[-1]['created_at']

    print(tstamp)
    


