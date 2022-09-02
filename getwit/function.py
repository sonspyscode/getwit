import webbrowser

import requests_oauthlib
from requests_oauthlib import OAuth1Session
import json
from getwit import model
from getwit import api_secret
import requests
# from urllib import parse
# import base64
# import hashlib
# import re
# import os
# from requests_oauthlib import OAuth2Session

consumer_key = api_secret.CONSUMER_KEY
consumer_secret = api_secret.CONSUMER_SECRET
bearer_token = api_secret.BEARER_TOKEN
client_id = api_secret.CLIENT_ID
redirect_uri = api_secret.CALLBACK_URL
headers = {"Authorization": "Bearer {}".format(bearer_token)}

#TWEETS
def get_tweet_lookup(tweet_ids):
    request_token_url = "https://api.twitter.com/oauth/request_token"
    oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

    try:
        fetch_response = oauth.fetch_request_token(request_token_url)
    except ValueError:
        print(
            "There may have been an issue with the consumer_key or consumer_secret you entered."
        )

    resource_owner_key = fetch_response.get("oauth_token")
    resource_owner_secret = fetch_response.get("oauth_token_secret")
    print("Got OAuth token: %s" % resource_owner_key)

    # Get authorization
    base_authorization_url = "https://api.twitter.com/oauth/authorize"
    authorization_url = oauth.authorization_url(base_authorization_url)
    # print("Click this link and authorize: %s" % authorization_url)
    webbrowser.open(authorization_url)
    verifier = input("Paste the oauth_verifier here: ")

    # Get the access token
    access_token_url = "https://api.twitter.com/oauth/access_token"
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=resource_owner_key,
        resource_owner_secret=resource_owner_secret,
        verifier=verifier,
    )
    oauth_tokens = oauth.fetch_access_token(access_token_url)


    access_token = oauth_tokens["oauth_token"]
    access_token_secret = oauth_tokens["oauth_token_secret"]

    # Make the request
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
    )

    params = model.get_tweet_par(tweet_ids)
    response = oauth.get(
        "https://api.twitter.com/2/tweets", params=params
    )

    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(response.status_code, response.text)
        )


    print("Response code: {}".format(response.status_code))
    json_response = response.json()
    with open("databank/tweet_lookup.json", "w") as file:
        json.dump(json_response, file, indent=4, sort_keys=True)

def get_tweet_by(tweet_id):
    request_token_url = "https://api.twitter.com/oauth/request_token"
    oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

    try:
        fetch_response = oauth.fetch_request_token(request_token_url)
    except ValueError:
        print(
            "There may have been an issue with the consumer_key or consumer_secret you entered."
        )

    resource_owner_key = fetch_response.get("oauth_token")
    resource_owner_secret = fetch_response.get("oauth_token_secret")
    print("Got OAuth token: %s" % resource_owner_key)

    # Get authorization
    base_authorization_url = "https://api.twitter.com/oauth/authorize"
    authorization_url = oauth.authorization_url(base_authorization_url)
    # print("Please go here and authorize: %s" % authorization_url)
    webbrowser.open(authorization_url)
    verifier = input("Paste the oauth_verifier here: ")

    # Get the access token
    access_token_url = "https://api.twitter.com/oauth/access_token"
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=resource_owner_key,
        resource_owner_secret=resource_owner_secret,
        verifier=verifier,
    )
    oauth_tokens = oauth.fetch_access_token(access_token_url)


    access_token = oauth_tokens["oauth_token"]
    access_token_secret = oauth_tokens["oauth_token_secret"]

    # Make the request
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
    )

    params = model.get_tweet_by_par()
    response = oauth.get(
        "https://api.twitter.com/2/tweets/{}".format(tweet_id), params=params
    )

    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(response.status_code, response.text)
        )

    print("Response code: {}".format(response.status_code))
    json_response = response.json()
    with open("databank/tweet_by.json", "w") as file:
        json.dump(json_response, file, indent=4, sort_keys=True)

#LIKES
def get_likes_lookup(tweet_id, max_results, pagination_token):
    request_token_url = "https://api.twitter.com/oauth/request_token"
    oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

    try:
        fetch_response = oauth.fetch_request_token(request_token_url)
    except ValueError:
        print(
            "There may have been an issue with the consumer_key or consumer_secret you entered."
        )

    resource_owner_key = fetch_response.get("oauth_token")
    resource_owner_secret = fetch_response.get("oauth_token_secret")
    print("Got OAuth token: %s" % resource_owner_key)

    # Get authorization
    base_authorization_url = "https://api.twitter.com/oauth/authorize"
    authorization_url = oauth.authorization_url(base_authorization_url)
    # print("Please go here and authorize: %s" % authorization_url)
    webbrowser.open(authorization_url)
    verifier = input("Paste the oauth_verifier here: ")

    # Get the access token
    access_token_url = "https://api.twitter.com/oauth/access_token"
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=resource_owner_key,
        resource_owner_secret=resource_owner_secret,
        verifier=verifier,
    )
    oauth_tokens = oauth.fetch_access_token(access_token_url)

    access_token = oauth_tokens["oauth_token"]
    access_token_secret = oauth_tokens["oauth_token_secret"]

    # Make the request
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
    )

    params = model.get_likes_lookup_par(max_results, pagination_token)
    response = oauth.get(
        "https://api.twitter.com/2/tweets/{}/liking_users".format(tweet_id), params=params
    )

    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(response.status_code, response.text)
        )

    print("Response code: {}".format(response.status_code))
    json_response = response.json()
    with open("databank/likes_tweets.json", "w") as file:
        json.dump(json_response, file, indent=4, sort_keys=True)

def get_liked_tweets(user_id,max_results,pagination_token):
    request_token_url = "https://api.twitter.com/oauth/request_token"
    oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

    try:
        fetch_response = oauth.fetch_request_token(request_token_url)
    except ValueError:
        print(
            "There may have been an issue with the consumer_key or consumer_secret you entered."
        )

    resource_owner_key = fetch_response.get("oauth_token")
    resource_owner_secret = fetch_response.get("oauth_token_secret")
    print("Got OAuth token: %s" % resource_owner_key)

    # Get authorization
    base_authorization_url = "https://api.twitter.com/oauth/authorize"
    authorization_url = oauth.authorization_url(base_authorization_url)
    # print("Please go here and authorize: %s" % authorization_url)
    webbrowser.open(authorization_url)
    verifier = input("Paste the oauth_verifier here: ")

    # Get the access token
    access_token_url = "https://api.twitter.com/oauth/access_token"
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=resource_owner_key,
        resource_owner_secret=resource_owner_secret,
        verifier=verifier,
    )
    oauth_tokens = oauth.fetch_access_token(access_token_url)

    access_token = oauth_tokens["oauth_token"]
    access_token_secret = oauth_tokens["oauth_token_secret"]

    # Make the request
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
    )

    params = model.get_liked_tweets_par(max_results,pagination_token)
    response = oauth.get(
        "https://api.twitter.com/2/users/{}/liked_tweets".format(user_id), params=params
    )

    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(response.status_code, response.text)
        )

    print("Response code: {}".format(response.status_code))
    json_response = response.json()
    with open("databank/liked_tweets.json", "w") as file:
        json.dump(json_response, file, indent=4, sort_keys=True)

