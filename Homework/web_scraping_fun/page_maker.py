#!/usr/bin/env python
# coding: utf-8

import pymongo
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mission_to_mars



app = Flask(__name__)
mongo = PyMongo(app, uri = "mongodb://localhost:27017/mars_page")


# reroutes the code to index.html in the template folder
@app.route("/")

def home():
    scrapeDict = mongo.db.scrapeDict.find_one()
    return render_template('index.html', scrapeDict = scrapeDict)


# scrape() function defined in mission_to_mars program


@app.route( "/scrapeItAll" )

def scrapeItAll():
    scrapeDict = mongo.db.scrapeDict
    marsData = mission_to_mars.scrape()
    scrapeDict.update(
        {}, 
        marsData,
        upsert = True
    )
    
    return redirect("/")
    

if (__name__ == "__main__"):
    app.run(debug = True)
    #app.run()

