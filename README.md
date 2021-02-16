# She Rocks!


![She Rocks](static/readme-doc/layout/home.png)

For the fourth Milestone Project, I decided to combine two of my passions, fashion and rock music, 
in an e-commerce website. Having a background in high-end retail, I decided to keep the same customer target, 
but specializing in rock chic style clothing.

View the live project here. [She Rocks](https://sherocks.herokuapp.com/)


### :page_with_curl: Navigation Menu

The navigation menu sticks to the top of every page. 

In this way, a user can navigate easily even if he/she scrolls down the page.

This is how it looks on larger devices:

![Navbar](static/readme-doc/layout/navbar.png)

On smaller screens the navbar collapses into a hamburger icon:

![Navbar](static/readme-doc/layout/navbarMobile.png)

![Navbar](static/readme-doc/layout/navbarMobileClick.png)

### :page_with_curl: Footer

The footer has a black background,
so that it marks a clear distinction with the rest of the body and visually close the space.

The area is divided into three sections, that on larger screens are one next to the other,
but on smaller screens are displayed vertically.

The first column is a brief summary of the menu with a list of the products pages.
There is also a mention about safe payments with Stripe, because I think that in a e-commerce
website is important to give clear information about payments.

The second column is the "Connect" section: we have the Social Media links, but also a link
to the Team page. Again, it is important to show the customer who is behind a virtual website.

The third column is about the Company info: name, address, CRN, phone and email.

![Footer](static/readme-doc/layout/footer.png)


### :page_with_curl: Home Page

The home page is divided into four sections.

The first one welcomes the user with a background image of a model dressed in a rock style,
 who personifies the target customer and serves to create an immediate visual and mental connection 
 between the user and the company.
An overlay with text ("Be a rock goddess") gives an input to buy, leveraging the target customers unconscious.
This first div has a parallax effect (obtained with JavaScript).

I wanted it to be incisive, direct and appealing. One of the first things I learned working in stores with highly 
demanding customers is that the first 5 seconds in which the customer enters the store already determines his willingness to buy.

Scrolling down the page, there is a second section with a quote by Coco Chanel "I don't do fashion. I am fashion", which
serves to empower again the feeling of strenght and uniqueness in the potential customer, flanked by a picture of the last item 
added in the store. This whole block is visible only on larger screens; on smaller devices the user can see only the picture and 
not the quote. I decided to leave only one of the two because I didn't want the home page to be too long: it should arouse interest,
not annoy.

![Second Section in Home Page](static/readme-doc/layout/second.png)

The third section is similar to the first one: there is again a background image with a model dressed in rock style, but the
text in the overlay now invites the user to register. 
There is again a parallax effect, but this time obtained with pure CSS.
I had to add some JavaScript to fix a bug on iOS, since the fixed background is not supported. Users from a iOS device can't see
the parallax effect on this third section, but it does not affect the User Experience.

![Third Section in Home Page](static/readme-doc/layout/third.png)

The last section is a carousel with random images taken from the products database. The images change everytime the user refreshes
the page, so the content is always dynamic.

![Fourth Section in Home Page](static/readme-doc/layout/fourth.png)


### :page_with_curl: Collection

The collection page is simple. It returns all the products in the database, and for each product there is a card with image, name, brand and price.

It is possible to sort the products by price, brand name and product name.

![All Products](static/readme-doc/layout/products.png)

### :page_with_curl: Search Functionality

From the navbar it is possible to search for a specific word in the database.

The results are displayed with the same layout of the collection page, but there is a extra banner with the text that the user
enterd in the search box.

![Search Functionality](static/readme-doc/layout/search.png)

### :page_with_curl: Sort Functionality

The sort functionality is available in all the products pages (collection, category, detail and search).

![Sort Functionality](static/readme-doc/layout/sort.png)

### :page_with_curl: Products by Category

The Category pages have the same layout of the collection page.

The only difference is that the title renders the name of the specific category.


### :page_with_curl: Product Detail

The product detail page has a title that takes the name of the category of the item and the brand (e.g. "Top by Alexander McQueen).

Then there is the image of the product, its name, brand, price, size (if it has sizes), quantity (the user can add more than one item),
and a submit button that send the product in the shopping bag, or a button that takes back to the collection page.

An accordion has three categories: description, material and reviews. The reviews section is visible only if the item has reviews,
otherwise there is only description and material.

At the bottom there is a carousel with random images (the same structure as there is on the home page). I thought it could increase
sales to add some random items just below the "add to bag" area.

![Detail Product](static/readme-doc/layout/detail.png)

### :page_with_curl: Team

The team page shows all the team members, and for each employee there is the picture, the name, the name of the department,
the role and the contacts (phone number and e-mail).

In this way it is easy for a user to contact the right person, and it also adds thrustworthy because the user can see exactly
who is behind the website.

### :page_with_curl: Login / Register

The login page (but also all the other pages related to allauth functionality) has a background image and a overlay with a 
glassmorphism effect. I choose it because I wanted the website to look modern.

![Detail Product](static/readme-doc/layout/signup.png)


### :page_with_curl: My Profile (only for registered users)

The Profile page is simple. It shows the user delivery information (with the chance to update them), and a section with
the activity of the user on the website.
This section shows the order history and the reviews added by the user.
If the user has no reviews yet, he/she can click on a link that takes to the Review page.

### :page_with_curl: Reviews (only for registered users)

This page has a simple layout and allows the user to add a review to one or more items in the store.

### :page_with_curl: Product Management (only for superusers)

This functionality is limited only to admin. It allows to add a product in the database.

A superuser can also edit or delete products from the collection page, the category pages, the product detail page.

---

## User Experience (UX)


* **:bookmark_tabs: Strategy Plane**

The website is an e-commerce that sells high-end clothing to women that like a rock-chic style.

The company that owns the website wants to show its modern, feminine and strong concept through a visual design and a clear functionality.

The goal is to attract potential customers and increase sales.

A target customer is a woman aged 25-45 that is interested in fashion, has a good economy and likes to spend her money 
on items that makes her feel beautiful. At the same time, she likes an active lifestyle and doesn't like to fit inside classical schemes. 
She has a passion for rock music and she feels independent; she is not afraid to dress sometimes a little bit over the top.

For this reason, the website needs to have a clear structure and a modern design.

Information about the company must be clear, giving also a strong brand identity, and the shopping process needs to be fast and simple.


* **:bookmark_tabs: Scope Plane**

Considering the goal of the website and the target customer, I realized that most of the visits come from mobile phones.

Customers usually shop from their mobile phones while doing something else (e.g. travelling on the subway or just chilling on the sofa),
so the website needs to be mobile first designed.


* **:bookmark_tabs: Structure Plane**

The customer should have the chance to register in order to save personal details and posthumously review the order history or add reviews.

At the same time, there should be the chance to complete an order without registering, for those customers who want only a one-time purchase
 or simply don't want to have a personal profile on the website.

Customers need to search the database by entering specific words in a search box, or by just navigating the website: the menu must
be clear and redirect to the main product categories. It is important also to add a sort button that allows the user to view
the products in a specific order: often users want to list the products by price.

The user needs to constantly monitor the status of the shopping bag without entering the shopping bag page. In this way
he/she knows exactly if is spending too much or if can go on shopping something else.

Admins can access the dashboard by logging in to the /admin path, or simply by logging in from the website as a common user does.
From the dashboard they can perform all the tasks related to orders, customers, products, employees, company details; from the
website pages they can just add new products, edit or delete the ones already on the database.


* **:bookmark_tabs: Skeleton Plane**

The structure of the website is:

* Home Page

* Products by Category

* All Products (Collection)

* Team 

* Register

* Sign In

* My Profile (personal details, order history and reviews)

* Shopping bag

* Checkout page

* Add review

* Product Management (admin)


* **:bookmark_tabs: Surface Plane**

For this project I have looked at different high end fashion websites (e.g. Dior, Chanel, Balmain) to check how those brands communicate
their identity and how they implemented the e-commerce section through design.

A common feature is the simple layout, with a lot of negative space that adds focus on the products, and the predominant use of
black and white colors.

I decided to keep a similar styling throughout the website, but adding some extra "spice" with a splash of color just to make
 the visual impact a little stronger and different (basically how the brand "She Rocks" is).

Call to action buttons are pink, while secondary buttons have a dark background. The size of the buttons is large enough for reliable
 interaction from mobile devices.

A parallax effect in the home page adds a modern touch and a dynamic interaction.

For the register/sign in/sign out page I decided to design a card with glassmorphism effect. According to all UX websites,
this is a trend for the year 2021 (even if it's nothing new because the effect is already known), so I wanted to use it in my project.
To give some tridimensional effect I added some depth using the principles of neumorphism (another trend in UX design).
This is more visible on the overlay in the carousel, that takes the same effect as in the sign in page.

![Glassmorphism effect](static/readme-doc/layout/glass.png)

### User stories

#### :computer: Customer stories

|   | Opportunity / Problem / Feature | Importance | Viability |
|---|---------------------------------|------------|-----------|
| 1 | As a customer, I want to navigate the website, so that I understand if I am intersted in buying something. | 5 | 5 |
| 2 | As a customer, I want to check the categories, so that I understand if I am intersted in buying something. | 5 | 4 |
| 3 | As a customer, I want to click on a specific category, so that I understand if I am intersted in buying something. | 5 | 4 |
| 4 | As a customer, I want to see new products, so that I understand if I am intersted in buying something. | 4 | 4 |
| 5 | As a customer, I want to search for a specific term, so that I can find something specific that I want. | 4 | 5 |
| 6 | As a customer, I want to sort products, so that I can see the product list in a specific order. | 4 | 4 |
| 7 | As a customer, I want to click on a specific product, so that I can view its details. | 5 | 4 |
| 8 | As a customer, I want to add a product on my bag, so that I can buy it. | 5 | 4 |
| 9 | As a customer, I want to view my shopping bag, so that I can know how much I am going to spend. | 5 | 4 |
| 10 | As a customer, I want to know how I am going to pay, so that I can feel safe to use my credit card. | 5 | 5 |
| 11| As a customer, I want to know who is behind the website, so that I can feel safe to pay. | 4 | 5 |
| 12 | As a customer, I want to know more about shipment, so that I can feel safe to place an order. | 4 | 3 |
| 13 | As a customer, I want to save my profile, so that I don't have to add all over again with a second purchase | 3 | 5 |
| 14 | As a customer, I want to edit my profile, so that I can update my details | 4 | 5 |
| 15 | As a customer, I want to delete my profile, so that I can delete my details from the database | 3 | 5 |
| 16 | As a customer, I want to add more products to my shopping bag, so that I can buy more than one piece per item | 5 | 4 |
| 17 | As a customer, I want to remove products from my shopping bag, so that I can edit my order | 5 | 4 |
| 18 | As a customer, I want to read reviews for a product, so that I can improve my shopping experience | 4 | 4 |
| 19 | As a customer, I want to write reviews for a product, so that I can share with other users my shopping experience | 4 | 4 |

#### :computer: Admin stories

|   | Opportunity / Problem / Feature | Importance | Viability |
|---|---------------------------------|------------|-----------|
| 1 | As an admin, I want to log in, so that I can access my dashboard | 5 | 5 |
| 2 | As an admin, I want to access my dashboard, so that I can view the tasks I can perform from there | 5 | 5 |
| 3 | As an admin, I want to access my dashboard, so that I can view all the products | 5 | 5 |
| 4 | As an admin, I want to access my dashboard, so that I can add products | 5 | 5 |
| 5 | As an admin, I want to access my dashboard, so that I can edit products | 5 | 5 |
| 6 | As an admin, I want to access my dashboard, so that I can delete products | 5 | 5 |
| 7 | As an admin, I want to access my dashboard, so that I can view all the orders | 5 | 5 |
| 8 | As an admin, I want to access my dashboard, so that I can edit orders | 5 | 5 |
| 9 | As an admin, I want to access my dashboard, so that I can delete orders | 5 | 5 |
| 10 | As an admin, I want to access my dashboard, so that I can view customers details | 5 | 5 |
| 11 | As an admin, I want to access my dashboard, so that I can edit customers details | 5 | 5 |
| 12 | As an admin, I want to access my dashboard, so that I can delete a customer profile | 5 | 5 |
| 13 | As an admin, I want to log in inside the website, so that I can perform tasks from there | 5 | 5 |
| 14 | As an admin, I want to log in inside the website, so that I can edit products from there | 5 | 5 |
| 15 | As an admin, I want to log in inside the website, so that I can delete products from there | 5 | 5 |


As shown from above, the admin stories are extremely important and need to be fully implemented.

The user stories as well are important, but a few will need more time. For instance, it won't be possible in the first release to add
a section about shipments because it means to contact a courier and check with them the terms.

### Design

### Colour Scheme

At the beginning I wanted to stuck with a black/white palette, but then I thought that a splash of colour was suitable, 
as the style of clothing has character and stands out. 

I opted for a deep pink (China Pink) and a dark purple (Russian Violet). I got the inspiration from cyberpunk digital art.

![Palette](static/readme-doc/palette.png)


### Typography

I choosed two fonts that are modern and highly legible: Montserrat and Raleway.

![Montserrat](static/readme-doc/montserrat.png)
![Raleway](static/readme-doc/raleway.png)


At the beginning I searched for something more out of the ordinary for the titles, but I ended up choosing Raleway.

I didn't want to make the page look too messy and the focus should stay on the pictures.


### Imagery

I got the products images from the brands web pages.

I selected the products that I thought would be perfect in this shop.

The team images has been taken from Unpslash, except for one image that is mine.

The pictures in the home page come from two different websites.

All the links to the images are here: [Images Links](static/readme-doc/Links.pdf)


### Wireframes

You can view my prototypes by clicking on the following links:

* [Mobile Prototype](static/readme-doc/wireframes/mobileEcommerce.pdf)

* [Tablet Prototype](static/readme-doc/wireframes/TabletEcommerce.pdf)

* [Desktop Prototype](static/readme-doc/wireframes/DesktopEcommerce.pdf)

Prototyping has been made with Balsamiq.



### Features

* Responsiveness throughout all devices.

* Navigation Bar always placed at the top of the screen oon all devices. Easy for the user to navigate.

* Brand Logo inside the navbar, always visible, that is also a link to the home page.

* Toasts that display important messages to the user (e.g. Order successfully completed, item added to bag, successfully signed in, etc).

* Shopping bag icon always visible at the top, with the count number of the products inside. Clicking on it, the user is redirected to
 the shopping bag page.

* Profile icon, always visible at the top. Clicking on it, a dropdown appears with sub-links to other pages: "register" and "sign in" for all users,
 "my profile" for registered users and "product management" for superusers.

* Footer always at the bottom of the page, with a summary of the most important links inside the web page, links to social media accounts,
 company information with relative details.

* Links clearly identifiable by a hand pointer cursor and a color change on hover.

* Add to bag buttons from the product detail page that allows to add the item to the shopping bag.

* Size selection for those items that have sizes.

* Quantity (add and subtract) functionality both on product detail page and shopping bag page.

* Secure checkout button that redirects to Stripe for safe payments.



### Features to implement

In the future I will add:

* A section about shipping: how long does it take to have a order shipped and then delivered,
which courier takes care of the parcels, shipping fees, etc.

* Functionality in the detail page that allows the user to go back to the exact point he/she was before clicking
on the specific product. Now it takes back to the collection page, but it can be frustrating if a user was
navigating in a specific category and had already scrolled down the page.

* Reviews only for item already purchased. Right now a registered user can add a review for any of the products in store.
 I will limit the functionality to only the products that the user actually purchased. This will avoid fake reviews.

* Chance for a registered user to delete his/her profile directly from the "Profile" area.

* In the confirmation email after placing an order I will include also all the details of the items purchased (name, brand,
price, quantity).

* Chance to log in using social accounts (Facebook, Instagram) and Google.

* Add a section about personal data processing (GDPR) -- very important to do if the website needs to be real!

* Change styling on toasts messages to make them more similar to overlays on carousel, adding consistency.

* Improve styling on 280px screens (see bug sections)

### Database

For this project I have used SQLite on the local server and Postgres for deployment.

<details>
<summary>Models</summary>

### User Profile
```
class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_country = CountryField(blank_label='Country', null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
```

### Category
```
class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=30)
    friendly_name = models.CharField(max_length=50, null=True, blank=True)
```

### Product
```
class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=160)
    brand = models.CharField(max_length=100)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    material = models.CharField(max_length=160)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=2000)
    image = models.ImageField(upload_to='products', null=True, blank=True)
```

### Review
```
class Review(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="reviewer")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviewed_item")
    review = models.CharField(max_length=160)
    created = models.DateField(auto_now=True)
```

### Order
```
class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="orders")
    full_name = models.CharField(
        default="", max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label="Country *", null=False, blank=False)
    postcode = models.CharField(
        default="", max_length=20, null=False, blank=False)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default='')
```

### Oder Line
```
class OrderLineItem(models.Model):
    order = models.ForeignKey(
        Order, null=False, blank=False, on_delete=models.CASCADE,
        related_name='lineitems')
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE)
    product_size = models.CharField(
        max_length=2, null=True, blank=True)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False,
        blank=False, editable=False)
```

### Company
```
class Company(models.Model):
    class Meta:
        verbose_name_plural = "Companies"

    name = models.CharField(max_length=60, null=False, blank=False)
    address = models.CharField(max_length=60, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
```

### Office
```
class Office(models.Model):
    name = models.CharField(max_length=60, null=False, blank=False)
    company = models.ForeignKey(
        'Company', on_delete=models.CASCADE, related_name="office")
```

### Employee
```
class Employee(models.Model):
    full_name = models.CharField(max_length=60, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    office = models.ForeignKey(
        'Office', on_delete=models.CASCADE, related_name="employee_in_office")
    role = models.CharField(max_length=30, null=False, blank=False)
    image = models.ImageField(upload_to='team', null=True, blank=True)
```
</details>

---

## Technologies Used

### Languages Used
* HTML5
* CSS3
* JavaScript
* Python 3.8.6

### Frameworks, Libraries & Programs Used

* Bootstrap 4.5.0.
* Google Fonts
* Font Awesome 4.7.0.
* Git
* GitHub
* GitPod
* Jinja
* pip3
* Django
* Django Crispy Fields
* Django allauth
* Django countries
* Django storages
* Gunicorn
* Pillow
* Psycopg
* Boto3
* Heroku
* SQLite
* Postgres
* [Django Secret Key Generator](https://miniwebtool.com/it/django-secret-key-generator/)
* Stripe
* AWS S3
* Chrome DevTools
* Balsamiq
* Favicon.ico
* Html Validator
* CSS Validator
* JSHint
* Autoprefixer CSS 9.7.6


---

## Testing

### :heavy_check_mark: Functionality Testing 


### :heavy_check_mark: Usability Testing


### :heavy_check_mark: Compatibility Testing

The website has been tested on laptop and mobile phone.

Browsers:

* Chrome: no issues.

* Edge: no issues.

* Firefox: a few issues. Check the "bug" section.

* Safari (on iPhone): issue with background attachment set to fixed. Check "bug" section for more details.

* Opera: 


### :heavy_check_mark: Performance Testing



### Bugs

#### Solved Bugs:

I had a problem with the home page on iOS, since the third section has a background attachment property set to fixed.
That gives a parallax effect, but is not supported on iOS.
The design was compromised, so I wrote some JavaScript to detect if the device is iOS, and if that returns true, 
the fixed property is removed from the section.

The parallax effect on this section is lost, but at least the background image is visible even if it scrolls with the page.

I could have also used the same parallax effect that has the first section in the home page, which is working properly also on iOS,
but the visual effect is slightly different and I didn't want to replicate the exact same result.

#### On 280px screens:
 
 The home page floats horizontally because the navbar is wider than the viewport.
 The pages are not centered.

---

---

## Deployment

The website is deployed connecting Heroku with GitHub.


#### Fork the code on GitHub
If you need to work on this code on your own, follow these steps:

* Log in to GitHub;
* Find the repository you are looking for;
* On the top-right of the page you will find a button with the name "Fork";
* Click on it and it will automatically fork the code to your GitHub.


#### Local Clone
To make a local clone of the site, just follow these stepsg:

* Log in to your GitHub;
* Under your repository section, select the repo that you need;
* You will find a green button with the name "Code". Click on it;
* On the dropdown selection, you will find a link to clone the code with HHTPS;
* Now open Git bash;
* Open the directory where you want to work on the cloned code;
* Type git clone followed by the link you have previously copied.


---

## Credits

### :star: Code

### :star: Media


### :star: Acknowledgements