#TIMELINE
def get_user_timeline(user_id):
    request_token_url = "https://api.twitter.com/oauth/request_token"
    oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

    try:
        fetch_response = oauth.fetch_request_token(request_token_url)
    except ValueError:
        print(
            "There may have been an issue with the consumer_key or consumer_secret you entered."
        )

    resource_owner_key = fetch_response.get("oauth_token")
    resource_owner_secret = fetch_response.get("oauth_token_secret")
    print("Got OAuth token: %s" % resource_owner_key)

    # Get authorization
    base_authorization_url = "https://api.twitter.com/oauth/authorize"
    authorization_url = oauth.authorization_url(base_authorization_url)
    # print("Please go here and authorize: %s" % authorization_url)
    webbrowser.open(authorization_url)
    verifier = input("Paste the oauth_verifier here: ")

    # Get the access token
    access_token_url = "https://api.twitter.com/oauth/access_token"
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=resource_owner_key,
        resource_owner_secret=resource_owner_secret,
        verifier=verifier,
    )
    oauth_tokens = oauth.fetch_access_token(access_token_url)

    access_token = oauth_tokens["oauth_token"]
    access_token_secret = oauth_tokens["oauth_token_secret"]

    # Make the request
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
    )

    params = model.get_user_timeline_par()
    response = oauth.get(
        "https://api.twitter.com/2/users/{}/tweets".format(user_id), params=params
    )

    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(response.status_code, response.text)
        )

    print("Response code: {}".format(response.status_code))
    json_response = response.json()
    with open("databank/user_timeline.json", "w") as file:
        json.dump(json_response, file, indent=4, sort_keys=True)

def get_user_mention_timeline(user_id):
    request_token_url = "https://api.twitter.com/oauth/request_token"
    oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

    try:
        fetch_response = oauth.fetch_request_token(request_token_url)
    except ValueError:
        print(
            "There may have been an issue with the consumer_key or consumer_secret you entered."
        )

    resource_owner_key = fetch_response.get("oauth_token")
    resource_owner_secret = fetch_response.get("oauth_token_secret")
    print("Got OAuth token: %s" % resource_owner_key)

    # Get authorization
    base_authorization_url = "https://api.twitter.com/oauth/authorize"
    authorization_url = oauth.authorization_url(base_authorization_url)
    # print("Please go here and authorize: %s" % authorization_url)
    webbrowser.open(authorization_url)
    verifier = input("Paste the oauth_verifier here: ")

    # Get the access token
    access_token_url = "https://api.twitter.com/oauth/access_token"
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=resource_owner_key,
        resource_owner_secret=resource_owner_secret,
        verifier=verifier,
    )
    oauth_tokens = oauth.fetch_access_token(access_token_url)

    access_token = oauth_tokens["oauth_token"]
    access_token_secret = oauth_tokens["oauth_token_secret"]

    # Make the request
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
    )

    params = model.get_user_mention_timeline_par()
    response = oauth.get(
        "https://api.twitter.com/2/users/{}/mentions".format(user_id), params=params
    )

    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(response.status_code, response.text)
        )

    print("Response code: {}".format(response.status_code))
    json_response = response.json()
    with open("databank/user_mention_timeline.json", "w") as file:
        json.dump(json_response, file, indent=4, sort_keys=True)

#USERS
def get_user_lookup_by(usernames):
    url = 'https://api.twitter.com/2/users/by'.format(usernames)
    params = model.get_user_lookup_by_par(usernames)
    respon = requests.request("GET", url, headers=headers, params=params)
    print(respon.status_code)
    for response_line in respon.iter_lines():
        if response_line:
            json_response = json.loads(response_line)
            with open("databank/user_lookup_by.json", "w") as file:
                json.dump(json_response, file, indent=4, sort_keys=True)
    if respon.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                respon.status_code, respon.text
            )
        )

def get_my_profile():
    request_token_url = "https://api.twitter.com/oauth/request_token"
    oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

    try:
        fetch_response = oauth.fetch_request_token(request_token_url)
    except ValueError:
        print(
            "There may have been an issue with the consumer_key or consumer_secret you entered."
        )

    resource_owner_key = fetch_response.get("oauth_token")
    resource_owner_secret = fetch_response.get("oauth_token_secret")
    print("Got OAuth token: %s" % resource_owner_key)

    # Get authorization
    base_authorization_url = "https://api.twitter.com/oauth/authorize"
    authorization_url = oauth.authorization_url(base_authorization_url)
    # print("Please go here and authorize: %s" % authorization_url)
    webbrowser.open(authorization_url)
    verifier = input("Paste the oauth_verifier here: ")

    # Get the access token
    access_token_url = "https://api.twitter.com/oauth/access_token"
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=resource_owner_key,
        resource_owner_secret=resource_owner_secret,
        verifier=verifier,
    )
    oauth_tokens = oauth.fetch_access_token(access_token_url)

    access_token = oauth_tokens["oauth_token"]
    access_token_secret = oauth_tokens["oauth_token_secret"]

    # Make the request
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
    )

    params = model.get_my_par()
    response = oauth.get(
        "https://api.twitter.com/2/users/me", params=params
    )

    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(response.status_code, response.text)
        )

    print("Response code: {}".format(response.status_code))
    json_response = response.json()
    with open("databank/my_profile.json", "w") as file:
        json.dump(json_response, file, indent=4, sort_keys=True)

def get_user_lookup_by_username(username):
    url = 'https://api.twitter.com/2/users/by/username/{}'.format(username)
    params = model.get_user_lookup_by_username_par()
    respon = requests.request("GET", url, headers=headers, params=params)
    print(respon.status_code)
    for response_line in respon.iter_lines():
        if response_line:
            json_response = json.loads(response_line)
            with open("databank/user_lookup_by.json", "w") as file:
                json.dump(json_response, file, indent=4, sort_keys=True)
    if respon.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                respon.status_code, respon.text
            )
        )

