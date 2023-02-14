from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/v1/employees', methods=['POST'])
def post_employees():
    employees = [
        {'id': 4, 'firstName': 'Josh', 'lastName': 'Dong', 'emailId': 'joshdong@example.com'},
        {'id': 5, 'firstName': 'Janet', 'lastName': 'Smurf', 'emailId': 'janetsmurf@example.com'},
        {'id': 6, 'firstName': 'Robert', 'lastName': 'Deniro', 'emailId': 'robertdeniro@example.com'}
    ]
    return jsonify(employees)

if __name__ == '__main__':
    app.run(debug=True, port=8080)