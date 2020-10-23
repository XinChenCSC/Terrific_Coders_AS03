import datetime

from flask import Flask, abort, jsonify, request

from inspector import Inspector

app = Flask(__name__)

# curl -s localhost:5000/search | json_pp

# curl -s localhost:5000/search?q=domino | json_pp
#   --> Search inspections by restaurant name.
# curl -s localhost:5000/search?cusine=italian | json_pp
#   --> Search inspections by restaurant name.
# curl -s localhost:5000/search?zipcode=11238 | json_pp
#   --> Search inspections by zipcode.

# Params can be combined for further filtering
@app.route('/search', methods=['GET'])
def search():
    abort(500, 'Unimplemented')

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