def get_users_lookup(user_ids):
    request_token_url = "https://api.twitter.com/oauth/request_token"
    oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

    try:
        fetch_response = oauth.fetch_request_token(request_token_url)
    except ValueError:
        print(
            "There may have been an issue with the consumer_key or consumer_secret you entered."
        )

    resource_owner_key = fetch_response.get("oauth_token")
    resource_owner_secret = fetch_response.get("oauth_token_secret")
    print("Got OAuth token: %s" % resource_owner_key)

    # Get authorization
    base_authorization_url = "https://api.twitter.com/oauth/authorize"
    authorization_url = oauth.authorization_url(base_authorization_url)
    # print("Please go here and authorize: %s" % authorization_url)
    webbrowser.open(authorization_url)
    verifier = input("Paste the oauth_verifier here: ")

    # Get the access token
    access_token_url = "https://api.twitter.com/oauth/access_token"
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=resource_owner_key,
        resource_owner_secret=resource_owner_secret,
        verifier=verifier,
    )
    oauth_tokens = oauth.fetch_access_token(access_token_url)

    access_token = oauth_tokens["oauth_token"]
    access_token_secret = oauth_tokens["oauth_token_secret"]

    # Make the request
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
    )

    params = model.get_users_lookup_par(user_ids)
    response = oauth.get(
        "https://api.twitter.com/2/users", params=params
    )

    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(response.status_code, response.text)
        )

    print("Response code: {}".format(response.status_code))
    json_response = response.json()
    with open("databank/users_lookup.json", "w") as file:
        json.dump(json_response, file, indent=4, sort_keys=True)

def get_user_lookup_by_id(user_id):
    request_token_url = "https://api.twitter.com/oauth/request_token"
    oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

    try:
        fetch_response = oauth.fetch_request_token(request_token_url)
    except ValueError:
        print(
            "There may have been an issue with the consumer_key or consumer_secret you entered."
        )

    resource_owner_key = fetch_response.get("oauth_token")
    resource_owner_secret = fetch_response.get("oauth_token_secret")
    print("Got OAuth token: %s" % resource_owner_key)

    # Get authorization
    base_authorization_url = "https://api.twitter.com/oauth/authorize"
    authorization_url = oauth.authorization_url(base_authorization_url)
    # print("Please go here and authorize: %s" % authorization_url)
    webbrowser.open(authorization_url)
    verifier = input("Paste the oauth_verifier here: ")

    # Get the access token
    access_token_url = "https://api.twitter.com/oauth/access_token"
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=resource_owner_key,
        resource_owner_secret=resource_owner_secret,
        verifier=verifier,
    )
    oauth_tokens = oauth.fetch_access_token(access_token_url)

    access_token = oauth_tokens["oauth_token"]
    access_token_secret = oauth_tokens["oauth_token_secret"]

    # Make the request
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
    )

    params = model.get_user_lookup_by_id_par()
    response = oauth.get(
        "https://api.twitter.com/2/users/{}".format(user_id), params=params
    )

    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(response.status_code, response.text)
        )

    print("Response code: {}".format(response.status_code))
    json_response = response.json()
    with open("databank/user_lookup_by_id.json", "w") as file:
        json.dump(json_response, file, indent=4, sort_keys=True)

#SPACES
def get_space_lookup(space_id):
    request_token_url = "https://api.twitter.com/oauth/request_token"
    oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

    try:
        fetch_response = oauth.fetch_request_token(request_token_url)
    except ValueError:
        print(
            "There may have been an issue with the consumer_key or consumer_secret you entered."
        )

    resource_owner_key = fetch_response.get("oauth_token")
    resource_owner_secret = fetch_response.get("oauth_token_secret")
    print("Got OAuth token: %s" % resource_owner_key)

    # Get authorization
    base_authorization_url = "https://api.twitter.com/oauth/authorize"
    authorization_url = oauth.authorization_url(base_authorization_url)
    # print("Please go here and authorize: %s" % authorization_url)
    webbrowser.open(authorization_url)
    verifier = input("Paste the oauth_verifier here: ")

    # Get the access token
    access_token_url = "https://api.twitter.com/oauth/access_token"
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=resource_owner_key,
        resource_owner_secret=resource_owner_secret,
        verifier=verifier,
    )
    oauth_tokens = oauth.fetch_access_token(access_token_url)

    access_token = oauth_tokens["oauth_token"]
    access_token_secret = oauth_tokens["oauth_token_secret"]

    # Make the request
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
    )

    params = model.get_spaces_by_id_par(space_id)
    response = oauth.get(
        "https://api.twitter.com/2/spaces/".format(space_id), params=params
    )

    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(response.status_code, response.text)
        )

    print("Response code: {}".format(response.status_code))
    json_response = response.json()
    with open("databank/space_lookup.json", "w") as file:
        json.dump(json_response, file, indent=4, sort_keys=True)

def get_search_space(str_query,state):
    url = 'https://api.twitter.com/2/spaces/search'.format(str_query)
    params = model.get_search_space_par(str_query,state)
    respon = requests.request("GET", url, headers=headers, params=params)
    print(respon.status_code)
    for response_line in respon.iter_lines():
        if response_line:
            json_response = json.loads(response_line)
            with open("databank/search_space.json", "w") as file:
                json.dump(json_response, file,  indent=4, sort_keys=True)
            # print(json.dumps(json_response, indent=4, sort_keys=True))
    if respon.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                respon.status_code, respon.text
            )
        )

def get_spaces(space_ids):
    request_token_url = "https://api.twitter.com/oauth/request_token"
    oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

    try:
        fetch_response = oauth.fetch_request_token(request_token_url)
    except ValueError:
        print(
            "There may have been an issue with the consumer_key or consumer_secret you entered."
        )

    resource_owner_key = fetch_response.get("oauth_token")
    resource_owner_secret = fetch_response.get("oauth_token_secret")
    print("Got OAuth token: %s" % resource_owner_key)

    # Get authorization
    base_authorization_url = "https://api.twitter.com/oauth/authorize"
    authorization_url = oauth.authorization_url(base_authorization_url)
    # print("Please go here and authorize: %s" % authorization_url)
    webbrowser.open(authorization_url)
    verifier = input("Paste the oauth_verifier here: ")

    # Get the access token
    access_token_url = "https://api.twitter.com/oauth/access_token"
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=resource_owner_key,
        resource_owner_secret=resource_owner_secret,
        verifier=verifier,
    )
    oauth_tokens = oauth.fetch_access_token(access_token_url)

    access_token = oauth_tokens["oauth_token"]
    access_token_secret = oauth_tokens["oauth_token_secret"]

    # Make the request
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
    )

    params = model.get_spaces_par(space_ids)
    response = oauth.get(
        'https://api.twitter.com/2/spaces', params=params
    )

    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(response.status_code, response.text)
        )

    print("Response code: {}".format(response.status_code))
    json_response = response.json()
    with open("databank/spaces_lookup.json", "w") as file:
        json.dump(json_response, file, indent=4, sort_keys=True)

