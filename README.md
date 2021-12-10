# mysiteF21_Project
COMP-8347: Internet Applications and Distributed Systems

F2021 Final Project Tasks

FEATURES
1. In admin.py create a class ProductAdmin(admin.ModelAdmin), register this with the admin site and show the name, category, price, and available fields, for each Product, in the admin interface page that lists all Products.
2. In admin.py write an action for ProductAdmin class that will add 50 to the current value of the stock field for the selected products and save the updated value in the database.
3. Add ‘register’ view that allows a user to register as a Client. Update myapp/urls.py and create a template register.html
4. Update the user_login view created in Lab 10 so that if a user who is not logged in goes to url ‘/myapp/myorders/’ they will be directed to the login page and after successful login they will go directly to the ‘/myapp/myorders/’ page (instead of the main index page).
5. Update base.html so that if a user is logged in, it will display Logout (myapp/logout) and My Orders (myapp/myorders) links. Otherwise, it will display Register Here (myapp/register) and Login (myapp/login) links. Each link should go to the corresponding view function defined earlier (in Lab 10 or in step 3 or 4 above).
6. Update base.html so that if a user is logged in, it will display “Hello <first_name>” instead of “Hello User”. Here <first_name> is the first name of the user that is currently logged in.
7. Add validators for stock field in Product model so that it is between 0 and 1000.
8. Upload image file. Add an optional field image field for a Client to upload his/her photo.
9. In admin.py create a class ClientAdmin(admin.ModelAdmin), register this with the admin site and show the first_name, last_name, city fields and list of categories the client is interested in, for each client, in the admin interface page that lists all clients.
10. Add a ‘Forgot password’ link on login page. It should email a new password to the user.
