from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    data={'page':'home'}
    return jsonify(data)


@app.route("/search", methods=['GET', 'POST'])
def search():
    data={'endpoint':'search'}
    if request.method == 'POST':
        domain=request.form['domain']
        url='https://{}/'.format(domain)
        try:
            resp=requests.get(url, verify=False)
            data={'endpoint':'search','domain':'{}'.format(url),'status_code':'{}'.format(resp.status_code)}
        except Exception as e:
            error=str(e)
            data={'page':'search','error':'{}'.format(error)}
    if request.method == 'GET':
        data={'page':'search','error':'Method should be POST'}
        
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