def get_spaces_by_creator_ids(user_ids):
    request_token_url = "https://api.twitter.com/oauth/request_token"
    oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

    try:
        fetch_response = oauth.fetch_request_token(request_token_url)
    except ValueError:
        print(
            "There may have been an issue with the consumer_key or consumer_secret you entered."
        )

    resource_owner_key = fetch_response.get("oauth_token")
    resource_owner_secret = fetch_response.get("oauth_token_secret")
    print("Got OAuth token: %s" % resource_owner_key)

    # Get authorization
    base_authorization_url = "https://api.twitter.com/oauth/authorize"
    authorization_url = oauth.authorization_url(base_authorization_url)
    # print("Please go here and authorize: %s" % authorization_url)
    webbrowser.open(authorization_url)
    verifier = input("Paste the oauth_verifier here: ")

    # Get the access token
    access_token_url = "https://api.twitter.com/oauth/access_token"
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=resource_owner_key,
        resource_owner_secret=resource_owner_secret,
        verifier=verifier,
    )
    oauth_tokens = oauth.fetch_access_token(access_token_url)

    access_token = oauth_tokens["oauth_token"]
    access_token_secret = oauth_tokens["oauth_token_secret"]

    # Make the request
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
    )

    params = model.get_spaces_by_creator_ids_par(user_ids)
    response = oauth.get(
        'https://api.twitter.com/2/spaces/by/creator_ids'.format(user_ids), params=params
    )

    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(response.status_code, response.text)
        )

    print("Response code: {}".format(response.status_code))
    json_response = response.json()
    with open("databank/spaces_by_creator_id.json", "w") as file:
        json.dump(json_response, file, indent=4, sort_keys=True)

#OAuth2.0 Autorization Code with PKCE
# def get_spaces_buyers(space_id):
#     url = 'https://api.twitter.com/2/spaces/{}/buyers'.format(space_id)
#     params = model.get_spaces_buyers()
#     respon = requests.request("GET", url, headers=headers, params=params)
#     print(respon.status_code)
#     for response_line in respon.iter_lines():
#         if response_line:
#             json_response = json.loads(response_line)
#             print(json.dumps(json_response, indent=4, sort_keys=True))
#     if respon.status_code != 200:
#         raise Exception(
#             "Request returned an error: {} {}".format(
#                 respon.status_code, respon.text
#             )
#         )
#
# def get_spaces_tweet(space_id):
#     url = 'https://api.twitter.com/2/spaces/:id/tweets'.format(space_id)
#     params = model.get_search_space_par(space_id)
#     respon = requests.request("GET", url, headers=headers, params=params)
#     print(respon.status_code)
#     for response_line in respon.iter_lines():
#         if response_line:
#             json_response = json.loads(response_line)
#             print(json.dumps(json_response, indent=4, sort_keys=True))
#     if respon.status_code != 200:
#         raise Exception(
#             "Request returned an error: {} {}".format(
#                 respon.status_code, respon.text
#             )
#         )

#VOLUME STREAMS

def get_sample_stream():
    param = model.sample_stream_par()
    headers = {"Authorization": "Bearer {}".format(bearer_token),
               "User-Agent": "v2SampleStreamJS"}
    url = 'https://api.twitter.com/2/tweets/sample/stream'
    respon = requests.request("GET", url, params= param, headers=headers, stream=True)
    print(respon.status_code)
    for response_line in respon.iter_lines():
        if response_line:
            json_response = json.loads(response_line)
            print(json.dumps(json_response, indent=4, sort_keys=True))
    if respon.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                respon.status_code, respon.text
            )
        )

#RETWEETS
def get_retweets_lookup(tweet_id, pagination_token):
    request_token_url = "https://api.twitter.com/oauth/request_token"
    oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

    try:
        fetch_response = oauth.fetch_request_token(request_token_url)
    except ValueError:
        print(
            "There may have been an issue with the consumer_key or consumer_secret you entered."
        )

    resource_owner_key = fetch_response.get("oauth_token")
    resource_owner_secret = fetch_response.get("oauth_token_secret")
    print("Got OAuth token: %s" % resource_owner_key)

    # Get authorization
    base_authorization_url = "https://api.twitter.com/oauth/authorize"
    authorization_url = oauth.authorization_url(base_authorization_url)
    # print("Please go here and authorize: %s" % authorization_url)
    webbrowser.open(authorization_url)
    verifier = input("Paste the oauth_verifier here: ")

    # Get the access token
    access_token_url = "https://api.twitter.com/oauth/access_token"
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=resource_owner_key,
        resource_owner_secret=resource_owner_secret,
        verifier=verifier,
    )
    oauth_tokens = oauth.fetch_access_token(access_token_url)

    access_token = oauth_tokens["oauth_token"]
    access_token_secret = oauth_tokens["oauth_token_secret"]

    # Make the request
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
    )

    params = model.get_retweets_lookup_par(pagination_token)
    response = oauth.get(
        "https://api.twitter.com/2/tweets/{}/retweeted_by".format(tweet_id), params=params
    )

    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(response.status_code, response.text)
        )

    print("Response code: {}".format(response.status_code))
    json_response = response.json()
    with open("databank/retweets_lookup.json", "w") as file:
        json.dump(json_response, file, indent=4, sort_keys=True)

#SEARCH TWEETS
def get_recent_tweet_count(str_query, end_time, granularity, since_id, start_time, until_id):
    url = "https://api.twitter.com/2/tweets/counts/recent".format(str_query)
    params = model.get_recent_tweet_count_par(str_query, end_time, granularity, since_id, start_time, until_id)
    respon = requests.request("GET", url, headers=headers, params=params)
    print(respon.status_code)
    for response_line in respon.iter_lines():
        if response_line:
            json_response = json.loads(response_line)
            with open("databank/recent_tweet_count.json", "w") as file:
                json.dump(json_response, file, indent=4, sort_keys=True)
    if respon.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                respon.status_code, respon.text
            )
        )

def get_recent_search(str_query, end_time, max_results, next_token, since_id, start_time, until_id):
    url = "https://api.twitter.com/2/tweets/search/recent".format(str_query)
    params = model.get_recent_search_par(str_query, end_time, max_results, next_token, since_id, start_time, until_id)
    respon = requests.request("GET", url, headers=headers, params=params)
    print(respon.status_code)
    for response_line in respon.iter_lines():
        if response_line:
            json_response = json.loads(response_line)
            with open("databank/recent_search.json", "w") as file:
                json.dump(json_response, file, indent=4, sort_keys=True)
    if respon.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                respon.status_code, respon.text
            )
        )

