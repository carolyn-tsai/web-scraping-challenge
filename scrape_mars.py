# Import dependencies

import pandas as pd
from bs4 import BeautifulSoup
import requests
from splinter import Browser
import time

# Initialize browser

def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}

    # For Mac Users:
    # executable_path = {"executable_path": "/usr/local/bin/chromedriver"}

    return Browser('chrome', **executable_path, headless=False)

# The following function will scrape various Mars related websites for data and return a Python dictionary of the data collected

def scrape():

    # Initialize browser

    browser = init_browser()

    # Create an empty dicitonary to store scraped Mars data

    mars_scrapped_data = {}

    ############################

    # NASA Mars News

    nasa_url = "https://mars.nasa.gov/news"
    browser.visit(nasa_url)
    time.sleep(3)
    nasa_html = browser.html
    nasa_soup = BeautifulSoup(nasa_html, 'html.parser')
    news_title = nasa_soup.find("div", class_="content_title").find("a").text
    news_p = nasa_soup.find("div", class_="article_teaser_body").text

    mars_scrapped_data["news_title"] = news_title
    mars_scrapped_data["news_p"] = news_p

    ############################

    # JPL Mars Space Images - Featured Image

    mars_images_url_page = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(mars_images_url_page)
    time.sleep(3)
    image_html = browser.html
    image_soup = BeautifulSoup(image_html, 'html.parser')
    image_info = image_soup.find("a", class_="button fancybox")
    image_med_size = image_info.attrs["data-fancybox-href"]
    image_large_size = (image_med_size.replace("mediumsize", "largesize")).replace("_ip", "_hires")
    featured_image_url = "https://www.jpl.nasa.gov" + image_large_size

    mars_scrapped_data["featured_image"] = featured_image_url

    ############################

    # Mars Weather

    twitter_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(twitter_url)
    time.sleep(3)
    twitter_html = browser.html
    twitter_soup = BeautifulSoup(twitter_html, 'html.parser')
    twitter_info = twitter_soup.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text

    mars_scrapped_data["twitter_mars_weather"] = twitter_info

    ############################

    # Mars Facts

    mars_facts_url = "https://space-facts.com/mars/"
    mars_data = pd.read_html(mars_facts_url)
    time.sleep(3)
    mars_data_df = mars_data[0]
    mars_data_df.columns = ["Description", "Value"]
    mars_data_df.set_index("Description", inplace=True)
    mars_table = mars_data_df.to_html()
    mars_table = mars_table.replace("\n", "")

    mars_scrapped_data["table_mars_data"] = mars_table

    ############################

    # Mars Hemispheres
    mars_hemi_images_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(mars_hemi_images_url)
    time.sleep(3)
    mars_hemi_html = browser.html
    mars_hemi_soup = BeautifulSoup(mars_hemi_html, "html.parser")
    mars_hemis = mars_hemi_soup.find_all("div", class_="item")

    hemisphere_image_urls  = []

    for hemisphere in mars_hemis:
        main_url = "https://astrogeology.usgs.gov"
        mars_hemi_dict = {}
        hemi = hemisphere.find("h3").text
        partial_url = hemisphere.find("a", class_="itemLink product-item")["href"]
        hemi_url = main_url + partial_url
        browser.visit(hemi_url)
        time.sleep(3)
        image_html = browser.html
        image_soup = BeautifulSoup(image_html, "html.parser")
        partial_image_url = image_soup.find("img", class_="wide-image")["src"]
        mars_hemi_dict["Title"] = hemi
        mars_hemi_dict["img_url"] = main_url + partial_image_url
        hemisphere_image_urls.append(mars_hemi_dict)

    mars_scrapped_data["hemispheres_data"] = hemisphere_image_urls

    browser.quit()

    return mars_scrapped_data





