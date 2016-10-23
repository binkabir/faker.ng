# faker.ng
Faker.ng is a library for generating Nigerian fake data such as names, addresses, and phone numbers. 

Instructions to get up and running locally:

1. You need to have MongoDB installed. In the db.py file you need to update your Mongo server details (currently set to localhost) and your port (currently set to the default 27017)

2. The config files have not yet been externalised, so you will have to manually udpate this 'path' in this file with your local settings:
parser.py

3. When you have this setup you then need to run the db_helper.py script: python db_helper.py, this will create a new faker database in mongo and create a collection called people, and it will populate the database

4. You need to then run index.py: python index.py, this will start the test server on:
IP - 127.0.0.1, if you are running locally and on port 5000

sample_api_result
sample_data_in_mongo_db

FakerNG is now live on faker.abujadevmeetup.com
To test the API visit:http://faker.abujadevmeetup.com/api/v1/faker/people