#QUOTE TWEETS
def get_quote_tweet(tweet_id, max_results, pagination_token):
    request_token_url = "https://api.twitter.com/oauth/request_token"
    oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

    try:
        fetch_response = oauth.fetch_request_token(request_token_url)
    except ValueError:
        print(
            "There may have been an issue with the consumer_key or consumer_secret you entered."
        )

    resource_owner_key = fetch_response.get("oauth_token")
    resource_owner_secret = fetch_response.get("oauth_token_secret")
    print("Got OAuth token: %s" % resource_owner_key)

    # Get authorization
    base_authorization_url = "https://api.twitter.com/oauth/authorize"
    authorization_url = oauth.authorization_url(base_authorization_url)
    # print("Please go here and authorize: %s" % authorization_url)
    webbrowser.open(authorization_url)
    verifier = input("Paste the oauth_verifier here: ")

    # Get the access token
    access_token_url = "https://api.twitter.com/oauth/access_token"
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=resource_owner_key,
        resource_owner_secret=resource_owner_secret,
        verifier=verifier,
    )
    oauth_tokens = oauth.fetch_access_token(access_token_url)

    access_token = oauth_tokens["oauth_token"]
    access_token_secret = oauth_tokens["oauth_token_secret"]

    # Make the request
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
    )

    params = model.get_quote_tweet_par(max_results, pagination_token)
    response = oauth.get(
        "https://api.twitter.com/2/tweets/{}/quote_tweets".format(tweet_id)
    )

    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(response.status_code, response.text)
        )

    print("Response code: {}".format(response.status_code))
    json_response = response.json()
    with open("databank/quote_tweets.json", "w") as file:
        json.dump(json_response, file, indent=4, sort_keys=True)

#MUTES
def get_mutes_lookup(user_id, max_results, pagination_token):
    request_token_url = "https://api.twitter.com/oauth/request_token"
    oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

    try:
        fetch_response = oauth.fetch_request_token(request_token_url)
    except ValueError:
        print(
            "There may have been an issue with the consumer_key or consumer_secret you entered."
        )

    resource_owner_key = fetch_response.get("oauth_token")
    resource_owner_secret = fetch_response.get("oauth_token_secret")
    print("Got OAuth token: %s" % resource_owner_key)

    # Get authorization
    base_authorization_url = "https://api.twitter.com/oauth/authorize"
    authorization_url = oauth.authorization_url(base_authorization_url)
    # print("Please go here and authorize: %s" % authorization_url)
    webbrowser.open(authorization_url)
    verifier = input("Paste the oauth_verifier here: ")

    # Get the access token
    access_token_url = "https://api.twitter.com/oauth/access_token"
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=resource_owner_key,
        resource_owner_secret=resource_owner_secret,
        verifier=verifier,
    )
    oauth_tokens = oauth.fetch_access_token(access_token_url)

    access_token = oauth_tokens["oauth_token"]
    access_token_secret = oauth_tokens["oauth_token_secret"]

    # Make the request
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
    )

    params = model.get_mutes_lookup_par(max_results, pagination_token)
    response = oauth.get(
        "https://api.twitter.com/2/users/{}/muting".format(user_id), params=params
    )

    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(response.status_code, response.text)
        )

    print("Response code: {}".format(response.status_code))
    json_response = response.json()
    with open("databank/mutes_lookup.json", "w") as file:
        json.dump(json_response, file, indent=4, sort_keys=True)

#LIST
def user_owned_list(user_id,max_results,pagination_token):
    request_token_url = "https://api.twitter.com/oauth/request_token"
    oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

    try:
        fetch_response = oauth.fetch_request_token(request_token_url)
    except ValueError:
        print(
            "There may have been an issue with the consumer_key or consumer_secret you entered."
        )

    resource_owner_key = fetch_response.get("oauth_token")
    resource_owner_secret = fetch_response.get("oauth_token_secret")
    print("Got OAuth token: %s" % resource_owner_key)

    # Get authorization
    base_authorization_url = "https://api.twitter.com/oauth/authorize"
    authorization_url = oauth.authorization_url(base_authorization_url)
    # print("Please go here and authorize: %s" % authorization_url)
    webbrowser.open(authorization_url)
    verifier = input("Paste the oauth_verifier here: ")

    # Get the access token
    access_token_url = "https://api.twitter.com/oauth/access_token"
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=resource_owner_key,
        resource_owner_secret=resource_owner_secret,
        verifier=verifier,
    )
    oauth_tokens = oauth.fetch_access_token(access_token_url)

    access_token = oauth_tokens["oauth_token"]
    access_token_secret = oauth_tokens["oauth_token_secret"]

    # Make the request
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
    )

    params = model.user_owned_list(max_results,pagination_token)
    response = oauth.get(
        "https://api.twitter.com/2/users/{}/owned_lists".format(user_id), params=params
    )

    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(response.status_code, response.text)
        )

    print("Response code: {}".format(response.status_code))
    json_response = response.json()
    with open("databank/user_owned_list.json", "w") as file:
        json.dump(json_response, file, indent=4, sort_keys=True)

def get_list_lookup(list_id):
    request_token_url = "https://api.twitter.com/oauth/request_token"
    oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

    try:
        fetch_response = oauth.fetch_request_token(request_token_url)
    except ValueError:
        print(
            "There may have been an issue with the consumer_key or consumer_secret you entered."
        )

    resource_owner_key = fetch_response.get("oauth_token")
    resource_owner_secret = fetch_response.get("oauth_token_secret")
    print("Got OAuth token: %s" % resource_owner_key)

    # Get authorization
    base_authorization_url = "https://api.twitter.com/oauth/authorize"
    authorization_url = oauth.authorization_url(base_authorization_url)
    # print("Please go here and authorize: %s" % authorization_url)
    webbrowser.open(authorization_url)
    verifier = input("Paste the oauth_verifier here: ")

    # Get the access token
    access_token_url = "https://api.twitter.com/oauth/access_token"
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=resource_owner_key,
        resource_owner_secret=resource_owner_secret,
        verifier=verifier,
    )
    oauth_tokens = oauth.fetch_access_token(access_token_url)

    access_token = oauth_tokens["oauth_token"]
    access_token_secret = oauth_tokens["oauth_token_secret"]

    # Make the request
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
    )

    params = model.get_list_lookup_par()
    response = oauth.get(
                "https://api.twitter.com/2/lists/{}".format(list_id), params=params
    )

    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(response.status_code, response.text)
        )

    print("Response code: {}".format(response.status_code))
    json_response = response.json()
    with open("databank/list_lookup.json", "w") as file:
        json.dump(json_response, file, indent=4, sort_keys=True)

