from flask import Flask, jsonify
app = Flask(__name__)


contracts = [
    {"id": 1, "title": "Website Development"},
    {"id": 2, "title": "Mobile App Contract"},
    {"id": 3, "title": "IT Support Agreement"}
]

customers = ["alice", "bob", "charlie"]
@app.route('/contract/<int:id>')
def get_contract(id):
   
    if id == 1:
        return "This contract is for John and building a shed", 200

    return "", 404



@app.route('/customer/<customer_name>')
def get_customer(customer_name):
    
    if customer_name.lower() in customers:
        return "", 204

    return "", 404


if __name__ == '__main__':
    app.run(debug=True)