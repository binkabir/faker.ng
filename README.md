# faker.ng
Faker.ng is a library for generating Nigerian fake data such as names, emails, sex, addresses, and phone numbers. It's main purpose is to help developers populate their applications with dummy record for testing and presentation. 

Instructions to get up and running locally:

1. You need to have MongoDB installed. In the db.py file you need to update your Mongo server details (currently set to localhost) and your port (currently set to the default 27017).

2. The config files have not yet been externalised, so you will have to manually update this 'path' in this file with your local settings:
parser.py

3. After this setup run the db_helper.py script: python db_helper.py.  This will create a new faker database with a mongo-collection called people in your local mongo database server. 

4. Run the index.py: python index.py, this will start the test server on:
IP - 127.0.0.1, if you are running locally and on port 5000

sample_api_result
sample_data_in_mongo_db

FakerNG is now live on faker.wecode.ng
To test the API visit:http://faker.wecode.ng/api/v1/faker/people
