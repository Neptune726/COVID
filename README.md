# COVID-19-Plotting-and-Modeling

A repository for modeling and analysing the current COVID pandemic. Below is a description of each file in this repo:

## Part 1 - ExploratoryAnalysisOfCOVIDData.ipynb
A brief Jupyter notebook for exploratory Analysis of COVID data.

## Part 2 - Simple Model of American Covid Deaths.ipynb
Notebook for a simple model using that uses poisson and bernoulli random variables to try to model American Coronavirus deaths: <br/> 
![equation](https://latex.codecogs.com/gif.latex?%5Chat%7Bd_%7Bi%7D%7D%3D%5Csum_%7Bi%7D%5E%7Bn%7D%20p_%7Bdeath%7D%20%5Ccdot%20possion%28n-i%2C%5Clambda%29%20%5Ccdot%20c%28i%29) <br/>
Where ![equation](https://latex.codecogs.com/gif.latex?c%28i%29) is the new cases in America for day ![equation](https://latex.codecogs.com/gif.latex?i) and ![equation](https://latex.codecogs.com/gif.latex?possion%28x%2C%5Clambda%29) is the PMF of a poisson random variable with parameter ![equation](https://latex.codecogs.com/gif.latex?%5Clambda) at ![equation](https://latex.codecogs.com/gif.latex?x). This model is trained using stochastic gradient descent

## Part 3 - Decay Model of American COVID Deaths.ipynb
An iteration on the model in part two where ![equation](https://latex.codecogs.com/gif.latex?p_%7Bdeath%7D) now exponentialy decays to 0 with time: <br/>
![equation](https://latex.codecogs.com/gif.latex?p_%7Bdeath%7D%20%5Cpropto%20e%5E%7B-s%20%5Ccdot%20t%7D) <br/>
For some constant ![equation](https://latex.codecogs.com/gif.latex?s).

## Utils python files
The Utils python files, listed below, are just some helper functions that I had already written in the notebooks above. I copy pasted them into a seperate file so that I could import and use them again for future notebooks. <br/>
Util .py files:
- **Utils.py** Some functions originally written in Part 1 - ExploratoryAnalysisOfCOVIDData.ipynb notebook
- **COVID_death_utils.py** Some function originally written in Part 2 - Simple Model of American Covid Deaths.ipynb

## CSV data files
CSV data files, file names listed below, are downloaded from the Johns Hobpkins COVID-19 repository: [CSSEGI repo](https://github.com/CSSEGISandData/COVID-19) <br/>

CSV data files:
- **time_series_covid19_confirmed_US.csv** Confirmed American Cases (downloaded on 8/14/20)
- **time_series_covid19_confirmed_global.csv** Confirmed Global Cases, excluding America, (downloaded on 8/14/20)
- **time_series_covid19_deaths_US.csv** American Deaths due to COVID 19 (downloaded on 8/14/20)
- **time_series_covid19_deaths_global.csv** Global Deaths, exluding America, due to COVID-19 (downloaded on 8/14/20)
