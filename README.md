# First Web Scraping Project

This is my first web scraping project, I am also new to working with csv files. So this might not be the most efficient way to complete the given task.  
Goal:  
	1) Scrape this website 'http://quotes.toscrape.com' and retrieve the following data...  
		a) From each quote box scrape the quote it self.  
		b) The authors name  
		c) Go to their biography page and scrape the birth date and location.  
		d) And repeat this for every item on the current page and all of the other pages as well.  
	2) Make a quote guessing game where the user must guess a randomly chosen quote from a huge list of items, the user has 4 tries to guess the author, and they get hints along the way.  
		a) Hint 1 will return the authors birth date and location.  
		b) Hint 2 will return the first letter of the authors first name.  
		c) Hint 3 will return the first letter of the authors last name.  
		d) If the user fails the 4th try, the user will see: 'Sorry you lose. The author was: (author name)'  
	3) And while were at it, we can save all this data to a csv file.  
		a) 1st column: Quote  
		b) 2nd: By Whom  
		c) 3rd: URL (this will be the biography page of the author)  
		d) 4th: Birth Date  
		e) 5th: Birth Location  