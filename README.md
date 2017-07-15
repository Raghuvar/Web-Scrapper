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

## Prerequisite
- Python 2/3. 
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
- You can navigate to the project directory and open the output.csv file with your supported application.


## Framework 

# Scrapy
- Scrapy is an application framework written in python, basically used to crawling websites and extracting structured 
data which can be used a wide range of the applications and make the work easier. It's also can be used to extract the 
data using APIs. 

- For more information about installing, creating and working on web-scraping using Scrapy, Please visit:

<br />
<a href="https://doc.scrapy.org/en/latest/intro/overview.html" target="_blank"> https://doc.scrapy.org/en/latest/intro/overview.html </a>


## Author

- Raghuvar Prajapati, <br />
  Undergrad, B.Tech(CSE) <br />
  IIIT-Vadodara


## Getting Help

If you need any help installing, using the application, or any suggestions please feel free to drop a mail to : <br />
 <a href="raghuvarprajapati@gmail.com">raghuvarprajapati@gmail.com</a>.
