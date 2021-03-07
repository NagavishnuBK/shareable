
# import all the required packages,
# import requests, render_template, redirect and request components of flask package
# and import app module from app package

import requests
import os
import subprocess
from flask import render_template, redirect, request, render_template_string

from app import app

# This segment is executed when the rendered html page routes the site to the same web address as its
@app.route('/')
def index():
    # this has a return statement that renders a designed html page with file name as "basic.html"
    return render_template('basic.html')

@app.route('/start', methods=['POST'])
def redirecting():
    return redirect("http://127.0.0.1:5000/start1")

@app.route('/start1', methods=['POST','GET'])
def render_plate():
#    f = open("E:\\Internship\\Lavelle_Networks\\OpenNESS\\Learning\\Learn 01-03-2021\\flaskapp\\app\\templates\\test_file1.html","w")
#    cwd = os.getcwd()
#    cwd = cwd + "\\app\\templates\\test_file1.html"
#    f = open(cwd,"w")
    hostname = subprocess.check_output((['hostname']))
    s = ""
    s = s + "<!DOCTYPE html>\n"
    s = s + "<html>\n"
    s = s + "<body>\n\n"
    s = s + "<h1>Flask app</h1>\n"
    s = s + "<p>To understand and learn Kubernetes.</p>\n\n"
    s = s + "<p>You just pinged the host: " + str(hostname)[2:-5] + "</p>\n"
    s = s + "</body>\n"
    s = s + "</html>"
#    f.write(s)
#    f.close()
    return render_template_string(s)

