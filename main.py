# import contact_utils
from contact_utils import Convert

PATH_CSV = 'data/contacts.csv'
PATH_JSON = 'data/contacts.json'
PATH_JSON_2 = 'data/contacts_2.json'

try:
    json_for_contacts = Convert(PATH_JSON).json_for_contacts('test')
    csv_to_contacts = Convert(path=PATH_CSV, encoding='utf8').csv_to_contact()
    contacts_to_json = Convert(path=PATH_JSON_2, contact=json_for_contacts).contacts_to_json()
except FileNotFoundError:
    print('File not found')
except PermissionError:
    print('Permission denied')



# for contact in csv_to_contacts:
    # print (f'{contact.id} - {contact.name} - {contact.email}')

# for contact in json_for_contacts:
    # print (f'{contact.id} - {contact.name} - {contact.email}')
