# corp-map
A hierarchical and radial view of corporation structures.

## To Do
* Move Javascript to different file
* Separate files for each company page
* Make area change size with screen size
* Fix border spacing
* Have text inside border
* Get node physics working
* Add radial map
* Update bsteen.io links
* Clean up vis-js folder
* Begin investigating web crawling

## companies.json format
* Each root company has its own JSON file
* Within the JSON file is an array of structs
* The first struct must always be the root company
* Order of children companies does not matter after first entry
* Size is set for a custom logo size; set to -1 to use the default image size
