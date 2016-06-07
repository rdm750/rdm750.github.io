import sugarcrm
import sys
import os

'''
Connects to CRM (sugarcrm) and gets/sets data

 
'''
# Connect
url = "http://198.12.88.203/service/v4/rest.php"
session = sugarcrm.Session(url,sys.argv[1],sys.argv[2])

print 'Connects to CRM (sugarcrm) and gets data'

print 'sugar.py username password firstname optional_last_name'
print 'sugar.py username password firstname \n or sugar.py username password firstname lastname'

print '\n'

def query(contact_query):
	contacts=session.get_entry_list(contact_query)
        for contact in contacts:
            print contact.first_name, contact.last_name
            for field in dir(contact):
                if field.find('email')>=0 and getattr(contact, field, "").find("@") >= 0:
                   print getattr(contact,field) 
        contacts = session.get_entries_count(contact_query)
        print 'Number of contacts found',contacts


contact_query = sugarcrm.Contact(first_name=str(sys.argv[3]))
if len(sys.argv)>4:
	contact_query = sugarcrm.Contact(first_name=str(sys.argv[3]),last_name=str(sys.argv[4]))

query(contact_query)


