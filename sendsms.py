# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
 
account_sid = 'account_sid' 
auth_token = 'auth_token' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid='MGb2ed8085...', 
                              body='Hello Freda',      
                              to='+3556939...' 
                          ) 
 
print(message.sid)
