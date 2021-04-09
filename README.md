 # Video Game Project

------------

<h3> <a name="top"></a> Hi there 👋,</h3>

Welcome to the README file for my Video Game Project.

In here, you will find expanded information on this project including goals, how we will be working through the pipeline and a data dictionary to help offer more insight to the variables that are being used.

------------
## Image goes here 
​
***
[[Project Description](#project_description)]
[[Project Planning](#planning)]
[[Key Findings](#findings)]
[[Data Dictionary](#dictionary)]
[[Data Acquire and Prep](#wrangle)]
[[Data Exploration](#explore)]
[[Statistical Analysis](#stats)]
[[Modeling](#model)]
[[Conclusion](#conclusion)]
___
​
​

------
## <a name="project_description"></a>Project Description:


The goal of this project is to predict Critic Score using a dataframe acquired from Kaggle regarding video games that have been rated by Metacritic within the last 50 years. Using clustering I intend to make new features and explore to find drivers of Critic Score. At which point I will attempt to make a regression model that will beat the baseline prediction.

<u>Data Source</u>

* The data can also be pulled from Kaggle.com 
    * https://www.kaggle.com/rush4ratio/video-game-sales-with-ratings?select=Video_Games_Sales_as_at_22_Dec_2016.csv
* This repository also has a CSV of the data available as well


[[Back to top](#top)]
​

------------
## Goals
​
The goals of the project are to answer the questions and deliver the following:
​
- Use clustering to identify what groups of features are the strongest drivers of Critic Score
- Deliver a final notebook that shows the key drivers behind Critic Score

​
***
## <a name="planning"></a>Project Planning: 



A link to the Trello board below can be found at https://trello.com/b/1kU88xjk/video-game-project



[[Back to top](#top)]
​

----------
### Projet Outline:
- Acquisiton of data through Kaggle
- Prepare and clean data with python - Jupyter Labs Notebook
- Explore data
    - if value are what the dictionary says they are
    - null values
        - are the fixable or should they just be deleted
    - categorical or continuous values
    - Make graphs that show 
- Run statistical analysis
- Model data 
- Test Data
- Conclude results
 
----------- 


## <a name="dictionary"></a>Data Dictionary  
[[Back to top](#top)]

---
|   Feature      |  Data Type   | Description    |
| :------------- | :----------: | -----------: |
|  Platform | object  | Which video game platform the game was released on originally    |
| Year_of_Release    | int64| Year the video game was originally released|
| Genre  | object | Genre the video game fits into|
| NA_Sales | float64 |Number, in millions, of sales the video game had in North America|
|  EU_Sales    | float64  | Number, in millions, of sales the video game had in Europe   |
| JP_Sales   | float64 | Number, in millions, of sales the video game had in Japan|
| Other_Sales    | float64| Number, in millions, of sales the video game had in all other markets|
| Global_Sales | float64 | Number, in millions, of sales the video game had worldwide |
|  Critic_Score  | float64   | Score, from 1 - 100, assigned to the game by professional critics indicating the video games quality |
| Critic_Count    | float64 | Number of critics who rated the game|
| User_Score   | float64 | Score, from 1 - 10, assigned to the game from average consumers on whether or not they enjoyed the video game|
| Rating   | object | Rating, assigned by the ESRB, indicating the appropriate minimum age of the video games audiance |

​
***
​
\* - Indicates the target feature in this Zillow data.
​
​
***
​

-------------------
  <h3><u>Hypothesis and Questions</u></h3>




<h5> The questions above will be answered using t-tests and correlation tests.</h5>


-------------------
  <h3><u>Takeaways</u></h3>
 


--------------------
 <h3><u>How To Recreate This Project</u></h3>
 
 
--------------------

