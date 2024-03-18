import joblib
from flask import Flask, render_template, request, url_for
from waitress import serve

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Home_1.html')

@app.route('/Predict')
def prediction():
    return render_template('Index.html')

@app.route('/form', methods=["POST"])
def brain():
    State_Name = float(request.form['State_Name'])
    Crop_Year = float(request.form['Crop_Year'])
    Crop = float(request.form['Crop'])
    Area = float(request.form['Area'])
    Production = float(request.form['Production'])

    values = [State_Name, Crop_Year, Crop, Area, Production]

if __name__ == '__main__':
    app.run(debug=True)
