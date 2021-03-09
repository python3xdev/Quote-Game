# First Web Scraping Project

This is my first web scraping project, I am also new to working with csv files. So this might not be the most efficient way to complete the given task.  
Goal:  
&nbsp;&nbsp;&nbsp;&nbsp;1) Scrape this website 'http://quotes.toscrape.com' and retrieve the following data...  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;a) From each quote box scrape the quote it self.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;b) The authors name  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;c) Go to their biography page and scrape the birth date and location.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;d) And repeat this for every item on the current page and all of the other pages as well.  
&nbsp;&nbsp;&nbsp;&nbsp;2) Make a quote guessing game where the user must guess a randomly chosen quote from a huge list of items, the user has 4 tries to guess the author, and they get hints along the way.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;a) Hint 1 will return the authors birth date and location.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;b) Hint 2 will return the first letter of the authors first name.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;c) Hint 3 will return the first letter of the authors last name.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;d) If the user fails the 4th try, the user will see: 'Sorry you lose. The author was: (author name)'  
&nbsp;&nbsp;&nbsp;&nbsp;3) And while were at it, we can save all this data to a csv file.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;a) 1st column: Quote  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;b) 2nd: By Whom  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;c) 3rd: URL (this will be the biography page of the author)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;d) 4th: Birth Date  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;e) 5th: Birth Location  