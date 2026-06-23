from flask import Flask, jsonify
app = Flask(__name__)

# Sample data
contracts = [
    {"id": 1, "title": "Website Development"},
    {"id": 2, "title": "Mobile App Contract"},
    {"id": 3, "title": "IT Support Agreement"}
]

customers = ["Alice", "Bob", "Charlie"]


# Contract route
@app.route('/contract/<int:id>')
def get_contract(id):
    for contract in contracts:
        if contract["id"] == id:
            return jsonify(contract), 200

    return "", 404


# Customer route
@app.route('/customer/<customer_name>')
def get_customer(customer_name):
    if customer_name in customers:
        # Customer exists, but no data is returned
        return "", 204

    return "", 404


if __name__ == '__main__':
    app.run(debug=True)