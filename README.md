# Ecommerce Nursery

### Problem Statement
Create an online nursery marketplace API where users can signup, login, view, and order plants available in different nurseries.

### Approach 
Created a website where owner and customer is users. Owner can see plant, add plant, see their orders. Customer can buy plant.

### API's
1. /register : customer and owner can signup.
2. /login :  customer and owner can login.
3. /logout : simple logout.
4. /add_plant : nursery owner can add plants.
5. /see_plant : nursery owner can see their added plants.
6. /see_order : nursery owner can see thier orders.
7. /place_order : customer can place order.
8. / : list all plants.

### Technical Stack used
1. Used Django framework ( all models are there in model.py , all views are there in view folder)
2. Ajax is also used.

### Steps to run
1. Create a python3 virtual enviornment and activate it.
2. Install the requirements via `pip install -r requirements.txt`.
3. Move to nursery folder.
4. Run `python manage.py makemigrations`.
5. Run `python manage.py migrate`
6. Run `python manage.py createsuperuser` then add credentials (this is used to access the database in '/admin' endpoint).
4. Finally run `python manage.py runserver`.

### Deployment
deployment can be done in pythonanywhere cloud server or Heroku server


### sample video link
https://drive.google.com/file/d/1i01vMjdZ2ffS4f7Sa2AGgamPXAvv4nXs/view?usp=sharing