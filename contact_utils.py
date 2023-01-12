import csv
import json

from contact import Contact

class Convert:
    def __init__(self, path:str, contact=None, encoding:str=None):
        self.path = path
        self.contact = contact
        self.encoding = encoding

    def csv_to_contact(self) -> dict:
        contacts = []

        with open(self.path, 'r', encoding=self.encoding) as f:
            reader = csv.reader(f)
            for row in reader:
                id, name, email = row
                contact = Contact(id=id, name=name, email=email)
                contacts.append(contact)
        return contacts

    def contacts_to_json(self):
        with open(self.path, 'w', encoding='utf-8') as f:
            json.dump(
                self.contact,
                f,
                ensure_ascii=False,
                indent=4,
                default=self._contact_representation
            )

    def json_for_contacts(self, test):
        contacts = []

        with open(self.path) as f:
            contacts_in_json = json.load(f)

            for contact in contacts_in_json:
                c = Contact(**contact)
                contacts.append(c)
        return contacts

    def _contact_representation(self, contact):
        return contact.__dict__
