import contact_utils

PATH_CSV = 'data/contacts.csv'
PATH_JSON = 'data/contacts.json'

try:
    # contacts = contact_utils.csv_to_contact(PATH_CSV, 'utf8')
    # contact_json = contact_utils.contacts_to_json(PATH_JSON, contacts)
    contacts_from_json = contact_utils.json_for_contacts(PATH_JSON)
except FileNotFoundError:
    print('File not found')
except PermissionError:
    print('Permission denied')

# for contact in contacts:
#     print (f'{contact.id} - {contact.name} - {contact.email}')
for contact in contacts_from_json:
    print (f'{contact.id} - {contact.name} - {contact.email}')
