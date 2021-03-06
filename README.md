<p align="center">
	<h3 align="center"> An application tool written in python, used to extract and browse the data available on the websites. </h3>
</p>


## Table of Contents

- [Problem](#problem)
- [Prerequisite](#prerequisite)
- [Setup](#setup)
- [FrameWork](#FrameWork)
- [Authors](#authors)
- [Getting Help](#getting-help)


## Problem

- The python script will hit the URLs [http://www.thelearningpoint.net/system/app/pages/search?scope=search-site&q=school&offset=0](http://www.thelearningpoint.net/system/app/pages/search?scope=search-site&q=school&offset=0). And it'll hit all the link available on that particular site.
When the script will run using scrapy utility it'll fetch the name and email-ids of all the schools 
listing at the site. With the developed python script (using Scrapy) we can stored the same into CSV format.  


## Main Running Python Script 

- Navigate to `/Web_Scraping/Web_Scraping/spiders/edugorillatask.py`


## Files Description

- `/Web_Scraping/scrapy.cfg` : deploy configuration file
- `/Web_Scraping/Web_Scraping/__init.py__` : project's Python module, we'll import our code from here.
- `/Web_Scraping/Web_Scraping/items.py` : project items definition file.
- `/Web_Scraping/Web_Scraping/pipelines.py` : project pipelines file.
- `/Web_Scraping/Web_Scraping/settings.py` : project setting file.
- `/Web_Scraping/Web_Scraping/spiders/__init.py__` : a directory where we'll later put our spiders.


## Prerequisite
- Python 2.7/3. 
- `Twisted Python package` (An asynchronous networking framework written in Python. An extensible framework for Python programming).
- `Scrapy/BeautifulSoup Framework`.
- Background of XML, HTML, CSS.
- Works on Linux, Windows, Mac OSX, BSD

## Setup

- Clone the directory into your local machine (using `git clone <name_of_application>`).
- Navigate to the cloned directory (`cd Web-Scrapper`).
- Move to the `Spiders` directory.
- Run `scrapy runspider edugorillatask.py<name_of_pythonScript>` 
- To store the file in csv Format Run 
		`scrapy runspider edugorillatask.py -o output.csv`
- View the output using `cat output.csv`		
- You can navigate to the project directory and open the output.csv file with your supported application also.


## Framework 

# Scrapy
- Scrapy is an application framework written in python, basically used to crawling websites and extracting structured 
data which can be used a wide range of the applications and make the work easier. It's also can be used to extract the 
data using APIs. 

- For more information about installing, creating and working on web-scraping using Scrapy, Please visit:
<a href="https://doc.scrapy.org/en/latest/intro/overview.html" target="_blank"> https://doc.scrapy.org/en/latest/intro/overview.html </a>

- The minimal versions which Scrapy is tested against are: <br />
	`Twisted 14.0` <br />
	`lxml 3.4` <br />
	`pyOpenSSL 0.14`
