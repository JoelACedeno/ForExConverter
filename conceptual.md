### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
  - Important differences between the two languages are that JS is used primarily for client-side development whereas Python is used primarily for server-side development and data handling; and that JS uses {} in function declaration where Python uses solely indentation, which makes script written in Python reliant on proper indentation.
- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
  - The get() method can be used for this, where if a dictionary key is not found it defaults the value to 0.

- What is a unit test?
  -  A unit test tests a specific function of the whole program.

- What is an integration test?
  - An integration test tests mulitple functions of a program at once and comfirms that they properly work when used together.

- What is the role of web application framework, like Flask?
  - Web app frameworks like Flask handle HTTP requests, produce html markup, handle forms and cookies, connect to databases and much more. 

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  - Depending on how the data needs to be handled will determine which method to use. If the data is security sensitive or if the data is essential to the resource being accessed a route URL should be used. If security is of no concern and multiple resources are being accessed at once a query param can be used.

- How do you collect data from a URL placeholder parameter using Flask?
  - The route() method is used with the placeholder inside < > brackets at the end of a defined route.

- How do you collect data from the query string using Flask?
  - Query string data can be collected by accessing key value pairs in "request.args"

- How do you collect data from the body of the request using Flask?
  - Data can be collected from the body by using the "request" object.

- What is a cookie and what kinds of things are they commonly used for?
  - Cookies are key-value pairs used to store small bits of information used in the browser.

- What is the session object in Flask?
  - The session object in Flask is a dictionary-like object that stores information for the current browser or client. Session data cannot be modified by users.

- What does Flask's `jsonify()` do?
  - This method transforms server-side Python objects into JSON data for client-side use throught HTTP responses.