- django  ridiculos fast 

- django ma scale boht hi  axha mil\ta ha minimum level pa. agr ap na $5 $10 pa deploy kara tb biyakafi user  ko handel krna ki power rakhti ha.. 


# 1. Understanding Django Basics
Django is a high-level Python web framework that helps developers build web applications quickly and efficiently. It follows the Model-View-Template (MVT) architectural pattern, which is similar to the MVC (Model-View-Controller) pattern. Here’s a breakdown:

- **Model:** Manages the data and defines your application's structure. Models are where you define your data tables (like User, Post, etc.).
- **View:** Handles the logic behind requests, processing data, and preparing what will be displayed.
- **Template:** Controls what the user sees and provides HTML pages for the frontend. Templates allow for dynamic data display.
# 2. Django Request Handling Flow
Django’s request-response cycle is what happens when a user tries to access a page in your Django app:

- **Step 1:** User Makes a Request
A user types in a URL or clicks a link, which sends a request to Django.

- **Step 2:** URL Routing
Django checks the urls.py file to match the request to a view function. Each URL pattern points to a specific view function that will handle the request.

- **Step 3:** View Processes the Request
The view function takes the request, processes any data (e.g., querying the database through models), and prepares data for the template.

- **Step 4:** Template Rendering
If a template is involved, the view sends data to it, which then renders HTML to be sent back to the user’s browser.


django create  the app not install it so  our main project does not know that  we have a new app so firstly we tell them that we have a app. in settig.py add the app name