def get_pinned_list(user_id):
    request_token_url = "https://api.twitter.com/oauth/request_token"
    oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

    try:
        fetch_response = oauth.fetch_request_token(request_token_url)
    except ValueError:
        print(
            "There may have been an issue with the consumer_key or consumer_secret you entered."
        )

    resource_owner_key = fetch_response.get("oauth_token")
    resource_owner_secret = fetch_response.get("oauth_token_secret")
    print("Got OAuth token: %s" % resource_owner_key)

    # Get authorization
    base_authorization_url = "https://api.twitter.com/oauth/authorize"
    authorization_url = oauth.authorization_url(base_authorization_url)
    # print("Please go here and authorize: %s" % authorization_url)
    webbrowser.open(authorization_url)
    verifier = input("Paste the oauth_verifier here: ")

    # Get the access token
    access_token_url = "https://api.twitter.com/oauth/access_token"
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=resource_owner_key,
        resource_owner_secret=resource_owner_secret,
        verifier=verifier,
    )
    oauth_tokens = oauth.fetch_access_token(access_token_url)

    access_token = oauth_tokens["oauth_token"]
    access_token_secret = oauth_tokens["oauth_token_secret"]

    # Make the request
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
    )

    params = model.get_pinned_list_par()
    response = oauth.get(
        "https://api.twitter.com/2/users/{}/pinned_lists".format(user_id), params=params
    )

    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(response.status_code, response.text)
        )

    print("Response code: {}".format(response.status_code))
    json_response = response.json()
    with open("databank/pinned_list.json", "w") as file:
        json.dump(json_response, file, indent=4, sort_keys=True)

def get_user_list_memberships(user_id,max_results, pagination_token):
    request_token_url = "https://api.twitter.com/oauth/request_token"
    oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

    try:
        fetch_response = oauth.fetch_request_token(request_token_url)
    except ValueError:
        print(
            "There may have been an issue with the consumer_key or consumer_secret you entered."
        )

    resource_owner_key = fetch_response.get("oauth_token")
    resource_owner_secret = fetch_response.get("oauth_token_secret")
    print("Got OAuth token: %s" % resource_owner_key)

    # Get authorization
    base_authorization_url = "https://api.twitter.com/oauth/authorize"
    authorization_url = oauth.authorization_url(base_authorization_url)
    # print("Please go here and authorize: %s" % authorization_url)
    webbrowser.open(authorization_url)
    verifier = input("Paste the oauth_verifier here: ")

    # Get the access token
    access_token_url = "https://api.twitter.com/oauth/access_token"
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=resource_owner_key,
        resource_owner_secret=resource_owner_secret,
        verifier=verifier,
    )
    oauth_tokens = oauth.fetch_access_token(access_token_url)

    access_token = oauth_tokens["oauth_token"]
    access_token_secret = oauth_tokens["oauth_token_secret"]

    # Make the request
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
    )

    params = model.get_list_membership_par(max_results, pagination_token)
    response = oauth.get(
        "https://api.twitter.com/2/users/{}/list_memberships".format(user_id), params=params
    )

    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(response.status_code, response.text)
        )

    print("Response code: {}".format(response.status_code))
    json_response = response.json()
    with open("databank/user_list_membership.json", "w") as file:
        json.dump(json_response, file, indent=4, sort_keys=True)

def get_list_member_lookup(list_id, max_results, pagination_token):
    request_token_url = "https://api.twitter.com/oauth/request_token"
    oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

    try:
        fetch_response = oauth.fetch_request_token(request_token_url)
    except ValueError:
        print(
            "There may have been an issue with the consumer_key or consumer_secret you entered."
        )

    resource_owner_key = fetch_response.get("oauth_token")
    resource_owner_secret = fetch_response.get("oauth_token_secret")
    print("Got OAuth token: %s" % resource_owner_key)

    # Get authorization
    base_authorization_url = "https://api.twitter.com/oauth/authorize"
    authorization_url = oauth.authorization_url(base_authorization_url)
    # print("Please go here and authorize: %s" % authorization_url)
    webbrowser.open(authorization_url)
    verifier = input("Paste the oauth_verifier here: ")

    # Get the access token
    access_token_url = "https://api.twitter.com/oauth/access_token"
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=resource_owner_key,
        resource_owner_secret=resource_owner_secret,
        verifier=verifier,
    )
    oauth_tokens = oauth.fetch_access_token(access_token_url)

    access_token = oauth_tokens["oauth_token"]
    access_token_secret = oauth_tokens["oauth_token_secret"]

    # Make the request
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
    )

    params = model.get_list_member_lookup_par(max_results, pagination_token)
    response = oauth.get(
        "https://api.twitter.com/2/lists/{}/members".format(list_id), params=params
    )

    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(response.status_code, response.text)
        )

    print("Response code: {}".format(response.status_code))
    json_response = response.json()
    with open("databank/list_member_lookup.json", "w") as file:
        json.dump(json_response, file, indent=4, sort_keys=True)

def get_user_list_followed(user_id,max_results,pagination_token):
    request_token_url = "https://api.twitter.com/oauth/request_token"
    oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

    try:
        fetch_response = oauth.fetch_request_token(request_token_url)
    except ValueError:
        print(
            "There may have been an issue with the consumer_key or consumer_secret you entered."
        )

    resource_owner_key = fetch_response.get("oauth_token")
    resource_owner_secret = fetch_response.get("oauth_token_secret")
    print("Got OAuth token: %s" % resource_owner_key)

    # Get authorization
    base_authorization_url = "https://api.twitter.com/oauth/authorize"
    authorization_url = oauth.authorization_url(base_authorization_url)
    # print("Please go here and authorize: %s" % authorization_url)
    webbrowser.open(authorization_url)
    verifier = input("Paste the oauth_verifier here: ")

    # Get the access token
    access_token_url = "https://api.twitter.com/oauth/access_token"
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=resource_owner_key,
        resource_owner_secret=resource_owner_secret,
        verifier=verifier,
    )
    oauth_tokens = oauth.fetch_access_token(access_token_url)

    access_token = oauth_tokens["oauth_token"]
    access_token_secret = oauth_tokens["oauth_token_secret"]

    # Make the request
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
    )

    params = model.get_user_list_followed_par(max_results,pagination_token)
    response = oauth.get(
        "https://api.twitter.com/2/users/{}/followed_lists".format(user_id), params=params
    )

    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(response.status_code, response.text)
        )

    print("Response code: {}".format(response.status_code))
    json_response = response.json()
    with open("databank/list_followed.json", "w") as file:
        json.dump(json_response, file, indent=4, sort_keys=True)

