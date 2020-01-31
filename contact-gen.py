import datetime
import re
import sys
import phonenumbers # pip install phonenumbers 
import json

from faker import Faker # pip install Faker
from faker.providers import phone_number
from faker.providers import internet
from faker.providers import company
from faker.providers import lorem
from faker.providers import address

fake = Faker()
fake.add_provider(phone_number)
fake.add_provider(internet)
fake.add_provider(company)
fake.add_provider(lorem)

# cleans up the fake phone number
# (sorry north american phone numbers only)

def sanitize_phone_number(pn):
	split = pn.split('x')
	without_extension = split[0]
	only_numbers = re.sub("[^0-9]", "", without_extension)
	remove_leading_zeros = only_numbers.lstrip("0")
	north_american_number = remove_leading_zeros
	if len(north_american_number) < 11:
		north_american_number = "+1%s" % north_american_number
	parsed = phonenumbers.parse(north_american_number, "US")
	pss = phonenumbers.is_valid_number(parsed)
	if pss:
		formatted = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164)
		return formatted
	else:
		return sanitize_phone_number(fake.phone_number())

def generate(count):

	profiles = []
	for _ in range(count):
		profile = {}
		profile['full_name'] = fake.name()
		full_name_split = fake.name().split(" ")
		profile['given_name'] = full_name_split[0]
		profile['family_name'] = full_name_split[1]
		profile['company_name'] = fake.company()
		profile['email_address']  = "%s_%s@%s" % (profile['given_name'].lower(), profile['family_name'].lower(), fake.free_email_domain())
		random_phone_number = fake.phone_number()
		profile['phone_number'] = sanitize_phone_number(random_phone_number) # sanitized & formatted
		profile['note'] = fake.paragraph(nb_sentences=3, variable_nb_sentences=True, ext_word_list=None)
		profile['address'] = fake.address().replace('\n', ', ')
		profile['id'] = fake.sha1()
		profile['image_url'] = fake.image_url()
		profiles.append(profile)

	print(json.dumps(profiles))
	with open('profiles.json', 'w') as outfile:
	    json.dump(profiles, outfile)

def main():
    # print command line arguments
    count = 10
    if len(sys.argv[1:]) > 0:
	    count = sys.argv[1:][0]
    generate(int(count))

if __name__ == "__main__":
    main()