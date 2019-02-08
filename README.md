# corp-map
A hierarchical and radial view of corporation structures.

## To Do
* Make spacing better
* Fix click issue
* Finish AT&T structure
* Format index.html
* Move Javascript to different file
* Bring up more info on click (full logo, name, net worth, website, !!FUN!! facts)
* Add more root companies
* Make a logo for the site
* Make area change size with screen size
* Make logos fit inside fixed size boxes
* Add radial map
* Update bsteen.io links
* Clean up vis-js folder
* Begin investigating web crawling

## companies.json format
* Each root company has its own JSON file
* Within the JSON file is an array of structs
* The first struct must always be the root company
* Order of children companies does not matter after first entry