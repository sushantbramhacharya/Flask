from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)


client = MongoClient('localhost:27017')
db = client['Hospital']
collection = db['Doctors']
all_doctors=list(collection.find())

print(all_doctors)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/doc', methods=['GET'])
def show_doctors():
    return render_template('doctor_template.html', doctors=all_doctors)

if __name__ == '__main__':
    app.run(debug=True)
