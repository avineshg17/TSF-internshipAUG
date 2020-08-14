# TSF-internshipAUG

# ML-Model-Flask-Deployment
This is a Project which is to Predict Marks Based on Number of Hours Studied 

# Prerequisites
You must have Scikit Learn, Pandas (for Machine Leraning Model) and Flask (for API) installed.

# Project Structure
This project has four major parts :

#model.py - This contains code fot our Machine Learning model to predict Marks based on data in 'Student_Scores.csv' file.
#app.py - This contains Flask APIs that receives  through GUI or API calls, computes the precited value based on our model and returns it.
#request.py - This uses requests module to call APIs already defined in app.py and dispalys the returned value.
#templates - This folder contains the HTML template to allow user to enter Hours detail and displays the predicted Marks.
# Running the project
Ensure that you are in the project home directory. Create the machine learning model by running below command -
python model.py
This would create a serialized version of our model into a file model.pkl

Run app.py using below command to start Flask API
python app.py
By default, flask will run on port 5000.

Navigate to URL http://localhost:5000
You should be able to view the homepage as below : alt text

Enter valid numerical values in input box and hit Predict.

If everything goes well, you should be able to see the predcited Marks vaule on the HTML page! alt text
