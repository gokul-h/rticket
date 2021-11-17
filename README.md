# R Ticket
A Railway Reservation and Management System
---
Features:
1. Search train between stations.
2. Search train by name.
3. Search train by number.
4. Book a train.
5. View order history.
---
Instructions to use: 
1. Download Zip folder
2. Extract and open in an IDE of your Choice
3. Install Python and create a virtual environment
4. Install requirements.txt
```commandline
pip install -r requirements.txt
```
5. Install PostgreSQL and create database rticket
6. You have to add train data using PGAdmin panel from CSV file
7. Change database settings in settings.py
8. Add RazorPay keys to below files \
payment/views.py \
templates/order/checkout.html
9. Run python migrations
```commandline
python manage.py makemigrations
python manage.py migrate
```
10. Start the Server
```commandline
python manage.py runserver
```
---
Backend - Django (Python) \
Frontend - HTML CSS Bootstrap JS JQuery \
Database - PostgreSQL \
Payment - RazorPay \
Hosting - Heroku 