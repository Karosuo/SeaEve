#SeaEve, Search an Event

**Main target was to get a system in wich:**<br />
*Any user can create an event and mark up in the map.<br />
*Every user has some event preferences and the system filter the results depending in that to show them what they want in the map.<br />
*The system detects the user's city (where currently is he/she approximetly) and finds the events available near him/her.<br />
*There's a calendar with the near events and color coded to identify them quickly.<br />
*Promotes and supports the local talent putting them on the map for free.<br />
*Gives a presentation card of the city and an easy and quick tour guide through this events.<br />

##This module:
*Captures the data for the adds thta will be displayed randomly in each reload of the page.<br />
**Includes images and specified data from the owner of the add.<br />
*Shows randomly the adds from the database to an html div in a test page.<br />

###Tech part:
Uses Google App Engine with Python and Webapp2 framework.<br />
Jinja to filter the results in just a portion of the html without using AJAX.<br />
