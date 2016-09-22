CONSUMER_KEY = '77b046lfl6qov7'     # This is api_key
CONSUMER_SECRET = 'ZHAidsQl5YwNptPE'   # This is secret_key

import oauth2 as oauth
import urlparse

consumer_key           = "77b046lfl6qov7"
consumer_secret        = "ZHAidsQl5YwNptPE"
consumer = oauth.Consumer(consumer_key, consumer_secret)
client = oauth.Client(consumer)

request_token_url      = 'https://api.linkedin.com/uas/oauth/requestToken'
resp, content = client.request(request_token_url, "POST")
if resp['status'] != '200':
    raise Exception("Invalid response %s." % resp['status'])

print content
print "\n"

request_token = dict(urlparse.parse_qsl(content))

print "Requesr Token:",  "\n"
print "- oauth_token        = %s" % request_token['oauth_token'], "\n"
print "- oauth_token_secret = %s" % request_token['oauth_token_secret'], "\n"

authorize_url = 'https://api.linkedin.com/uas/oauth/authorize'
print "Go to the following link in your browser:", "\n"
print "%s?oauth_token=%s" % (authorize_url, request_token['oauth_token']), "\n"

url_2 = authorize_url+"?oauth_token="+request_token['oauth_token']
print url_2

import requests
import urllib2

s = requests.session()
login_data = dict(email='rdm750@gmail.com', password='A6fH6mSfZ4')
content1 = s.post(url_2, data=login_data)
r = urllib2.urlopen('https://www.linkedin.com/uas/oauth/authorize/submit')
print r.read()

#resp1, content1 = client.request(url_2, "POST")
#pin1= dict(urlparse.parse_qsl(content1))
#print pin1

accepted = 'n'
while accepted.lower() == 'n':
    accepted = raw_input('Have you authorized me? (y/n) ')
oauth_verifier = raw_input('What is the PIN? ')

access_token_url = 'https://api.linkedin.com/uas/oauth/accessToken'
token = oauth.Token(request_token['oauth_token'], request_token['oauth_token_secret'])
token.set_verifier(oauth_verifier)
client = oauth.Client(consumer, token)

resp, content = client.request(access_token_url, "POST")
access_token = dict(urlparse.parse_qsl(content))

'''
print "Access Token:", "\n"
print "- oauth_token        = %s" % access_token['oauth_token'], "\n"
print "- oauth_token_secret = %s" % access_token['oauth_token_secret']
print "You may now access protected resources using the access tokens above."
'''


USER_TOKEN = access_token['oauth_token']   # This is oauth_token
USER_SECRET = access_token['oauth_token_secret']   # This is oauth_secret
RETURN_URL = ''

from linkedin import linkedin
from oauthlib import *

# Define CONSUMER_KEY, CONSUMER_SECRET,  
# USER_TOKEN, and USER_SECRET from the credentials 
# provided in your LinkedIn application

# Instantiate the developer authentication class

authentication = linkedin.LinkedInDeveloperAuthentication(CONSUMER_KEY, CONSUMER_SECRET, 
                                                      USER_TOKEN, USER_SECRET, 
                                                      RETURN_URL, linkedin.PERMISSIONS.enums.values())

# Pass it in to the app...

application = linkedin.LinkedInApplication(authentication)

# Use the app....

g = application.get_profile()
print g

#print application.get_companies()

print application.search_company(selectors=[{'companies': ['name', 'universal-name', 'website-url']}], params={'keywords': 'apple microsoft'})

#c = application.get_connections()
#print c
#print application.get_memberships()

print application.search_profile(selectors=[{'people': ['first-name', 'last-name']}], params={'keywords': 'apple microsoft'})




