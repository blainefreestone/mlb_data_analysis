# Overview

[Video Explanation](http://youtube.link.goes.here)

## The Dataset

The data analyzed by this program is [The Baseball Databank](https://www.kaggle.com/datasets/open-source-sports/baseball-databank) which is data on baseball players, teams, and games from 1871 to 2015. 

This dataset has four main tables: **Main** (player names, DOB, and biographical info), **Batting** (batting statistics), **Pitching** (pitching statistics), and **Fielding** (fielding statistics). 

In this program we utilize the **Main**  and **Batting** tables.

The **Main** table has 18,846 rows and contains information about individual players. The table looks like this:
|playerID|birthYear|birthMonth|...|nameFirst|nameLast|weight|height|bats|
|-|-|-|-|-|-|-|-|-|
|aardsda01|1981|12|...|David|Aardsma|220|75|R|
|zychto01|1990|8|...|Tony|Zych|190|75|R|

The **Batting** table has 101,332 rows and contains batting data for individual players in a year. The table looks like this:
|playerID|yearID|...|AB|R|H|2B|...|BB|
|-|-|-|-|-|-|-|-|-|
|zobribe01|2015|...|235|39|63|20|...|33|
|allisar01|1871|...|137|28|40|4|...|2|

{Describe the methods of combining and organizing tables}

## The Program Objectives

The questions I aim to answer with this dataset are:
- How have league-wide batting statistics (such as AVG, OBP, and SLG) changed over the history of the MLB (from 1871 to 2015)?
- How have the same batting statistics changed over a given player's individual career?
- Based on a set of features for a given player (past batting data, age, etc.), and given the number of at bats in a season, what is a predicted batting average (AVG)?

# Data Analysis Results

# Development

This program was developed using **Visual Studio Code** and **Python 3.11.3**.

The following Python libraries were used:
- Pandas
- sklearn
- matplotlib

# Useful Resources

- [Kaggle](http://url.link.goes.here)

# Future Work

This project was an excercise in **writing software** to analyze complex and large datasets. I am not a data scientist and therefore many improvements in the *methods* of analyzing this data are possible, such as:

* Better feature engineering.
* Improvements in how league-wide statistical data is shown over time.

In terms of the software itself, there are many improvements and additions that could be made:

* A UI to interact with the data and the way in which it is displayed.