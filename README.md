# Shop Score Page

This service allows you to receive information about the processing of orders in the online store.
Information update occurs every 10 seconds. When this occurs, the following data is displayed:

* Maximum waiting time for orders not yet processed
* The number of unprocessed orders
* Number of orders processed today

In addition, there is a color display when displaying the maximum waiting time for orders that have not yet been processed:

* Green color - the waiting time does not exceed 7 minutes
* Yellow color - the waiting time does not exceed 30 minutes
* Red color - waiting time exceeds 30 minutes

Online version of service is deployed on Heroku and available [here](https://shop-score-info.herokuapp.com/).

# Quickstart

For service launch on localhost need to install Python 3.5 and then install all dependencies:

```bash

$ pip install -r requirements.txt

```

To access the online store database, you must specify its URI:

```bash

$ export DATABASE_URI='postgresql://username:password@database.host:port/database_name'

```

Usage:

```bash

$ python3 server.py

```

Then open page [localhost:5000](http://localhost:5000) in browser.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
