# Chapter 4: Web Scraping
## Summary:

Big data. Big deal. In this chapter, we're going to take a gander at a subject
known as "Web Scraping." What's that you ask? Is that when you crawl the
Internet for days trying to escape the dark web? No, that's called
poor judgement. Web scraping is when a script or program retrieves information
from a website for processing, analyzing, or organizing.

So why did I mention big data? Well, since the computer is retrieving the data
from the website(s), it can get that data and crunch through it pretty quickly.
So, naturally, web scraping is popular among those seeking the usage and analytics
of "big data." You could grab the numbers and statistics from a large collection
of websites, store it in a neat data structure, and produce whatever your heart
desires--graphs, charts, tables, etc. manufactured from the data.

Maybe handling a sea of data seems daunting to you though. Perhaps we could
study the more common applications of web scraping? Sure! Web scraping can be
used for myriad tasks, such as:
  - Sports statistics
  - Social media trends
  - Online product comparisons
  - Stock data aggregation
  - Crime statistics

So, in this chapter we'll get to look at the basics of scraping the web using
a pretty sweet third-party Python package called *BeautifulSoup*.

---

## Content:

Alright, so first we need to install *BeautifulSoup* for Python. The newest
version, as of the writing of this book, is v4.4.1, which supports both Python 2.6+
and Python 3. You can install the package with whatever package manager you prefer,
such as *pip* or *easy_install*, like so:

```
pip install beautifulsoup4
```

```
easy_install beautifulsoup4
```

Or, if you don't like that method, you can always visit the website for the package
at [https://www.crummy.com/software/BeautifulSoup/bs4/download/](https://www.crummy.com/software/BeautifulSoup/bs4/download/).

To test that you installed the package successfully, you can simply start the
Python interpreter, and run the following import command:

```python
from bs4 import BeautifulSoup
```

If that import command completed without error, you're setup and ready to scrape!

---

Now then, before we actually start using the *bs4* package, let's first take
a look at the general process of web scraping, as follows:
  1. Study the format of target webpage
  2. Retrieve content of webpage (an HTTP request)
  3. Search the content for specific data based off the content format
  4. Do stuff with the data found in the search

Okay, let's put this into practice. This first example is so simple, we don't
need to use *bs4*.

```python
# Example 4-1 (scrape0.py):
import requests
page = requests.get('http://github.com/zach-king/')
print(page.content)
```

Here, we're using the builtin *requests* package from Python (2 and 3). After
importing the package, we use the `get()` function to retrieve the HTML document
that the server sends back for my GitHub profile, at [http://github.com/zach-king](http://github.com/zach-king).

After storing that in a variable called `page` we can print its contents out
and verify the same HTML is received this way as when we view it in a web browser.
Keep in mind that you can view the source code of a webpage in your browser by
right clicking and selecting either *inspect element* or *view source* (I recommend
  using *inspect element* since you can more accurately tell what elements you are
  looking at).

---

## Wrap Up:
