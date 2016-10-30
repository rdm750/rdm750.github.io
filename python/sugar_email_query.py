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
#session = sugarcrm.Session(url,sys.argv[1],sys.argv[2])
session = sugarcrm.Session(url,'admin','beautyman')
print banner
#s = csv.writer(open('contacts_ID_fields_Dump.csv','wb'))
#s.writerow(['ID','FIRST','LAST'])
s= csv.DictReader(open('/Users/medhamalgaonkar/Desktop/rohit/Database_Website_Volunteer/USIC Members Unpaid 2015.csv','rU'))
rs=csv.writer(open('/Users/medhamalgaonkar/Desktop/rohit/Database_Website_Volunteer/USIC Members Unpaid 2015_Mod.csv','w'))
rs2=csv.writer(open('/Users/medhamalgaonkar/Desktop/rohit/Database_Website_Volunteer/USIC Members Unpaid 2015_Mod_2.csv','w'))

list_of_fields=[]

def email_query(contact_query,emal,addrs):
    progres = 0
    contacts=session.get_entry_list(contact_query)
    for contact in contacts:
        #print [contact.id,contact.first_name, contact.last_name,contact.email1]
            #s.writerow([contact.id,contact.first_name, contact.last_name,contact.email1])
        for field in dir(contact):
                list_of_fields.append(field)
                if getattr(contact, field, "")!='':
                    if field.find('email')>=0 and getattr(contact, field, "").find(emal) >= 0:
                        #print getattr(contact,field)
                        #print [contact.id,contact.first_name, contact.last_name,contact.email1,contact.interests_c]
                        new_row = [contact.id,contact.first_name, contact.last_name,contact.email1,contact.interests_c]
     
                        #for itm in dir(contact):
                            #pass
                            #print getattr(contact,itm)
                        print '-*-'*10
                        progres+=1
                    else:
                        new_row = [contact.id,contact.first_name, contact.last_name,contact.email1,contact.interests_c]
                        
        #print new_row                    
                                       
    contacts = session.get_entries_count(contact_query)
    if contacts == 0:
        print rs2.writerow([emal])    
    else:
        #pass
        print rs.writerow(new_row)
    print 'Number of contacts found',contacts,'Contacts with email match',progres


for row in s:
    print row['E-mail']
    #Address    City    State   Zip
    #primary_address_city   primary_address_country primary_address_postalcode  primary_address_state   primary_address_street
    contact_query = sugarcrm.Contact(first_name ='%'+row['First'].strip()+'%',last_name ='%'+row['Last'].strip()+'%'\
    ,alt_address_street='%'+row['Address'].strip()+'%',\
    alt_address_city ='%'+row['City'].strip()+'%',alt_address_state = '%'+row['State'].strip()+'%',alt_address_postalcode='%'+row['Zip'].strip()+'%')   
    #email = row['E-mail']) #first_name ='%'+row['First']+'%',last_name ='%'+row['Last']+'%')  #    

    email_query(contact_query,row['E-mail'].strip(),row['Address'].strip())

#accounts_query=modules[Accounts](first_name=str(sys.argv[3]))
print '*'*10

