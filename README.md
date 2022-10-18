# twittter_scarpping_without_api
A simple Twitter scarper without using Twitter API (used snscrape lib)

## About

This web application is designed to parse basic twitter account information such as (username, number of followers, number of friends and account description). In addition, for each user, you can get information about the last 10 tweets from the current date, with date and time. For a correct search, you must specify the link in its entirety.

List example: <br>
https://twitter.com/tyler <br>
https://twitter.com/novogratz <br>
https://twitter.com/elonmusk <br>
https://twitter.com/MessariCrypto <br>
https://twitter.com/CryptoHayes

After submitting the form, you get general information about the requested accounts, and when you click on an account, the last 10 tweets are displayed.

To start a new search, use the "Back" button.

## Tech Stack

The project is currently running on the following versions:

* Python 3.10.6
* Django 4.1.2
* Snscrape 0.4.3.20220106

## Running Locally

To run the project locally first you need to clone the repository:

```
git clone https://github.com/MrRom4ke/twittter_scarpping_without_api.git
```

Create a virtualenv:

```
virtualenv venv -p python3
```

Install the development requirements:

```
pip install -r requirements/local.txt
```

Run the local server:

```
python manage.py runserver
```

## License

The source code is released under the [MIT License](https://github.com/vitorfs/parsifal/blob/master/LICENSE).

### Авторы
Андрей, Стёпа, Лера и Максим 
