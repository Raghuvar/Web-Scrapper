<p align="center">
	<h3 align="center"> An application tool written in python, used to extract and browse the data available on the websites. </h3>
</p>
=======


## Table of Contents

- [Prerequisite](#prerequisite)
- [Setup](#setup)
- [FrameWork](#FrameWork)
- [Authors](#authors)
- [Getting Help](#getting-help)

=======

## Problem

## The python script will hit the URLs [http://www.thelearningpoint.net/system/app/pages/search?scope=search-site&q=school&offset=0](http://www.thelearningpoint.net/system/app/pages/search?scope=search-site&q=school&offset=0). And it'll hit all the link available on that particular site.
When the script will run using scrapy utility it'll fetch the name and email-ids of the listing schools 
available in the site. Finally it can be stored into CSV format.  

## Prerequisite
- Python 2/3 
- Twisted Python package (An asynchronous networking framework written in Python. An extensible framework for Python programming)
- Scrapy/BeautifulSoup Framework
- Background of XML, HTML

=======

## Setup

- Clone the directory into your local machine (using git clone <https://github.com/uname/yourapplication.git>.
- Navigate to the cloned directory (cd Web-Scraper).
- Move to the `Spiders` directory.
- Run `scrapy runspider edugorillatask.py<name_of_pythonScript>` to run the python script using scrapy framework
- To store the file in csv Format Run 
		`scrapy runspider edugorillatask.py -o output.csv`
- View the output using `cat output.csv`		
- You can navigate to the project directory and open the output.csv file with your supported application.

=======

## Framework 

# Scrapy
- Scrapy is an application framework written in python, basically used to crawling websites and extracting structured 
data which can be used a wide range of the applications and make the work easier. It's also can be used to extract the 
data using APIs. 

- For more information about installing, creating and working on web-scraping using Scrapy, Please visit:
[https://doc.scrapy.org/en/latest/intro/overview.html](https://doc.scrapy.org/en/latest/intro/overview.html)

=======

## Author

- Raghuvar Prajapati, 
  Undergrad, B.Tech(CSE)
  IIIT-Vadodara

=======

## Getting Help

If you need any help installing, using the application, or any suggestion please do drop a mail  to <a href="raghuvarprajapati@gmail.com">raghuvarprajapati@gmail.com</a>.
