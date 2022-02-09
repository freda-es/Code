# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
 
account_sid = 'ACf154a88c2e2b9e4ac792fc4a6834227c' 
auth_token = '3e23e49549cca47624827349f622cc9d' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid='MGb2ed808529d3f460f778b8f8d9f6c063', 
                              body='Hello Freda',      
                              to='+355693989000' 
                          ) 
 
print(message.sid)
