# Protocols & HTTP
 **Authors**: Ben Hurst & J Christie
 **Version**: 1.0.0
 ## Overview
 Basic HTTP server using the Python standard library and cowpy.
 ## Getting Started
    1) Clone or fork repo from github.
    2) Run ```python server.py``` in the terminal to spin up the server.
    3) Using the http client of your choice (I reccomend Postman), you can hit the server with various requests (refer to API section below)
    4) Malformed endpoints and requests without query strings will return appropriate error codes

 ## Architecture
Python 3.7, Pytest, http.server, urllib.parse, os, cowpy
GitHub
 ## API
 - GET: http://localhost:5000/ -> Returns homepage
 - GET: http://localhost:5000/cow?msg=hiii -> Returns steggy saying hiii
 - POST: http://localhost:5000/cow?msg=hiii -> Returns JSON
 ## Change Log
 08-21-2018 17:50 Basic Functionality Done

 08-21-2018 10:30 Added more tests
 ## License
This project is licensed under the MIT license
