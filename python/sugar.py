import sugarcrm
import sys
import os
import codecs
import csv
from collections import defaultdict

banner =\
'''
Connects to CRM (sugarcrm) and gets/sets data
Connects to CRM (sugarcrm) and gets data
sugar.py username password firstname optional_last_name
sugar.py username password firstname \n or sugar.py username password firstname lastname
 
'''
# Connect
url = "http://198.12.88.203/service/v4/rest.php"
session = sugarcrm.Session(url,sys.argv[1],sys.argv[2])
print banner
#s = csv.writer(open('contacts_ID_fields_Dump.csv','wb'))
#s.writerow(['ID','FIRST','LAST'])
s= csv.DictReader(open('/Users/medhamalgaonkar/Desktop/rohit/Database_Website_Volunteer/USIC Members Unpaid 2015.csv','r'))

list_of_fields=[]

def query(contact_query):
    progres = 0
    contacts=session.get_entry_list(contact_query)
    for contact in contacts:
            #s.writerow([contact.id,contact.first_name, contact.last_name,contact.email1])
        #
        for con in vars(contact).items():
            pass
            #print con
        
        #print progres,
        for field in dir(contact):
            if 'email' not in field:
                pass
                #print field    
        for field in dir(contact):
            list_of_fields.append(field)
            print getattr(contact,field)
            if getattr(contact, field, "")!='':
                if field.find('email')>=0 and getattr(contact, field, "").find('@') >= 0:
                    #print getattr(contact,field)
                    #print [contact.id,contact.first_name, contact.last_name,contact.email1,contact.interests_c,contact.primary_address_street]  
                    print '-*-'*10   
                    progres+=1
        
    contacts = session.get_entries_count(contact_query)
        
    print 'Number of contacts found',contacts,'Contacts with email match',progres

'''
def email_query(contact_query):
        progres = 0
    contacts=session.get_entry_list(contact_query)
        for contact in contacts:
            #s.writerow([contact.id,contact.first_name, contact.last_name,contact.email1])
            progres+=1
            print progres,
            
             
            for field in dir(contact):
                list_of_fields.append(field)
        
        if getattr(contact, field, "")!='':
            field.find('email')>=0 if getattr(contact, field, "").find("@") >= 0:
                   print getattr(contact,field) 
        
        contacts = session.get_entries_count(contact_query)
        
        print 'Number of contacts found',contacts
'''

if len(sys.argv) < 3:
    contact_query = sugarcrm.Contact()  #first_name
    contact_query.query = "first_name = 'rohit' "

else:    
    contact_query = sugarcrm.Contact(first_name = '%'+str(sys.argv[3])+'%',last_name='%'+str(sys.argv[4]))  #primary_address_street', u'1201 Bethlehem Pike'

modules = session.get_available_modules()
for m in modules:
    print m.module_key
print '-*-'*10

#accounts_query=modules[Accounts](first_name=str(sys.argv[3]))
'''
if len(sys.argv)>4:
    contact_query = sugarcrm.Contact(first_name=str(sys.argv[3]),last_name=str(sys.argv[4]))
'''
'''
for df in dir(contact_query):
    print df
    for dfw in dir(df):
        print dfw
'''

query(contact_query)

print '*'*10
