# Emerging Technology Project
# Author: Cathal Donohoe - G00344919

##  How to run
Create a new folder and open a Command Prompt in that directory. </br>
Clone the github link, "https://github.com/CathalDonohoe/Jupiter". </br>
Change directory into the new folder created. </br>
From here run "docker build -t (name of file) ." </br>
After this has been built, run this "docker run -d -p 5000:5000 (name of file)" </br>
Load up your browser, and navigate to "http://localhost:5000/" </br>
This will boot up the web service page and will allow us to enter the speed value and get the predicted power from the Jupyter Notebook </br>


$ export FLASK_APP=webService.py  
$ flask run  
 * Running on http://127.0.0.1:5000/
