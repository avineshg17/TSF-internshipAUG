#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle


# In[5]:


app = Flask(__name__,template_folder='template')
model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    
    return render_template('index.html')

@app.route('/predict',methods = ['POST'])
def predict():
    
    float_features = [float(x) for x in request.form.values()]
    final_features = [np.array(float_features)]
    prediction = model.predict(final_features)
    
    
    output = round(prediction[0],2)
    
    return render_template('index.html' ,prediction_text='The Marks will be {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)


# In[ ]:




