from flask import Flask, render_template, request
import pickle
import pandas as pd
import typeconv as tp
import new_df

model = pickle.load(open('ml_model.pkl','rb'))

app = Flask(__name__,template_folder='template')
@app.route('/')
def main():
    return render_template('index.html')

@app.route('/prediction')
def prediction():
    return render_template('prediction.html')


@app.route('/pred',methods=["POST"])
def home():
    d1 = request.form['gender']
    d2 = request.form['Relevant Experience']
    d3 = request.form['university']
    d4 = request.form['qualification']
    d5 = request.form['discipline']
    d6 = request.form['Last New Job']
    d7 = request.form['Experience in years']
    d8 = request.form['Company Size']
    d9 = request.form['companytype']
    d10 = request.form['traininghours']
    new_data = [[d1,d2,d3,d4,d5,d7,d8,d9,d6,d10]]
    print(new_data)
    new_df1 = new_df.new_dataframe(new_data)
    dataframe_after_type=tp.typeconvo(new_df1)
    print(dataframe_after_type)
    predict_value = model.predict(new_df1)
    print(predict_value)
    if predict_value == 1:
        return render_template('prediction.html', data = "Looking for a job change")
    elif predict_value == 0 :
        return render_template('prediction.html', data = "Not looking for job change")
if __name__ == "__main__":
    app.run(debug=True)
