Auctions-Django
Design an eBay-like e-commerce auction site that will allow users to post auction listings, place bids on listings, comment on those listings, and add listings to a “watchlist.”

Django Admin Credentials:
UserID : "rajveer" Password : "raj@1234"

Homepage
![image](https://github.com/user-attachments/assets/fce77472-157c-4734-b03d-3b06390bf96f)


Clicking on a listing take users to a page specific to that listing. On that page, users will be able to view all details about the listing, including the current price for the listing. If the user is signed in and is the one who created the listing, the user have the ability to “close” the auction from this page, which makes the highest bidder the winner of the auction and makes the listing no longer active. Users who are signed in will be able to add comments to the listing page. The listing page displays all comments that have been made on the listing.

The user will be able to add the item to their “Watchlist.” If the item is already on the watchlist, the user will be able to remove it.

watchlist page
![image](https://github.com/user-attachments/assets/63bd8ef3-779f-486d-9936-09381549d5a3)


Users will be able to visit a page to create a new listing. They will be able to specify a title for the listing, a text-based description, and what the starting bid should be.

Category Page
![image](https://github.com/user-attachments/assets/1409b33a-1789-48e6-9e92-344e1c04ec8d)


Users will be able to visit a page that displays a list of all listing categories.

List of category Page
![image](https://github.com/user-attachments/assets/227d8e9b-cdea-4317-aefa-daf16c116b2c)


Django Admin Interface:
Django admin interface, a site administrator will be able to view, add, edit, and delete any listings, comments, and bids made on the site.
