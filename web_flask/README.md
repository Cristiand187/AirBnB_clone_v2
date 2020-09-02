# 0x04. AirBnB clone - Web framework

## :books: Resources
Read or watch:
* [What is a Web Framework?](https://intranet.hbtn.io/rltoken/_zBFEBzn5i35om4VT4Y3vQ)
* [A Minimal Application](https://intranet.hbtn.io/rltoken/aY1qkYlIbCDDULBN6nJNYA)
* [Routing](https://intranet.hbtn.io/rltoken/bAqYEpI4Ph-zLU7EM8iXjg)
* [Rendering Templates](https://intranet.hbtn.io/rltoken/mpA3GC0bX8WOHO15xUL2Yw)
* [Synopsis](https://intranet.hbtn.io/rltoken/-JZxrxnDnOID141U1qDcew)
* [Variables](https://intranet.hbtn.io/rltoken/-qwqxJ6YyQ7Z9JvvPIE1AA)
* [Comments](https://intranet.hbtn.io/rltoken/TsdwbqCk1utlpeOhc5eUFg)
* [Whitespace Control](https://intranet.hbtn.io/rltoken/NR5WFn7I6qUTh-b70Od69Q)
* [List of Control Structures](https://intranet.hbtn.io/rltoken/pyvwBzYKgoDeNQ6_QIwUsw)
* [Flask](https://intranet.hbtn.io/rltoken/k2C-4UmlYXgA6oMgO7fLgg)
* [Jinja](https://intranet.hbtn.io/rltoken/fid5cMJKYMaRJqL60PlUew)

---
## :bulb: Learning Objectives
What you should learn from this project:

* What is a Web Framework
* How to build a web framework with Flask
* How to define routes in Flask
* What is a route
* How to handle variables in a route
* What is a template
* How to create a HTML response in Flask by using a template
* How to create a dynamic template (loops, conditions…)
* How to display in HTML data from a MySQL database

---
## :computer: Task

### [0. Hello Flask!](./0-hello_route.py)
Write a script that starts a Flask web application:
 * Your web application must be listening on 0.0.0.0, port 5000
 * Routes:
	 * /: display “Hello HBNB!”
 * You must use the option strict_slashes=False in your route definition


### [1. HBNB](./1-hbnb_route.py)
Write a script that starts a Flask web application:
 * Your web application must be listening on 0.0.0.0, port 5000
 * Routes:
	 * /: display “Hello HBNB!”
 * /hbnb: display “HBNB”
 * You must use the option strict_slashes=False in your route definition


### [2. C is fun!](./2-c_route.py)
Write a script that starts a Flask web application:
 * Your web application must be listening on 0.0.0.0, port 5000
 * Routes:
	 * /: display “Hello HBNB!”
 * /hbnb: display “HBNB”
 * /c/<text>: display “C ” followed by the value of the text variable (replace underscore _ symbols with a space )
 * You must use the option strict_slashes=False in your route definition


### [3. Python is cool!](./3-python_route.py)
Write a script that starts a Flask web application:
 * Your web application must be listening on 0.0.0.0, port 5000
 * Routes:
	 * /: display “Hello HBNB!”
 * /hbnb: display “HBNB”
 * /c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
 * /python/(<text>): display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
	 * The default value of text is “is cool”
	 * You must use the option strict_slashes=False in your route definition


### [4. Is it a number?](./4-number_route.py)
Write a script that starts a Flask web application:
 * Your web application must be listening on 0.0.0.0, port 5000
 * Routes:
	 * /: display “Hello HBNB!”
 * /hbnb: display “HBNB”
 * /c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
 * /python/(<text>): display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
	 * The default value of text is “is cool”
 * /number/<n>: display “n is a number” only if n is an integer
 * You must use the option strict_slashes=False in your route definition


### [5. Number template](./5-number_template.py)
Write a script that starts a Flask web application:
 * Your web application must be listening on 0.0.0.0, port 5000
 * Routes:
	 * /: display “Hello HBNB!”
 * /hbnb: display “HBNB”
 * /c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
 * /python/(<text>): display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
	 * The default value of text is “is cool”
 * /number/<n>: display “n is a number” only if n is an integer
 * /number_template/<n>: display a HTML page only if n is an integer: 
	 * H1 tag: “Number: n” inside the tag BODY 
	 * You must use the option strict_slashes=False in your route definition


### [6. Odd or even?](./6-number_odd_or_even.py)
Write a script that starts a Flask web application:
 * Your web application must be listening on 0.0.0.0, port 5000
 * Routes:
	 * /: display “Hello HBNB!”
 * /hbnb: display “HBNB”
 * /c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
 * /python/(<text>): display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
	 * The default value of text is “is cool”
 * /number/<n>: display “n is a number” only if n is an integer
 * /number_template/<n>: display a HTML page only if n is an integer: 
	 * H1 tag: “Number: n” inside the tag BODY
 * /number_odd_or_even/<n>: display a HTML page only if n is an integer: 
	 * H1 tag: “Number: n is even|odd” inside the tag BODY
	 * You must use the option strict_slashes=False in your route definition


### [7. Improve engines](./models/engine/file_storage.py)
Before using Flask to display our HBNB data, you will need to update some part of our engine:


### [8. List of states](./web_flask/7-states_list.py)
Write a script that starts a Flask web application:
 * Your web application must be listening on 0.0.0.0, port 5000
 * You must use storage for fetching data from the storage engine (FileStorage or DBStorage) => from models import storage and storage.all(...)
 * After each request you must remove the current SQLAlchemy Session:
	 * Declare a method to handle @app.teardown_appcontext
 * Call in this method storage.close()
 * Routes:
	 * /states_list: display a HTML page: (inside the tag BODY)
	 * H1 tag: “States”
 * UL tag: with the list of all State objects present in DBStorage sorted by name (A->Z) tip
 * LI tag: description of one State: <state.id>: <B><state.name></B>
	 * 
 * Import this 7-dump to have some data
 * You must use the option strict_slashes=False in your route definition


### [9. Cities by states](./web_flask/8-cities_by_states.py)
Write a script that starts a Flask web application:
 * Your web application must be listening on 0.0.0.0, port 5000
 * You must use storage for fetching data from the storage engine (FileStorage or DBStorage) => from models import storage and storage.all(...)
 * To load all cities of a State:
	 * If your storage engine is DBStorage, you must use cities relationship
 * Otherwise, use the public getter method cities
 * After each request you must remove the current SQLAlchemy Session:
	 * Declare a method to handle @app.teardown_appcontext
 * Call in this method storage.close()
 * Routes:
	 * /cities_by_states: display a HTML page: (inside the tag BODY)
	 * H1 tag: “States”
 * UL tag: with the list of all State objects present in DBStorage sorted by name (A->Z) tip
 * LI tag: description of one State: <state.id>: <B><state.name></B> + UL tag: with the list of City objects linked to the State sorted by name (A->Z)
	 * LI tag: description of one City: <city.id>: <B><city.name></B>
	 * 
 * Import this 7-dump to have some data
 * You must use the option strict_slashes=False in your route definition


### [10. States and State](./web_flask/9-states.py)
Write a script that starts a Flask web application:
 * Your web application must be listening on 0.0.0.0, port 5000
 * You must use storage for fetching data from the storage engine (FileStorage or DBStorage) => from models import storage and storage.all(...)
 * To load all cities of a State:
	 * If your storage engine is DBStorage, you must use cities relationship
 * Otherwise, use the public getter method cities
 * After each request you must remove the current SQLAlchemy Session:
	 * Declare a method to handle @app.teardown_appcontext
 * Call in this method storage.close()
 * Routes:
	 * /states: display a HTML page: (inside the tag BODY)
	 * H1 tag: “States”
 * UL tag: with the list of all State objects present in DBStorage sorted by name (A->Z) tip
 * LI tag: description of one State: <state.id>: <B><state.name></B>
	 * /states/<id>: display a HTML page: (inside the tag BODY)
	 * If a State object is found with this id:
	 * H1 tag: “State: ”
 * H3 tag: “Cities:”
 * UL tag: with the list of City objects linked to the State sorted by name (A->Z)
	 * LI tag: description of one City: <city.id>: <B><city.name></B>
	 * Otherwise: 
	 * H1 tag: “Not found!”
	 * 
 * You must use the option strict_slashes=False in your route definition
 * Import this 7-dump to have some data


### [11. HBNB filters](./web_flask/10-hbnb_filters.py)
Write a script that starts a Flask web application:
 * Your web application must be listening on 0.0.0.0, port 5000
 * You must use storage for fetching data from the storage engine (FileStorage or DBStorage) => from models import storage and storage.all(...)
 * To load all cities of a State:
	 * If your storage engine is DBStorage, you must use cities relationship
 * Otherwise, use the public getter method cities
 * After each request you must remove the current SQLAlchemy Session:
	 * Declare a method to handle @app.teardown_appcontext
 * Call in this method storage.close()
 * Routes:
	 * /hbnb_filters: display a HTML page like 6-index.html, which was done during the project 0x01. AirBnB clone - Web static
 * Copy files 3-footer.css, 3-header.css, 4-common.css and 6-filters.css from web_static/styles/ to the folder web_flask/static/styles
 * Copy files icon.png and logo.png from web_static/images/ to the folder web_flask/static/images
 * Update .popover class in 6-filters.css to allow scrolling in the popover and a max height of 300 pixels.
 * Use 6-index.html content as source code for the template 10-hbnb_filters.html:
	 * Replace the content of the H4 tag under each filter title (H3 States and H3 Amenities) by &nbsp;
 * State, City and Amenity objects must be loaded from DBStorage and sorted by name (A->Z)
	 * You must use the option strict_slashes=False in your route definition
 * Import this 10-dump to have some data


### [12. HBNB is alive!](./web_flask/100-hbnb.py)
Write a script that starts a Flask web application:
 * Your web application must be listening on 0.0.0.0, port 5000
 * You must use storage for fetching data from the storage engine (FileStorage or DBStorage) => from models import storage and storage.all(...)
 * To load all cities of a State:
	 * If your storage engine is DBStorage, you must use cities relationship
 * Otherwise, use the public getter method cities
 * After each request you must remove the current SQLAlchemy Session:
	 * Declare a method to handle @app.teardown_appcontext
 * Call in this method storage.close()
 * Routes:
	 * /hbnb: display a HTML page like 8-index.html, done during the 0x01. AirBnB clone - Web static project
	 * Copy files 3-footer.css, 3-header.css, 4-common.css, 6-filters.css and 8-places.css from web_static/styles/ to the folder web_flask/static/styles
 * Copy all files from web_static/images/ to the folder web_flask/static/images
 * Update .popover class in 6-filters.css to enable scrolling in the popover and set max height to 300 pixels.
 * Update 8-places.css to always have the price by night on the top right of each place element, and the name correctly aligned and visible (i.e. screenshots below)
 * Use 8-index.html content as source code for the template 100-hbnb.html:
	 * Replace the content of the H4 tag under each filter title (H3 States and H3 Amenities) by &nbsp;
 * Make sure all HTML tags from objects are correctly used (example: <BR /> must generate a new line)
 * State, City, Amenity and Place objects must be loaded from DBStorage and sorted by name (A->Z)
	 * You must use the option strict_slashes=False in your route definition
 * Import this 100-dump to have some data

---

## Author
* **Cristian David Pineda Vargas** - [Cristiand187](https://github.com/Cristiand187)