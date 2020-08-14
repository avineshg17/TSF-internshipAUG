# TSF-internshipAUG

# ML-Model-Flask-Deployment(TASK NO.2)
This is a Project which is to Predict Marks Based on Number of Hours Studied 

# Prerequisites
You must have Scikit Learn, Pandas (for Machine Leraning Model) and Flask (for API) installed.

# Project Structure
This project has four major parts :

1.model.py - This contains code fot our Machine Learning model to predict Marks based on data in 'Student_Scores.csv' file.
2.app.py - This contains Flask APIs that receives  through GUI or API calls, computes the precited value based on our model and returns it.
3.request.py - This uses requests module to call APIs already defined in app.py and dispalys the returned value.
4.templates - This folder contains the HTML template to allow user to enter Hours detail and displays the predicted Marks.
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


# Determining Number Of Clusters(TASK 3)

In this task we have to Determine Number Of cluster(Unsupervised Learning) For a very Popular Kaggle Dataset i.e. IRIS dataset
I have Used KMeans and WCSS for Determining Number of Cluster which came out to be (K=3) i have alos plotted Dendrograms For the same


# Working with DecisionTree Algorithm and Visualising(TASK 4)

# Decision Tree Algorithm
Decision Tree algorithm belongs to the family of supervised learning algorithms. Unlike other supervised learning algorithms, the decision tree algorithm can be used for solving regression and classification problems too.
The goal of using a Decision Tree is to create a training model that can use to predict the class or value of the target variable by learning simple decision rules inferred from prior data(training data).
In Decision Trees, for predicting a class label for a record we start from the root of the tree. We compare the values of the root attribute with the record’s attribute. On the basis of comparison, we follow the branch corresponding to that value and jump to the next node.
# About Project
In this task we have to work with DecisionTreeClassifier Algorithm(Ensemble Learning) with the Same IRIS dataset and Visualise it to understand it more easily


