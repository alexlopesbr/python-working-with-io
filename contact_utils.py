import csv
import json

from contact import Contact


def csv_to_contact(path:str, encoding:str='latin_1') -> dict:
    contacts = []
    with open(path, 'r', encoding=encoding) as f:
        reader = csv.reader(f)
        for row in reader:
            id, name, email = row
            contact = Contact(id=id, name=name, email=email)
            contacts.append(contact)
    return contacts

def contacts_to_json(path:str, contacts):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(contacts, f, ensure_ascii=False, indent=4, default=_contact_representation)

def _contact_representation(contact):
    return contact.__dict__

def json_for_contacts(path:str):
    contacts = []

    with open(path) as f:
        contacts_in_json = json.load(f)

        for contact in contacts_in_json:
            # c = Contact(contact['id'], contact['name'], contact['email'])
            c = Contact(**contact)
            contacts.append(c)
    return contacts
