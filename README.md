# contact-gen

A python script that generates N user profiles. This script provides a thin wrapper around the python [Faker](http://faker.rtfd.org) library. It enforces that the generated phone number be a valid (north american for now) number and outputs the profiles in json.


## installation

1. `pip install Faker`
2. `pip install phonenumbers` 

## usage

`python contact-gen.py 50 // Generates 50 profiles and outputs a profiles.json file in the directory the script is run`
