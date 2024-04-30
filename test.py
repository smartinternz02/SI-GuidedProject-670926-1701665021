from flask import *
import numpy as np
import pandas
# import pickle
import pickle4 as pickle
import os

app = Flask(__name__)
# model = pickle.load(open('rf.pkl', 'rb'))

import pickle


with open('rf.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/input")
def output():
    return render_template("input.html")

@app.route('/submit',methods=["POST","GET"])# route to show the predictions in a web UI
def submit():
    #  reading the inputs given by the user
    input_feature=[int(x) for x in request.form.values()]  
    #input_feature = np.transpose(input_feature)
    input_feature=[np.array(input_feature)]
    print(input_feature)
    data = list(input_feature)
    names = ['ADM0_NAME', 'ADM1_NAME', 'ADM2_NAME', 'Income_Category','Income_Year', 'IncomeValue', 'Income_DataSource']
    data = pandas.DataFrame(data,columns=names)
    #print(data)
    
    #data_scaled = scale.fit_transform(data)

    

     # predictions using the loaded model file
    prediction=model.predict(data)
    print(prediction)
    prediction = round(int(prediction))
 
   
    return render_template("output.html", result=prediction)

if __name__ == "__main__":
    app.run(debug = True,port = 1111)