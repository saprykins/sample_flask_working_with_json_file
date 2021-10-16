# with pagination
# strange behavior with handmade json files

"""
next steps:

1/ split in separate parts:
- controller(handles request, get file name from html-page)
- view(prints out)
- model(changes its status, biz logic)

2/ what to do without extention

3/ what is the difference between .json and .html

"""


# command line commands
# pip install flask
# python -c "import flask; print(flask.__version__)"

# commands after .py-file is saved:

# export FLASK_APP=ex11-v2
# export FLASK_ENV=development # not required line
# flask run
# or instead of the last line flask run --reload
# this will reload server after each file change

# you can check in browser
# http://127.0.0.1:5000/statuses
# http://127.0.0.1:5000/statuses/p=13
# http://127.0.0.1:5000/id_number.json
# http://127.0.0.1:5000/id_number.html
# http://127.0.0.1:5000/id_number # doesn't work


import json
from flask import jsonify
from flask import Flask
from flask import request


app = Flask(__name__)


def read_json():
# puts data from json-file to array

    json_file_in_array = []
    
    with open(r"C:/_My_Files/_FA/_ETUDES/python/py-code/day_3/2015-01-01-15.json", encoding="utf-8") as json_input:
    # with open(r"/Users/sio/Desktop/python_scripts/day_3/data_sample.json", encoding="utf-8") as json_input:
    # with open(r"C:/_My_Files/_FA/_ETUDES/python/py-code/day_3/data_sample.json", encoding="utf-8") as json_input:
        for feed in json_input:
            line = json.loads(feed)
            # print(line)
            # print(line["id"])
            json_file_in_array.append(line)
    return json_file_in_array
    # return str(json_file_in_array[0]['id'])


@app.route('/statuses', methods=['GET', 'POST'])
def liste_of_statuses():
# prints out to web-page an array 

    array = json_file_in_array
    return str(array)    # return str(array[0]['id'])


@app.route('/statuses/<ident>.<format>', methods=['GET', 'POST'])
def find_the_status(ident, format):
# prints out from array specifit record defined by ident
# ident is given from URL

    array = json_file_in_array

    if format == "json":
        for line in array:
            if line['id'] == ident:
                # return str(line) # returns sth
                # return jsonify(json.dumps(line)) # returns in json format
                return jsonify(line)  # +jolie
    if format == "html":
        for line in array:
            if line['id'] == ident:
                # return str(line) # returns sth
                return json.dumps(line)  # returns sth


# pagination
@app.route('/statuses/p=<int:page>', methods=['GET', 'POST'])
def pagination(page):
# prints out the chosen page of records
# page number is defined in URL
# where number of records per line is defined by number_by_page

    array = json_file_in_array
    number_by_page = 2
        
    sol = page * number_by_page
    eol = (page + 1)* number_by_page
    
    return str(array[sol:eol])


json_file_in_array = read_json()
