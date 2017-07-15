"""
	A python script: Used for extracting and browsing useful information availble on the websites.
	@Author: Raghuvar Prajapati

"""


import re
import scrapy
from scrapy.exceptions import CloseSpider


class edugorillataskSpider(scrapy.Spider):
	name = 'edugorillatask'
	allowed_domains = ["thelearningpoint.net"]	
	start_urls = []
	start_urls.extend(["http://www.thelearningpoint.net/system/app/pages/search?scope=search-site&q=school&offset=%d/" % j for j in range(10)])

	"""
	Parse function is the most important function in any of the web scrapping task. Here will define a parse method
	which will parse all the contents inside the elements of a h3 tag, 'a' tag and href tag.
	"""
	#
	def parse(self, response):	
		url_list = response.xpath('//h3/a/@href').extract();
		for link in url_list:
			complete_url = response.urljoin(link)
			yield scrapy.Request(complete_url,callback=self.parseDetails)

	"""
	ParseDetails function will first select the data using css-selectors. So, response.xpath will return a
	SelectorList. 
	XPath is a language for selecting nodes in XML documents, which can also be used with HTML. 
	"""
	def parseDetails(self, response):
		try:
			details = response.xpath('//div/b/font/text()').extract()
			email = self.extractSubString(details[6],'Email:', ', ');

			#get the email address of the schools if it's a valid email address
			if(self.validateEmail(email)):
				yield {'Name': details[0], 'Email-id':email}

		# raise is a keyword which is used to get the errors as an exceptions in python. Throwing an error.
		# Printing a fancy error message if can't parse the link.
		except IndexError:
			raise CloseSpider("reason=Canceled, Can not parse one of the links, Please refine your search")

	
	"""
	Function "extractSubString" will extract a particular substring from the input string
	(between the starting string(start) and ending string(end))
	"""
	
	def extractSubString(self,inputStr,start,end):
		return inputStr[inputStr.find(start)+len(start):inputStr.rfind(end)]


	# To check the correct format of the email of any of the schools listing on the link.
	def validateEmail(self, email):
		if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
			return 1
		return 0

