# Import libraries for connection mongodb
import urllib
import certifi
from pymongo import MongoClient
from unicodedata import name

#function to open db from a mongo user
def connect_mongodb (db_username, db_passw, db_name):
    MONGODB_USERNAME = urllib.parse.quote_plus(db_username)
    MONGODB_PASSWORD = urllib.parse.quote_plus(db_passw)
    MONGODB_DATABASE = db_name
    ca = certifi.where()
    MONGODB_URL = "mongodb+srv://"+MONGODB_USERNAME+":"+MONGODB_PASSWORD+"@cluster0.ks8wq.mongodb.net/"+MONGODB_DATABASE+"?retryWrites=true&w=majority"
    client = MongoClient(MONGODB_URL, tlsCAFile=ca)
    database = client.get_database(db_name)
    return database

#call the function to generate your own db
databases = connect_mongodb (db_username='freda', db_passw='19freda87', db_name='mydb')
#generate my clusters
my_cluster = databases.mobile_numbers

#create a query according to a certain request
query1 = {"HasPhone" : 1}

#extract the data depending on the query
list_numbers=list()
for phones in my_cluster.find(query1):
      list_numbers.append(phones["Phone"])
my_number = '+355' + str(list_numbers[0])


#connection with twilio
import os
from twilio.rest import Client
 
account_sid = 'ACf154a88c2e2b9e4ac792fc4a6834227c' 
auth_token = '3e23e49549cca47624827349f622cc9d' 
client1 = Client(account_sid, auth_token) 
 
#sending sms
message = client1.messages.create(  
                              messaging_service_sid='MG3a02647da11bba2f4ef4d9b179f3bb11', 
                              body='HelloFreda',      
                              to='+355693989000'
                          ) 

#sending whatsup sms
# message = client1.messages.create(
#                               body='Hello there!',
#                               from_='whatsapp:+14155238886',
#                               to='whatsapp:+355693989000'
#                           )
 
print(message.sid)
