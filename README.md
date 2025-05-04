Auctions-Django
Design an eBay-like e-commerce auction site that will allow users to post auction listings, place bids on listings, comment on those listings, and add listings to a “watchlist.”

Django Admin Credentials:
UserID : "rajveer" Password : "raj@1234"

Homepage
image

Clicking on a listing take users to a page specific to that listing. On that page, users will be able to view all details about the listing, including the current price for the listing. If the user is signed in and is the one who created the listing, the user have the ability to “close” the auction from this page, which makes the highest bidder the winner of the auction and makes the listing no longer active. Users who are signed in will be able to add comments to the listing page. The listing page displays all comments that have been made on the listing.

The user will be able to add the item to their “Watchlist.” If the item is already on the watchlist, the user will be able to remove it.

watchlist page
image

Users will be able to visit a page to create a new listing. They will be able to specify a title for the listing, a text-based description, and what the starting bid should be.

Category Page
image

Users will be able to visit a page that displays a list of all listing categories.

List of category Page
image

Django Admin Interface:
Django admin interface, a site administrator will be able to view, add, edit, and delete any listings, comments, and bids made on the site.
