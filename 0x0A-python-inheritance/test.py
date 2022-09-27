#!/usr/bin/python3


class Contacts:
	no_of_contacts = 0
	contacts_info = {}

	def __init__(self, name="", email=""):
		type(self).no_of_contacts += 1
		self.name = name
		self.email = email
		Contacts.contacts_info[self.name] = self.email

	@property
	def name(self):
		return self.__name
	
	@property
	def email(self):
		return self.__email

	@name.setter
	def name(self, value):
		self.__name = value

	@email.setter
	def email(self, value):
		if '@' not in value:
			raise ValueError("Invalid email")
		self.__email = value

	@classmethod
	def contact(cls, value=""):
		if " - " not in value:
			raise ValueError("Invalid")
		name, email = value.split(" - ")
		return cls(name, email)

	def __str__(self):
		cont = {self.__name: self.__email}
		return str(cont)
	
	@classmethod
	def all_contacts(self):
		print(self.contacts_info)


con1 = Contacts.contact("Frnac - def@37.com")
print(con1.name)
#con1.email()
print(con1)

con2 = Contacts.contact("May - sghd@dhe.com")
con2 = Contacts.contact("Maer - djnd@gr .com")

Contacts.all_contacts()