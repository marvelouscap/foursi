#EC GITHUB


import requests_oauthlib # use the pip method to get this
import webbrowser
import json


client_key = "cgNLneBYKOq26p5KgUct1HNMZ48GPp5FVArVTsRPSsblpD7Srr"
client_secret= "9iOcaGRiis5NFkoQuDcs4mXXLE2UkRMbShgABU7qsOoa4Cibwy"

request_token_url = 'http://www.tumblr.com/oauth/request_token'
authorization_url = 'http://www.tumblr.com/oauth/authorize'
access_token_url = 'http://www.tumblr.com/oauth/access_token'



def get_tokens():
    oauth = requests_oauthlib.OAuth1Session(client_key, client_secret=client_secret)  #creating a new instance of the OAuth1Session class, saving client_key and client_secret as instance variables to use later
    request_token_url = 'http://www.tumblr.com/oauth/request_token' #baseurl. type: string
    fetch_response = oauth.fetch_request_token(request_token_url)
    resource_owner_key = fetch_response.get('oauth_token')
    resource_owner_secret = fetch_response.get('oauth_token_secret') #keys from the dictionary saved as variables to be used later
#big picture the application is saying hello to twitter, I'll be asking you more things later; give me an owner_key and owner_secret to use for the rest of the session whenever I talk to you, so you'll know it's me
    base_authorization_url = 'http://www.tumblr.com/oauth/authorize' #setting base_authorization_url to be a string
    authorization_url = oauth.authorization_url(base_authorization_url) #calling the authorization_url method on oauth instance
    webbrowser.open(authorization_url)
    access_token_url = 'http://www.tumblr.com/oauth/access_token'
    oauth_tokens = oauth.fetch_access_token(access_token_url)
    resource_owner_key = oauth_tokens.get('oauth_token')
    resource_owner_secret = oauth_tokens.get('oauth_token_secret')
    
    return (client_key, client_secret, resource_owner_key, resource_owner_secret, verifier)
print get_tokens()