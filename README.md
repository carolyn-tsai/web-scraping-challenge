# web_scraping_challenge

## Mission to Mars


For this assignment, I built a web application that scrapes various websites for data related to the Mission to Mars. The information collected is displayed on a single HTML page. 


### Data Scarping

The following websites were scraped:

- NASA Mars News Site (https://mars.nasa.gov/news) 
- JPL Featured Space Image site (https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars)
- Mars Weather twitter account (https://twitter.com/marswxreport)
- Mars Facts webpage (https://space-facts.com/mars)
- USGS Astrogeology site (https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars)

### MongoDB and Flask Application

MongoDB and Flask templating were used to create a new HTML page that displays all of the information that was scraped from the URLs above.

- My Jupyter Notebook code was converted into a Python script called *scarpe_mars.py* with a function called *scrape* that executes all of the scraping code from the script and returns one Python dictionary containing all of the scraped data.
- A route called */scrape* was created that imports the *scrape_mars.py* script and calls the *scrape* function
  - The return value is stored in MongoDB as a Python dictionary
- Another root route was created that queries the Mongo database and passes the mars data into an HTML template that displays the data
- A template HTML file called *index.html* will take the mars data dictionary and display all of the data in the appropriate HTML elements

### Tools Used:

- Jupyter Notebook
- BeautifulSoup
- Pandas
- Python
- Requests/Splinter
- Flask

-----------------------------------------------------------------------------------------------------------

### Resources:
- https://realpython.com/beautiful-soup-web-scraper-python/
- https://towardsdatascience.com/how-to-web-scrape-with-python-in-4-minutes-bc49186a8460
- https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/
- https://www.youtube.com/watch?v=r_xb0vF1uMc
- https://help.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax
- https://docs.mongodb.com/manual/reference/method/db.collection.find/
- https://flask.palletsprojects.com/en/1.1.x/
- https://stackoverflow.com/
- https://www.geeksforgeeks.org/