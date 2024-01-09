## Climbing Route Recommender


soon to come:

~~- web scraper to download all mountainproject data for the continental us~~
- website for users to create profiles, browse routes, and have routes recommended to them based on preferences for type of climbing / difficulty / location / proximity to other climbs / etc

<hr>

#### begin my stream-of-consciousness planning for this project
<br>
when recommending routes this should take into account

- type of climbing 
- difficulty
- ratings left by other users
- route length and number of pitches
- how far away it is => this could be how how long it would take to drive w/ google maps api, or if that costs money then just how many miles calculated by coordinates
- proximity to other routes => this would probably be better to just do distance in miles since you hike between some crags

all this can be accomplished with just what i have in the csv files, is there anything else?

- if there is a good description of the climb / approach
- are there pictures of the route

can use the links in the csv files to scrape for these things ^

so for now i think just gather all the csv files and then start work on website

once i get the website set up enough for users to login and mess with their profiles, shunt all the csv data into a database and play with displaying it/searching thru it