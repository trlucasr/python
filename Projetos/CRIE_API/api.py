from flask import Flask

app = Flask(__name__)

app.run(debug=True)

@app.route('/todo/getall',methods=['GET'])
def getTasks():
    return 'Get all taks!'