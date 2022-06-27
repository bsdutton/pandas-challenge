# pandas-challenge

* Used PyCitySchools_starter to see requirements for this homework and to see what the results should look like.
* Did all my work in main-working.ipynb so there are a lot of extra code-blocks for all differnt methods I tried.
* Cleaned up solutions for submittal in main.ipynb before it was converted to main.py to run.

#### This homework was LONG!!!

#### Things I learned.
* It was easier to keep track of dataframe names and column names by adding numbers to new ones when I tried something else.
* I learned the hard way to copy dataframes before I did anything that would change datatypes.  Many times I'd get to a step only to find I could not go further because I had changed the datatype from float64 to object.  I had to backtrack to see where I made the change, and I learned to make copies of dataframes before did a computation to change datatype.
* I also learned the persistence of groupby keys(index).  I had to rebuild dataframes and track down where the key was first used so I could make a new dataframe I could use different groupby on.
* The section in https://pandas.pydata.org/docs/user_guide/groupby.html on "Group by: split-apply-combine" was most helpful, in particular the section "DataFrame column selection in GroupBy" in helping me understand the persistence of the groupby keys.
* 