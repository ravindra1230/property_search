# Search Engine Program
***
**Objective :** This is a program that returns all the match above 40% of a query based on parameters.

**Language and version used : Python 3.6.8**


## Usage:

The data can be stored in the `sample_data.py` file where all the property's are stored along with all the queries that need to be performed.

To run the program enter the following into the terminal after changing the data as required and navigating to the directory:

```sh
$ python solution.py
```

**Output examples:** 

```sh
	$ python solution.py     
		1 [[3, 90], [4, 65]]
		2 [[3, 75]]
```
where the output is in the form :
`query['id'] [[match1['id'],match1 percentage], [match2['id'],match2 percentage]] , etc`