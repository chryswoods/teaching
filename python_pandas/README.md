# Python Pandas

You need to download these data files

* [people.csv](https://raw.githubusercontent.com/chryswoods/teaching/master/python_files/people.csv)
* [biographies.tsv](https://raw.githubusercontent.com/chryswoods/teaching/master/python_files/biographies.tsv)
* [invested.xlsx](https://raw.githubusercontent.com/chryswoods/teaching/master/python_pandas/invested.xlsx)

## Importing pandas

[pandas](https://pandas.pydata.org) is a python library for data analysis and 
manipulation.

Import pandas using

```python
import pandas as pd
```

This loads the pandas library, and makes it accessible via `pd`

## Reading csv files

Read a csv file using

```python
df = pd.read_csv("people.csv")
```

You can look at the top of the data using

```python
df.head()
```

Similarly you can see the end of the data using

```python
df.tail()
```

You can view specific columns using their name (almost like a dictionary)

```python
df["ID"]
```

You can access a subset of rows by slicing, e.g.

```python
df.loc[0:3]
```

would extract the first three rows. To extract individual rows use;

```python
df.loc[0]
```

(would get the first row)

You can extract specific columns in specific rows using

```python
df.loc[0, "ID"]
```

(get the first value in the "ID" column)

```python
df.loc[0, ["ID", "Name"]]
```

(get the first value in the "ID" and "Name" columns)

Alternatively, you can combined `loc` and column lookup, e.g.

```python
df.loc[0]["ID"]
```

or

```python
df["ID"].loc[0]
```

## Selecting by searching

Select rows that match conditions, e.g.

```python
df[ df["ID"] == "P5a180b0" ]
```

or 

```python
df[ df["Name"].str.contains("Brunel") ]
```

You can perform a case-insensitive search using

```python
df[ df["Name"].str.contains("brunel", case=False) ]
```

Sometimes you will get multiple results back from a search, e.g.

```python
df[ df["Name"].str.contains("claxton", case=False) ]
```

The number on the left is the index of the row in the original data, e.g.
in the original data "Christopher Claxton" is at row 10. You can get this
row using

```python
df[ df["Name"].str.contains("claxton", case=False) ].loc[10]
```

If you want to search by the index in the returned result, use `iloc`, e.g.

```python
df[ df["Name"].str.contains("claxton", case=False) ].iloc[0]
```

You can also use [regular expressions](../python_regexp/README.md) to 
find anyone called `chris` followed by anything, followed by `clax`,
(so using `chris.*clax`),

```python
df[ df["Name"].str.contains(r"chris.*clax", case=False) ]
```

or you can use `startswith` or `endswith`

```python
df[ df["Name"].str.endswith("nel") ]
```

## Fixing data

The data is not clean, as the names contain extra spaces, e.g.

```python
df[ df["Name"].str.startswith("Isam") ]
```

returns nothing, as the name is actually ` Isambard...`, e.g.

```python
df[ df["Name"].str.startswith(" Isam") ]
```

We need to strip out all of the unnecessary whitespace. We can do this
by setting `skipinitialwhitespace` to `True` when reading the CSV file

```python
df = pd.read_csv("people.csv", skipinitialspace=True)
```

Now we can correctly find Isambard...

```python
df[ df["Name"].str.startswith("Isam") ]
```

## Joining Data

Read the biography data using

```python
bios = pd.read_csv("biographies.tsv", sep="\t", skipinitialspace=True)
```

Note that we pass `\t` to tell pandas to use tabs as separators

We now want to join the biography data into the people data. Since the 
ID is used to match people to biographies, we can use

```python
df = pd.merge(df, bios, on="ID")
```

Check the data using

```python
df.head()
```

Now let's find all people who were involved in the propeller trials...

```python
df[ df["Biography"].str.contains("propeller", case=False) ]
```

We can print all of the data out more fully by looping over all of the 
rows and printing the data...

```python
for row in df[ df["Biography"].str.contains("propeller", case=False) ].values:
    print(row)
```

We can further limit the search to people involved in screw propellers
by searching for `screw.*propeller` ("screw" followed by anything followed
by "propeller"), e.g.

```python
for row in df[ df["Biography"].str.contains(r"screw.*propeller", case=False) ].values:
    print(row)
```

## Excel

We can read and write excel files :-)

```python
df.to_excel("data.xlsx", sheet_name="Sheet 1")
```

will write the data to the file `data.xlsx`, writing to a sheet called
`Sheet 1`.

You can also write the search results to Excel, e.g.

```python
df[ df["Biography"].str.contains(r"propeller", case=False) ].to_excel("data.xlsx", sheet_name="Sheet 1")
```

You can read data from Excel too, e.g. the Excel file `invested.xlsx` contains
the (fictional!) amounts of money invested by different people in the project.

```python
invested = pd.read_excel("invested.xlsx")
```

## Merging in financial data

We can merge in the financial data using `pd.merge`

```python
df = pd.merge(df, invested, on="ID")
df.head()
```

We can plot this as a bar chart using

```python
df.plot.bar(x="Name", y="Invested")
```

You can also plot the results of searches, e.g.

```python
df[ df["Biography"].str.contains("propeller", case=False) ].plot.bar(x="Name", y="Invested")
```

You can change to see how much was invested by people involved with 
the Archimedes trials, e.g.

```python
df[ df["Biography"].str.contains("archimedes", case=False) ].plot.bar(x="Name", y="Invested")
```

You can calculate the total sum invested using

```python
df["Invested"].sum()
```

You can also get other statistical values using

```python
print(df["Invested"].mean())
print(df["Invested"].median())
print(df["Invested"].max())
print(df["Invested"].min())
```

You can find the people who invested the most using

```python
df[ df["Invested"] == df["Invested"].max() ]
```

We can see everyone who invested more than the median using

```python
df[ df["Invested"] > df["Invested"].median() ]
```

and we can plot everyone who invested more than 80% of the maximum using

```python
df[ df["Invested"] > 0.8 * df["Invested"].max() ].plot.bar(x="Name", y="Invested")
```

## Grouping by category

The "Affiliations" column contains the colon-separated affiliations of the
people in the project. The `groupby` function can arrange data into groups, e.g.

```python
df.groupby("Affiliations").sum()
```

prints the sum of the investments for each group, while

```python
df.groupby("Affiliations").sum().plot.bar()
```

will plot these as a bar chart.

The groups are all of the combined affiliations. If we want to sum the contributions
from everyone associated with "GWR" then we could type...

```python
df[ df["Affiliations"].str.contains("GWR") ]
```

However, this doesn't work because many of the affiliations are empty (null), 
and so the `contains` function won't work

We need to replace the null values with empty strings. We can do this using

```python
df = df.fillna("")
```

Now, you can see that all null values are empty strings, 

```python
df.head()
```

We can now search on affiliation...

```python
df[ df["Affiliations"].str.contains("GWR") ]
```

and get the total invested for members of a specific affiliation

```python
df[ df["Affiliations"].str.contains("GWR") ]["Invested"].sum()
```

We can print the total invested by each affiliation using

```python
for affiliation in ["B&A", "BCC", "BDC", "GWR", "RN", "SMV"]:
    print(affiliation, df[ df["Affiliations"].str.contains(affiliation) ]["Invested"].sum())
```

And we can graph this by placing the data into a new pandas dataframe, e.g.

```python
data = {"Affiliation": [], "Invested": []}

for affiliation in ["B&A", "BCC", "BDC", "GWR", "RN", "SMV"]:
    data["Affiliation"].append(affiliation)
    data["Invested"].append(df[ df["Affiliations"].str.contains(affiliation) ]["Invested"].sum())

pd.DataFrame(data).plot.bar(x="Affiliation", y="Invested")
```

## Conclusion

[This notebook brings all of the above together](https://raw.githubusercontent.com/chryswoods/teaching/master/python_pandas/lesson.ipynb)


