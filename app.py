# from __future__ import print_function
# from future.stanard_library import install_aliasas
# install_aliasas()

# from urllib.parse import urlparse, urlencode
from urllib.requst import urlopen, Requst
# from urllib.error import HTTPError

import json
import os
import sys

from flask import Flask
from flask import request
from flask import make_response

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
	req = request.get_json(silent=True, force=True)

	print("Request:")
	print(json.dumps(req, indent=4))

	# Dictionary Object
	res = process_request(req)

	# Dictionary converted to json
	res = json.dumps(rest, indent=4)

	r = make_response(res)
	r.headers['Content-Type'] = 'application/json'
	return r

def process_request(req):
	if req.get("result").get("action") != "TodaysOpportunities.Direct":
		return {}

	#Type of opportunity
	oppType = result.get("result").get("parameters").get("opp-type") 

	speech = "The following people qualify for " + oppType + ": John Doe, Joe Schmo, Lisa Grahm"

	return {
		"speech": speech,
		"displayText": speech,
		#Change this
		"source": "apiai-weather-webhook-sample" 
	}
	## Converting website url to json usable json.
    # result = urlopen(yql_url).read()
    # data = json.loads(result)
    # res = makeWebhookResult(data)
    # return res

if __name__ == '__main__':
	port = int(os.getenv('PORT'), 5000)

	print("Starting app on port %d" % port)

	app.run(debug=False, port=port, host='0.0.0.0')