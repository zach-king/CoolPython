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

---

## Wrap Up:
