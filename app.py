from flask import Flask, render_template, request
import pandas as pd
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def medical_condition():
    data_df = pd.read_csv('C:\\Users\\SDE77\\Desktop\\Healthcare_Data\\Q2\\healthcare_dataset.csv')
    if request.method == "POST":
        name = request.form['name']
        bg = request.form['bg']
        gender = request.form['gender']
        condition = data_df[(data_df['Gender'] == gender) & (data_df['Blood Group'] == bg)]['Medical Condition'].values[0]
        return render_template('result.html', name = name, condition = condition)
    else:
        return render_template('index.html')

@app.route('/update', methods=['GET', 'POST'])
def addUserData():
    if request.method == "POST":
        # Get data from the form
        name = request.form['name']
        gender = request.form['gender']
        bg = request.form['bg']
        # Store the data in a dictionary
        user_data = {'Name': name, 'Gender': gender, 'Blood Group': bg}
        # Append the user data to a CSV file
        with open('user_data.csv', 'a') as f:
            f.write(f"{name},{gender},{bg}\n")
    else:
        # If it's a GET request or any other method, initialize an empty dictionary
        user_data = {}
    return render_template('addData.html', user_data=user_data)
    
    

if __name__ == "__main__":
    app.run(debug=True, port=5000)

    