def get_list_followers_lookup(list_id, max_results, pagination_token):
    request_token_url = "https://api.twitter.com/oauth/request_token"
    oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

    try:
        fetch_response = oauth.fetch_request_token(request_token_url)
    except ValueError:
        print(
            "There may have been an issue with the consumer_key or consumer_secret you entered."
        )

    resource_owner_key = fetch_response.get("oauth_token")
    resource_owner_secret = fetch_response.get("oauth_token_secret")
    print("Got OAuth token: %s" % resource_owner_key)

    # Get authorization
    base_authorization_url = "https://api.twitter.com/oauth/authorize"
    authorization_url = oauth.authorization_url(base_authorization_url)
    # print("Please go here and authorize: %s" % authorization_url)
    webbrowser.open(authorization_url)
    verifier = input("Paste the oauth_verifier here: ")

    # Get the access token
    access_token_url = "https://api.twitter.com/oauth/access_token"
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=resource_owner_key,
        resource_owner_secret=resource_owner_secret,
        verifier=verifier,
    )
    oauth_tokens = oauth.fetch_access_token(access_token_url)

    access_token = oauth_tokens["oauth_token"]
    access_token_secret = oauth_tokens["oauth_token_secret"]

    # Make the request
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
    )

    params = model.get_list_followers_lookup(max_results, pagination_token)
    response = oauth.get(
        "https://api.twitter.com/2/lists/{}/followers".format(list_id), params=params
    )

    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(response.status_code, response.text)
        )

    print("Response code: {}".format(response.status_code))
    json_response = response.json()
    with open("databank/list_followers.json", "w") as file:
        json.dump(json_response, file, indent=4, sort_keys=True)

def get_list_tweets(list_id, max_results, pagination_token):
    request_token_url = "https://api.twitter.com/oauth/request_token"
    oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

    try:
        fetch_response = oauth.fetch_request_token(request_token_url)
    except ValueError:
        print(
            "There may have been an issue with the consumer_key or consumer_secret you entered."
        )

    resource_owner_key = fetch_response.get("oauth_token")
    resource_owner_secret = fetch_response.get("oauth_token_secret")
    print("Got OAuth token: %s" % resource_owner_key)

    # Get authorization
    base_authorization_url = "https://api.twitter.com/oauth/authorize"
    authorization_url = oauth.authorization_url(base_authorization_url)
    # print("Please go here and authorize: %s" % authorization_url)
    webbrowser.open(authorization_url)
    verifier = input("Paste the oauth_verifier here: ")

    # Get the access token
    access_token_url = "https://api.twitter.com/oauth/access_token"
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=resource_owner_key,
        resource_owner_secret=resource_owner_secret,
        verifier=verifier,
    )
    oauth_tokens = oauth.fetch_access_token(access_token_url)

    access_token = oauth_tokens["oauth_token"]
    access_token_secret = oauth_tokens["oauth_token_secret"]

    # Make the request
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
    )

    params = model.get_list_tweets_par(max_results, pagination_token)
    response = oauth.get(
        "https://api.twitter.com/2/lists/{}/tweets".format(list_id), params=params
    )

    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(response.status_code, response.text)
        )

    print("Response code: {}".format(response.status_code))
    json_response = response.json()
    with open("databank/list_tweets.json", "w") as file:
        json.dump(json_response, file, indent=4, sort_keys=True)

#FOLLOWS
def get_following_lookup(user_id, max_results, pagination_token):
    request_token_url = "https://api.twitter.com/oauth/request_token"
    oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

    try:
        fetch_response = oauth.fetch_request_token(request_token_url)
    except ValueError:
        print(
            "There may have been an issue with the consumer_key or consumer_secret you entered."
        )

    resource_owner_key = fetch_response.get("oauth_token")
    resource_owner_secret = fetch_response.get("oauth_token_secret")
    print("Got OAuth token: %s" % resource_owner_key)

    # Get authorization
    base_authorization_url = "https://api.twitter.com/oauth/authorize"
    authorization_url = oauth.authorization_url(base_authorization_url)
    # print("Please go here and authorize: %s" % authorization_url)
    webbrowser.open(authorization_url)
    verifier = input("Paste the oauth_verifier here: ")

    # Get the access token
    access_token_url = "https://api.twitter.com/oauth/access_token"
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=resource_owner_key,
        resource_owner_secret=resource_owner_secret,
        verifier=verifier,
    )
    oauth_tokens = oauth.fetch_access_token(access_token_url)

    access_token = oauth_tokens["oauth_token"]
    access_token_secret = oauth_tokens["oauth_token_secret"]

    # Make the request
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
    )

    params = model.get_following_lookup_par(max_results, pagination_token)
    response = oauth.get(
        "https://api.twitter.com/2/users/{}/following_lookup".format(user_id), params=params
    )

    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(response.status_code, response.text)
        )

    print("Response code: {}".format(response.status_code))
    json_response = response.json()
    with open("databank/following.json", "w") as file:
        json.dump(json_response, file, indent=4, sort_keys=True)

def get_followers_lookup(user_id, max_results, pagination_token):
    url = "https://api.twitter.com/2/users/{}/followers".format(user_id)
    params = model.get_followers_lookup_par(max_results, pagination_token)

    request_token_url = "https://api.twitter.com/oauth/request_token"
    oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

    try:
        fetch_response = oauth.fetch_request_token(request_token_url)
    except ValueError:
        print(
            "There may have been an issue with the consumer_key or consumer_secret you entered."
        )

    resource_owner_key = fetch_response.get("oauth_token")
    resource_owner_secret = fetch_response.get("oauth_token_secret")
    print("Got OAuth token: %s" % resource_owner_key)

    # Get authorization
    base_authorization_url = "https://api.twitter.com/oauth/authorize"
    authorization_url = oauth.authorization_url(base_authorization_url)
    # print("Please go here and authorize: %s" % authorization_url)
    webbrowser.open(authorization_url)
    verifier = input("Paste the oauth_verifier here: ")

    # Get the access token
    access_token_url = "https://api.twitter.com/oauth/access_token"
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=resource_owner_key,
        resource_owner_secret=resource_owner_secret,
        verifier=verifier,
    )
    oauth_tokens = oauth.fetch_access_token(access_token_url)

    access_token = oauth_tokens["oauth_token"]
    access_token_secret = oauth_tokens["oauth_token_secret"]

    # Make the request
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
    )

    params = model.get_followers_lookup_par(max_results, pagination_token)
    response = oauth.get(
        "https://api.twitter.com/2/users/{}/followers".format(user_id), params=params
    )

    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(response.status_code, response.text)
        )

    print("Response code: {}".format(response.status_code))
    json_response = response.json()
    with open("databank/followers_lookup.json", "w") as file:
        json.dump(json_response, file, indent=4, sort_keys=True)

