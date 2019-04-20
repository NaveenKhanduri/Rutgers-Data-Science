#!/usr/bin/env python
# coding: utf-8


import pymongo
from splinter import Browser
from bs4 import BeautifulSoup
from flask import Flask, render_template, redirect
import os


def init_browser():
    executable_path = {"executable_path": os.getcwd() + "/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrapenews():
    listings = {}
    
    brrowser = init_browser()
    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    
    brrowser.visit(url)

    html = brrowser.html
    soup = BeautifulSoup(html, "html.parser")
    
    #locates all div containers of class "list_text". Basically, the twitter updates.
    chunks = soup.find_all("div", class_ = "list_text")
        
    for chunk in chunks:
        
        header = chunk.find('a').text
            
        body = chunk.find("div", class_ = "article_teaser_body").text
        
        listings[header] = body
    brrowser.quit()
    news = []
    news.append(list(listings.keys())[0])
    news.append(list(listings.values())[0])
    return news


def scrapeimg():

    brrowser = init_browser()
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    brrowser.visit(url)

    html = brrowser.html
    soup = BeautifulSoup(html, "html.parser")
    
    
    chunk = soup.find("div", class_ = "carousel_container")
    link = chunk.find("a")["data-fancybox-href"]
    imagelink = "https://www.jpl.nasa.gov" + str(link)

    brrowser.quit()
        
    return imagelink


#test to see if it works

#imagelink = scrapeimg()
#print(imagelink)

def scrapeweather():
    weatherurl = "https://twitter.com/marswxreport?lang=en"

    browser = init_browser()
    browser.visit(weatherurl)
    
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    
    chunk = soup.find("div", class_ = "js-tweet-text-container")
    text = chunk.find("p").text
    browser.quit()
    return text

#test

#weatherText = scrapeweather()
#print(weatherText)

def scrapehemi():
    
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    hemilist = {}
    browser = init_browser()
    browser.visit(url)
    
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    
    
    chunks = soup.find_all("div", class_ = "item")
    browser.quit()

    for chunk in chunks:
       
        title = chunk.find('h3').text
        
        imglink = chunk.find('a', class_ = "itemLink product-item")["href"]
        hemiurl = "https://astrogeology.usgs.gov" + imglink  
        
        """the image on the given page is lame and small, 
        so I did a tedious thing and rerouted to the web page for each  
        hemisphere to scrape the image on that page instead. """
        
        hemibrowser = init_browser()
        hemibrowser.visit(hemiurl)
        hemihtml = hemibrowser.html
        
        hemisoup = BeautifulSoup(hemihtml, "html.parser")
        hemilink = hemisoup.find('img', class_ = "wide-image")["src"]
        hemilist[title] = "https://astrogeology.usgs.gov" + hemilink
        hemibrowser.quit()
        
    return hemilist

#test
# scrapehemi()


#compressing all the scraping functions into one big function, and compiling the value as a dictionary
def scrape():
    scrapeDict = {}
    newslist = scrapenews()
    hemilist = scrapehemi()
    scrapeDict["mars_news_title"] = newslist[0]
    scrapeDict["mars_news_summary"] = newslist[1]
    scrapeDict["featured_image"] = scrapeimg()
    scrapeDict["mars_weather"] = scrapeweather()
    scrapeDict["hemisphere_images1"] = list(hemilist.values())[0]
    scrapeDict["hemisphere_images2"] = list(hemilist.values())[1]
    scrapeDict["hemisphere_images3"] = list(hemilist.values())[2]
    scrapeDict["hemisphere_images4"] = list(hemilist.values())[3]
    
    return scrapeDict

