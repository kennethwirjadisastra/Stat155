# Weather Prediction Model
Kenneth Wirjadisastra

In this project, we train a machine learning model to predict the
temperature in Denver, CO based on historical weather data in the area.
The goal is to use a recurrent neural network (RNN) to predict the
tomorrow’s temperature based on previous weather data in the area.

## [Project 1](Project1)

In Project 1, we delimit the problem. This included introducing the
motivation behind the question and finding data. Once data has been
obtained, we must clean it before moving on to EDA in Project 2. We also
merge data from multiple locations in Denver, CO and split the resulting
data set into training, testing, and validation sets.

### Reproducing [Project 1](Project1)

-   Run `*_data_clean.ipynb` to generate the cleaned data, found in
    [`clean_data`](Project1/clean_data)
-   Split the data into training, validation, and testing by running
    [`split_data.ipynb`](Project1/split_data.ipynb). Data from Denver
    Centennial Airport (`APA`) will be used for modeling.
-   Merge the training data by running
    [`data_merge.ipynb`](Project1/data_merge.ipynb). This data will be
    used by [`EDA.ipynb`](Project2/EDA.ipynb) in [Project2](Project2).

## [Project 2](Project2)

In Project 2, we perform exploratory data analysis (EDA). This allows us
to describe the data and explore the relationships between variables.
The aim is to produce plots that help us answer the question of
interest: what will tomorrow’s temperature be given recent temperatures
around Denver, CO?

### Reproducing [Project 2](Project2)

-   Reproduce [Project 1](Project1) by following the steps above.
-   Run [`EDA.ipynb`](Project2/EDA.ipynb) to perform exploratory data
    analysis

## [Project 3](Project3)

In Project 3, we create a model to help us determine what tomorrow’s
temperature will be like in Centennial, CO. We will build and train an
RNN in PyTorch and evaluate its performance.

### Reproducing [Project 3](Project3)

-   Generate training, validation, and testing data by reproducing
    [Project 1](Project1)
-   Run [`RNN_model.ipynb`](Project3/RNN_model.ipynb) to model the
    weather in Denver Centennial Airport.

## [Project 4](Project4)

In Project 4, we evaluate how the amount of missing data and the
imputation methods used impact our model’s performance. We will test
various amounts of missing data and use techniques such as Kalman
Smoother, moving average, and linear interpolation to impute the
training data to train our model. Then we will test its performance on
the true test data.

### Reproducing [Project 4](Project4)

-   While this project is not dependent on [Project 3](Project3), it is
    recommended to reproduce [Project 3](Project3) before continuing to
    [Project 4](Project4)
-   Generate training, validation, and testing data by reproducing
    [Project 1](Project1)
-   Run
    [`project4_simulation_wirjadisastra_kenneth.ipynb`](Project4/project4_simulation_wirjadisastra_kenneth.ipynb)
-   Run [`anova.ipynb`](Project4/anova.ipynb)

## Session Info

------------------------------------------------------------------------

`matplotlib          3.10.1`

`numpy               1.26.4`

`pandas              2.2.3`

`scipy               1.15.2`

`seaborn             0.13.2`

`session_info        v1.0.1`

`sklearn             1.6.1`

`statsmodels         0.14.4`

`torch               2.7.0`

------------------------------------------------------------------------

`IPython             9.2.0`

`jupyter_client      8.6.3`

`jupyter_core        5.7.2`

------------------------------------------------------------------------

`Python 3.11.1`

`Windows-10-10.0.26100-SP0`

------------------------------------------------------------------------