#BLOCK
def get_block_lookup(user_id,max_results,pagination_token):
    request_token_url = "https://api.twitter.com/oauth/request_token"
    oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

    try:
        fetch_response = oauth.fetch_request_token(request_token_url)
    except ValueError:
        print(
            "There may have been an issue with the consumer_key or consumer_secret you entered."
        )

    resource_owner_key = fetch_response.get("oauth_token")
    resource_owner_secret = fetch_response.get("oauth_token_secret")
    print("Got OAuth token: %s" % resource_owner_key)

    # Get authorization
    base_authorization_url = "https://api.twitter.com/oauth/authorize"
    authorization_url = oauth.authorization_url(base_authorization_url)
    # print("Please go here and authorize: %s" % authorization_url)
    webbrowser.open(authorization_url)
    verifier = input("Paste the oauth_verifier here: ")

    # Get the access token
    access_token_url = "https://api.twitter.com/oauth/access_token"
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=resource_owner_key,
        resource_owner_secret=resource_owner_secret,
        verifier=verifier,
    )
    oauth_tokens = oauth.fetch_access_token(access_token_url)


    access_token = oauth_tokens["oauth_token"]
    access_token_secret = oauth_tokens["oauth_token_secret"]

    # Make the request
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
    )

    params = model.block_lookups_par(max_results,pagination_token)
    response = oauth.get(
        "https://api.twitter.com/2/users/{}/blocking".format(user_id), params=params
    )

    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(response.status_code, response.text)
        )

    print("Response code: {}".format(response.status_code))
    json_response = response.json()
    with open("databank/block_lookup.json", "w") as file:
        json.dump(json_response, file, indent=4, sort_keys=True)

#OAUTH 2.0 App-Only & end point full archive search Twitter v2 for academic research
#SEARCH TWEETS ALL
# def full_archive_search(str_query, max_results):
#     url = "https://api.twitter.com/2/tweets/search/all".format(str_query)
#     params = model.full_archive_search_par(str_query, max_results)
#     respon = requests.request("GET", url, headers=headers, params=params)
#     print(respon.status_code)
#     for response_line in respon.iter_lines():
#         if response_line:
#             json_response = json.loads(response_line)
#             print(json.dumps(json_response, indent=4, sort_keys=True))
#         if respon.status_code != 200:
#             raise Exception(
#                 "Request returned an error: {} {}".format(
#                     respon.status_code, respon.text
#                 )
#             )
#
# def full_archive_tweet_count(str_query):
#     url = "https://api.twitter.com/2/tweets/counts/all".format(str_query)
#     params = model.full_archive_tweet_count_par(str_query)
#     respon = requests.request("GET", url, headers=headers, params=params)
#     print(respon.status_code)
#     for response_line in respon.iter_lines():
#         if response_line:
#             json_response = json.loads(response_line)
#             print(json.dumps(json_response, indent=4, sort_keys=True))
#         if respon.status_code != 200:
#             raise Exception(
#                 "Request returned an error: {} {}".format(
#                     respon.status_code, respon.text
#                 )
#             )

#BOOKMARKS
# def bookmarks_lookup():
#     # Set the scopes
#     scopes = ["bookmark.read", "tweet.read", "users.read", "offline.access"]
#
#     # Create a code verifier
#     code_verifier = base64.urlsafe_b64encode(os.urandom(30)).decode("utf-8")
#     code_verifier = re.sub("[^a-zA-Z0-9]+", "", code_verifier)
#
#     # Create a code challenge
#     code_challenge = hashlib.sha256(code_verifier.encode("utf-8")).digest()
#     code_challenge = base64.urlsafe_b64encode(code_challenge).decode("utf-8")
#     code_challenge = code_challenge.replace("=", "")
#
#     # Start an OAuth 2.0 session
#     oauth = OAuth2Session(client_id, redirect_uri=redirect_uri, scope=scopes)
#
#     # Create an authorize URL
#     auth_url = "https://twitter.com/i/oauth2/authorize"
#     authorization_url, state = oauth.authorization_url(
#         auth_url, code_challenge=code_challenge, code_challenge_method="S256"
#     )
#
#     # Visit the URL to authorize your App to make requests on behalf of a user
#     print(
#         "Visit the following URL to authorize your App on behalf of your Twitter handle in a browser:"
#     )
#     print(authorization_url)
#
#     # Paste in your authorize URL to complete the request
#     authorization_response = input(
#         "Paste in the full URL after you've authorized your App:\n"
#     )
#
#     # Fetch your access token
#     token_url = "https://api.twitter.com/2/oauth2/token"
#
#     # The following line of code will only work if you are using a type of App that is a public client
#     auth = False
#
#     # If you are using a confidential client you will need to pass in basic encoding of your client ID and client secret.
#
#     # Please remove the comment on the following line if you are using a type of App that is a confidential client
#     # auth = HTTPBasicAuth(client_id, client_secret)
#
#     token = oauth.fetch_token(
#         token_url=token_url,
#         authorization_response=authorization_response,
#         auth=auth,
#         client_id=client_id,
#         include_client_id=True,
#         code_verifier=code_verifier,
#     )
#
#     # Your access token
#     access = token["access_token"]
#
#     # Make a request to the users/me endpoint to get your user ID
#     user_me = requests.request(
#         "GET",
#         "https://api.twitter.com/2/users/me",
#         headers={"Authorization": "Bearer {}".format(access)},
#     ).json()
#     user_id = user_me["data"]["id"]
#
#     # Make a request to the bookmarks url
#     url = "https://api.twitter.com/2/users/{}/bookmarks".format(user_id)
#     headers = {
#         "Authorization": "Bearer {}".format(access),
#         "User-Agent": "BookmarksSampleCode",
#     }
#     response = requests.request("GET", url, headers=headers)
#     if response.status_code != 200:
#         raise Exception(
#             "Request returned an error: {} {}".format(response.status_code, response.text)
#         )
#     print("Response code: {}".format(response.status_code))
#     json_response = response.json()
#     print(json.dumps(json_response, indent=4, sort_keys=True))

#BATCH COMPLIANCE
# def create_compliance_job():
#     params = model.create_compliance_job_par()
#     url = "https://api.twitter.com/2/compliance/jobs"
#     respon = requests.request("GET", url, headers=headers, json=params)
#     print(respon.status_code)
#     for response_line in respon.iter_lines():
#         if respon.status_code != 200:
#             raise Exception(respon.status_code, respon.text)
#         return respon.json()