# Emerging Technology Project
# Author: Cathal Donohoe 
# Student Number: G00344919
# Email: G00344919@gmit.ie

## The Brief
In this project you must create a web service that uses machine learning to make pre-dictions based on the data set powerproduction available on Moodle.  The goal is toproduce a model that accurately predicts wind turbine power output from wind speed values, as in the data set.  You must then develop a web service that will respond with predicted power values based on speed values sent as HTTP requests.  Your submission must be in the form of a git repository containing, at a minimum, the following items: </br>
1.  Jupyter  notebook  that  trains  a  model  using  the  data  set.   In  the  notebook  youshould explain your model and give an analysis of its accuracy. </br>
2.  Python script that runs a web service based on the model, as above. </br>
3.  Dockerfile to build and run the web service in a container. </br>
4.  Standard items in a git repository such as a README. </br>


## The Project
The goal of this project is to create a webservice that uses machine learning to make predictions based on the data set powerproduction provided to us by our lecturer. </br>
We use Tensorflow and Keras to do this. </br>
There is a jupyter notebook that computes and explains the machine learning for the web service to do. </br>
There is a webservice.py that is a Flask API that takes in the prediciton model created in the notebook. </br>
There is a html file that is used by the webservice. </br>
The docker file builds and runs the web service in a container. </br>
</br>
##  How to run
Create a new folder and open a Command Prompt in that directory. </br>
Clone the github link, "https://github.com/CathalDonohoe/Jupiter". </br>
Change directory into the new folder created. </br>
From here run "docker build -t (name of file) ." </br>
After this has been built, run this "docker run -d -p 5000:5000 (name of file)" </br>
Load up your browser, and navigate to "http://localhost:5000/" </br>
This will boot up the web service page and will allow us to enter the speed value and get the predicted power from the Jupyter Notebook </br>

## Without Docker
</br>
Open command prompt in the directory of the file. </br>
Run this line: set FLASK_APP=webService.py  </br>
After that run the following: python -m flask run </br>
Then move to your browser and enter in the following link: http://127.0.0.1:5000/ </br>
</br>

# End
