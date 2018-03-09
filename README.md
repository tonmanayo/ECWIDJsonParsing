# ECWIDJsonParsing
This application takes json data from ecwid and puts it into a .csv file

use get all the products json data from your store and save it in a file called products.json
use get all the categories json data from your store and save it in a file called categories.json

to get all .json data from profucts: - replace YOURSECRETTOKEN with your token
https://app.ecwid.com/api/v3/11514205/products?token=YOURSECRETTOKEN
then offset the page every 100 products until you have all your products: EXAMPLE
https://app.ecwid.com/api/v3/11514205/products?token=YOURSECRETTOKEN&&offset=100
https://app.ecwid.com/api/v3/11514205/products?token=YOURSECRETTOKEN&&offset=200

remember to save and append the json data to products.json

same process to get categories - then save all the json data to categories.json
https://app.ecwid.com/api/v3/11514205/categories?token=YOURSECRETTOKEN 

unix:
once you have created both .json files run python parsingJson.py

windows:
https://stackoverflow.com/questions/9493086/python-how-do-you-run-a-py-file
