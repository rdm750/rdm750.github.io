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
#query(accounts_quer)

print '*'*10
#query(accounts_query)
#print list_of_fields

'''
with codecs.open("Contact_fields_template.csv", "w", encoding='utf8') as out:
    out.write(' '.join(list_of_fields))

columns = defaultdict(list)

with open('Contact_fields_template_Mod.csv') as f:
     reader = csv.DictReader(f)
     for row in reader:
         for (k,v) in row.items():
             columns[k].append(v)

print '*'*10
#print (columns['first_name'])
f.close()

f=open('Contact_fields_template_Mod.csv','r')
k=0
update_list=[]
for line in f:
    test=line.split(',')
    if k==0:
        header=test 
    s=0
    if ''.join(map(str,test))!=''.join(map(str,header)):
        print '*'*30 
        for t in test: 
            if t!=',' and t!='' and t not in header:
                print t,s,header[s]
		update_list.append(tuple([header[s],t]))
            s+=1
    k+=1

f.close()
	    	
print [k for k in update_list]
'''
#    for email, (first_name, last_name) in emails.items():
 #       out.write("%s,%s,%s\n" % (email, first_name, last_name))
'''
'''
