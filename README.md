# A Scrapy scraper for Books on [rokomari.com](https://www.rokomari.com)

## Overview

This repo contains code for scrapy bot (scraper) which scrapes book information from one of the largest online bookshop in Bangladesh, [**rokomari.com**](https://www.rokomari.com)

The scraper collected **3 Lac+** book information from [**rokomari.com**](https://www.rokomari.com)

## Setup

To setup this bot in your local machine follow the followings:

First, you'll probably need to create a virtual environment (venv). It's always safer and a good idea to run any project under a virtual environment. Go to a directory where you want to create your venv and open terminal/cmd there
and paste or write this command:

```bash
python -m venv <directory name>
```
For example, if you name your directory 'venv', then your command should look like this

```bash
python -m venv venv
```
Btw, make sure to have python installed :p

Now that you have created a virtual environment you need to activate it. To activate the virtual environemnt, and assuming its' name is `venv`. use the command

On **Linux** / **Mac**
```bash
$ source venv/bin/activate
```

On **Windows**
```cmd
# In cmd.exe
venv\Scripts\activate.bat
# In Powershell
venv\Scripts\activate.psl
```

Next, On the current working directory clone this repo using,

```bash
git clone https://github.com/Tasfiq-K/rokomari_scraping.git
```
Then go inside the `rokomari_scraping` directory using

```bash
cd rokomari_scraping
```
and install the dependencies

```bash
pip install -r requirements.txt
```

If you've come to this far, then you have setup your working environment and installed the dependencies required to run the bot.

Now, to actually run the bot you'll have to go one directorie deep, where the `scrapy.cfg` file resides. Use

```bash
cd rokomariScraper
```
to go there.

Now you can actually run the bot as is (if you want that).

To run the bot use the scrapy command line tools

```bash
scrapy crawl rokomariBooks -o file_name_of_your_choice.extension
```

The `scrapy crawl rokomariBooks` will start crawling but if you want the output in a file like csv or json, you should use a file name (any name you prefer) and proper file extension like `.csv` or `.json`. For example

```bash
scrapy crawl rokomariBooks -o book_data.csv
```

this will start crawling and will generate `csv` file named `book_data` in your current working directory.

That's it. Your bot will scrape book data from rokomari.com.

## Code

If you want to modify the code, then go to the `spiders` directory where there's a python file called `rokomariBooks.py` where the source code for this scraper lives. Also checkout the `items.py` to deal with the data fields.

# Thank you.
