# with pagination
# strange behavior with handmade json files


# command line commands
# pip install flask
# python -c "import flask; print(flask.__version__)"

# commands after .py-file is saved:

# export FLASK_APP=ex11-v2
# export FLASK_ENV=development # not required line
# flask run

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
    json_file_in_array = []
    
    # with open(r"C:/_My_Files/_FA/_ETUDES/python/py-code/day_3/2015-01-01-15.json", encoding="utf-8") as json_input:
    # with open(r"/Users/sio/Desktop/python_scripts/day_3/data_sample.json", encoding="utf-8") as json_input:
    with open(r"C:/_My_Files/_FA/_ETUDES/python/py-code/day_3/data_sample.json", encoding="utf-8") as json_input:
        for feed in json_input:
            line = json.loads(feed)
            # print(line)
            # print(line["id"])
            json_file_in_array.append(line)
    return json_file_in_array
    # return str(json_file_in_array[0]['id'])


@app.route('/statuses', methods=['GET', 'POST'])
def liste_of_statuses():
    array = json_file_in_array
    return str(array)    # return str(array[0]['id'])


@app.route('/statuses/<ident>.<format>', methods=['GET', 'POST'])
def find_the_status(ident, format):
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
    array = json_file_in_array
    number_by_page = 2
        
    sol = page * number_by_page
    eol = (page + 1)* number_by_page
    
    return str(array[sol:eol])


json_file_in_array = read_json()
