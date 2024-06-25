from flask import Flask, request, jsonify
import requests
import whois

app = Flask(__name__)

@app.route("/search/<domain>", methods=['GET', 'POST'])
def home(domain):
	assert domain == request.view_args['domain']
	print(domain)
	return jsonify(search(domain))



def search(domain):
	search_result=whois.whois(domain)
	return(search_result)



if __name__ == '__main__':
	app.run(debug=True)
