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

list_of_fields=[]
def query(contact_query):
	contacts=session.get_entry_list(contact_query)
        for contact in contacts:
            print contact.first_name, contact.last_name
            for field in dir(contact):
                list_of_fields.append(field)
		
		if getattr(contact, field, "")!='':
#field.find('email')>=0 if getattr(contact, field, "").find("@") >= 0:
                   print getattr(contact,field) 
        contacts = session.get_entries_count(contact_query)
        print 'Number of contacts found',contacts


contact_query = sugarcrm.Contact(first_name=str(sys.argv[3]))
modules = session.get_available_modules()
for m in modules:
    print m.module_key
print '-*-'*10

#accounts_query=modules[Accounts](first_name=str(sys.argv[3]))

if len(sys.argv)>4:
	contact_query = sugarcrm.Contact(first_name=str(sys.argv[3]),last_name=str(sys.argv[4]))


query(contact_query)

print '*'*10
