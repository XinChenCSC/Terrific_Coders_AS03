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
	inspector = Inspector()
	query = request.args.get('q')
	cusin = request.args.get('cusine')
	zipcode = request.args.get('zipcode')
	limit = request.args.get('limit',5)	

	result = []

	if query:
		for inspection in inspector.inspections:
			if query.lower() in inspection.restaurant_name.lower():
				result.append(inspection)
	if cusine:
		inspections = results or inspector.inspections
		for inspection in inspector.inspections:
			if cusine.lower() in inspection.cusine.lower():
				result.append(inspection)
	if zipcode:
		inspections = results or inspector.inspections
		for inspection in inspector.inspections:
			if zipcode.lower() in inspection.zipcode.lower():
				result.append(inspection)
	return jsonify({"data": [result.to_json() for result in results[:limit]]})

    

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
