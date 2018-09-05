from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/',methods=['POST'])
def foo():
  data = json.loads(request.data)
  # print ("New commit by: {}".format(data['commits'][0]['author']['name']))
  if data:
    print (data)
    return "OK"
  return "NOT OK"

if __name__ == '__main__':
   app.run(debug=True, host="127.0.0.1", port=8898)