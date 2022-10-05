### Description
This is django rest framework project. It contains the rest apis for books publication. Most of the apis are accessible 
using jwt token. Few apis are with authentication. There are example requests in postman collection given on root path.

### Installation:
1. create and activate python virtual environment using python 3.9
2. install requirements.txt `pip install requirements.txt`

### Run Application
1. apply migrations. 
   `python manage.py migrate`
2. to run the test cases, run this command 
   `python manage.py test`
3. to run the server, run this command. 
   `python manage.py runserver`

To test the apis, please run the postman collection(apis.postman_collection.json) in post added in root directory of 
project. If you don't have postman, installed on you computer, you can open the postman json file. 
It contains all the information related to apis.