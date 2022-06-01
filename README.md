# InfoSec_BAC

This project demonstrates broken and working access control on a flask app.
for this, we have two flask apps that , while looking alike, are based on two different kinds of access.


The first example (broken_access_control) only checks for the entered user-data to be correct and continues to identify the user using a URL argument.
This argument can be altered to see the profile of a different user.

The second example (working_access_control) uses the flask-login package to properly authenticate the user. When the user accesses the profile page, a session cookie, sent by a user is used to properly identify and authenticate the already logged in user.

User credentials for testing:
Paul:V3ryS3cr3t!
Moritz:Sup€r€cr€t!

These can be used to test and try to find out the favourite singer of the other user without using its credentials.

## Install required package(s)
```
pip install -r requirements.txt
```

## Configure the environment and start the Flask app

Bash:
```
    export FLASK_APP=broken_access_control (for negative example)
    export FLASK_APP=working_access_control (for positive example)
    export FLASK_ENV=development (optional)
    flask run
```
CMD:
```
    set FLASK_APP=broken_access_control (for negative example)
    set FLASK_APP=working_access_control (for positive example)
    set FLASK_ENV=development (optional)
    flask run
```
Powershell:
```
    $env:FLASK_APP = "broken_access_control" (for negative example)
    $env:FLASK_APP = "working_access_control" (for positive example)
    $env:FLASK_ENV = "development" (optional)
    flask run
```