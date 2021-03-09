"""
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
"""

import requests
from bs4 import BeautifulSoup
from csv import writer
from random import choice

response = requests.get('http://quotes.toscrape.com')
soup = BeautifulSoup(response.text, 'html.parser')
new_page_slug = soup.find(class_='next')('a')[0]['href']
quotes = []

scrape = True

def refactor_csv_file():
	text = open('quotes.csv', 'r')
	text = ''.join(i for i in text).replace(';', '.')
	x = open('quotes.csv', 'w')
	x.writelines(text)
	x.close()

with open('quotes.csv', 'w') as file:
	csv_writer = writer(file)
	csv_writer.writerow(['Quote','By Whom','URL','Birth Date','Birth Location'])
	while scrape:
		for i in range(0, len(soup.find_all(class_='quote'))):
			quote_class = soup.find_all(class_='quote')[i]
			quote = quote_class('span')[0].get_text()
			name = quote_class('small')[0].get_text()
			url = quote_class('a')[0]['href']
			birth_info = BeautifulSoup(requests.get(f'http://quotes.toscrape.com{url}').text, 'html.parser')('p')[1].find_all('span')
			birth_date = birth_info[0].get_text()
			birth_location = birth_info[1].get_text()
			quotes.append([quote, name, url, birth_date, birth_location])
			csv_writer.writerow([f'{quote}', name, url, birth_date, birth_location])
		try:
			response = requests.get(f'http://quotes.toscrape.com{new_page_slug}')
			soup = BeautifulSoup(response.text, 'html.parser')
			new_page_slug = soup.find(class_='next')('a')[0]['href']
		except TypeError:
			# "Successfully Scraped All Web Pages..."
			scrape = False

refactor_csv_file()

def new_game(value):
	if value[0] == 'y':
		print(f'---------------------------------------------NEW GAME----------------------------------------------')
		game()
	else:
		exit()

def hint(num):
	if num == 1:
		return f'---1st Hint:\nBorn: {chosen_quote[3]} {chosen_quote[4]}'

	if num == 2:
		name_list = chosen_quote[1].split()
		first = name_list[0]
		return f'---2nd Hint:\nThe first letter of their first name is: {first[0]}'

	if num == 3:
		name_list = chosen_quote[1].split()
		last = name_list[1]
		return f'---3rd Hint:\nThe first letter of their last name is: {last[0]}'

	if num == 4:
		return 'No more hints for you!'

def reveal_answer():
	return f'Sorry you lose. The author was: {chosen_quote[1]}'

def game():
	global chosen_quote
	chosen_quote = choice(quotes)
	guess_count = 4
	hint_level = 1
	print(f"{chosen_quote[0]}")
	user_guess = ''
	while user_guess != chosen_quote[1] and guess_count != 0:
		user_guess = input(f'Guess who said the above quote (Guesses left: {guess_count}): ')
		if user_guess != chosen_quote[1]:
			print(hint(hint_level))
			guess_count -= 1
			hint_level += 1
	if user_guess == chosen_quote[1]:
		print("You Win!")
		guess_count = 4
		hint_level = 1
		chosen_quote = choice(quotes)
		play_again = input('Do you want to play again (y/n): ')
		new_game(play_again)
	elif guess_count <= 0:
		result = reveal_answer()
		print(result)
		guess_count = 4
		hint_level = 1
		play_again = input('Do you want to play again (y/n): ')
		new_game(play_again)

if __name__ == '__main__':
	game()