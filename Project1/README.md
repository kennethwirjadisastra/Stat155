# Project 1


# Weather Prediction Model

Weather forecasting models have become integrated in our daily lives.
Many of us rely on these models to make informed decisions. These
decisions can be inconsequential (what to wear tomorrow) or significant
(how should a city allocate its resources).

Because of the chaotic nature of the weather, it is difficult to find a
model that accurately models its time evolution. In this project, we aim
to minimize the error in the model prediction given historical weather
data. We will implement a regression and compare its results to that of
a neural network and discuss the applications of both.

**Goal: Given historical weather data, our goal will be to predict the
following day’s weather.**

## Data

The data was collected at <https://www.ncdc.noaa.gov/cdo-web/datasets>.
We combine data from four different stations (DEN, APA, Central Park,
and Denver Water Department). The stations in these locations collect
data daily. For this project, we consider observations from January 01,
2005 up until the most recent data in early April 2025.

Each dataset contains a slightly different number of columns ranging
from 17 to 39. Some of the notable variables include precipitation (in),
snowfall (in.), snow depth (in.), daily maximum temperature (F), and
daily minimum temperature. The number of observations in each dataset
also varies depending on how recently the data was updated. The number
of observations ranges between 7288 and 7378.

Below we show a preview of the raw data from Centennial Airport. There
are nearly 7,400 rows and 27 columns in the dataframe.

``` r
# install.packages("tidyverse")
library(tidyverse)
```

    ── Attaching core tidyverse packages ──────────────────────── tidyverse 2.0.0 ──
    ✔ dplyr     1.1.4     ✔ readr     2.1.5
    ✔ forcats   1.0.0     ✔ stringr   1.5.1
    ✔ ggplot2   3.5.1     ✔ tibble    3.2.1
    ✔ lubridate 1.9.3     ✔ tidyr     1.3.1
    ✔ purrr     1.0.2     
    ── Conflicts ────────────────────────────────────────── tidyverse_conflicts() ──
    ✖ dplyr::filter() masks stats::filter()
    ✖ dplyr::lag()    masks stats::lag()
    ℹ Use the conflicted package (<http://conflicted.r-lib.org/>) to force all conflicts to become errors

``` r
df.raw <- read.csv("./raw_data/APA_weather_raw.csv")
glimpse(df.raw)
```

    Rows: 7,398
    Columns: 27
    $ STATION <chr> "USW00093067", "USW00093067", "USW00093067", "USW00093067", "U…
    $ NAME    <chr> "DENVER CENTENNIAL AIRPORT, CO US", "DENVER CENTENNIAL AIRPORT…
    $ DATE    <chr> "2005-01-01", "2005-01-02", "2005-01-03", "2005-01-04", "2005-…
    $ AWND    <dbl> 7.61, 5.14, 4.47, 7.16, 3.80, 6.04, 7.83, 16.11, 14.09, 6.26, …
    $ FMTM    <int> 1056, 655, 1519, 1103, 458, 214, 2226, 1228, 1202, 225, 1611, …
    $ PGTM    <int> 1002, 654, 1520, 1103, 249, 208, 2226, 1221, 1202, 1324, 1611,…
    $ PRCP    <dbl> 0.00, 0.00, 0.00, 0.00, 0.00, 0.18, 0.00, 0.00, 0.00, 0.00, 0.…
    $ SNOW    <dbl> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA…
    $ SNWD    <dbl> NA, NA, NA, NA, NA, 2, 2, 1, NA, NA, NA, NA, 3, 2, 1, 1, 1, NA…
    $ TAVG    <int> 37, 28, 33, 17, 4, 22, 21, 31, 48, 40, 34, 24, 26, 25, 27, 29,…
    $ TMAX    <int> 51, 34, 49, 28, 7, 41, 31, 48, 59, 55, 41, 31, 40, 45, 44, 45,…
    $ TMIN    <int> 22, 21, 17, 6, 1, 3, 10, 13, 37, 25, 26, 16, 12, 4, 9, 13, 25,…
    $ TSUN    <int> 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,…
    $ WDF2    <int> 260, 160, 50, 340, 10, 150, 160, 230, 240, 180, 340, 360, 290,…
    $ WDF5    <int> 250, 160, 50, 340, 20, 150, 150, 230, 240, 320, 330, 10, 290, …
    $ WSF2    <dbl> 21.0, 14.1, 14.1, 19.9, 8.9, 14.1, 23.0, 33.1, 32.0, 15.0, 13.…
    $ WSF5    <dbl> 29.1, 15.0, 16.1, 21.0, 10.1, 17.0, 25.9, 40.9, 38.0, 16.1, 15…
    $ WT01    <int> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA…
    $ WT02    <int> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA…
    $ WT03    <int> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA…
    $ WT04    <int> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA…
    $ WT05    <int> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA…
    $ WT06    <int> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA…
    $ WT07    <int> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA…
    $ WT08    <int> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA…
    $ WT09    <int> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA…
    $ WT10    <int> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA…

There are a lot of missing values in the dataset. We clean the data
using the [APA_data_clean.ipynb](./APA_data_clean.ipynb). We the columns
with many NaN values. There are now only 12 columns. This is what the
data looks like after cleaning.

``` r
library(tidyverse)
df.clean <- read.csv("./clean_data/APA_weather_clean.csv")
glimpse(df.clean)
```

    Rows: 7,397
    Columns: 12
    $ DATE    <chr> "2005-01-01", "2005-01-02", "2005-01-03", "2005-01-04", "2005-…
    $ STATION <chr> "USW00093067", "USW00093067", "USW00093067", "USW00093067", "U…
    $ NAME    <chr> "DENVER CENTENNIAL AIRPORT, CO US", "DENVER CENTENNIAL AIRPORT…
    $ AWND    <dbl> 7.61, 5.14, 4.47, 7.16, 3.80, 6.04, 7.83, 16.11, 14.09, 6.26, …
    $ PRCP    <dbl> 0.00, 0.00, 0.00, 0.00, 0.00, 0.18, 0.00, 0.00, 0.00, 0.00, 0.…
    $ TMAX    <dbl> 51, 34, 49, 28, 7, 41, 31, 48, 59, 55, 41, 31, 40, 45, 44, 45,…
    $ TMIN    <dbl> 22, 21, 17, 6, 1, 3, 10, 13, 37, 25, 26, 16, 12, 4, 9, 13, 25,…
    $ WDF2    <dbl> 260, 160, 50, 340, 10, 150, 160, 230, 240, 180, 340, 360, 290,…
    $ WDF5    <dbl> 250, 160, 50, 340, 20, 150, 150, 230, 240, 320, 330, 10, 290, …
    $ WSF2    <dbl> 21.0, 14.1, 14.1, 19.9, 8.9, 14.1, 23.0, 33.1, 32.0, 15.0, 13.…
    $ WSF5    <dbl> 29.1, 15.0, 16.1, 21.0, 10.1, 17.0, 25.9, 40.9, 38.0, 16.1, 15…
    $ TARGET  <dbl> 34, 49, 28, 7, 41, 31, 48, 59, 55, 41, 31, 40, 45, 44, 45, 48,…

The rest of the data (both raw and cleaned) and the scripts used maybe
found by navigating to the [raw_data subdirectory](./raw_data).

## Data Dictionary

The data dictionary for the cleaned DEN weather data is as follows:

<table>
<thead>
<tr class="header">
<th>Variable</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PRCP</td>
<td>Precipitation in inches</td>
</tr>
<tr class="even">
<td>SNOW</td>
<td>Snowfall in inches</td>
</tr>
<tr class="odd">
<td>SNWD</td>
<td>Snow depth in inches</td>
</tr>
<tr class="even">
<td>TMAX</td>
<td>Maximum temperature in degrees Fahrenheit</td>
</tr>
<tr class="odd">
<td>TMIN</td>
<td>Minimum temperature in degrees Fahrenheit</td>
</tr>
<tr class="even">
<td>AWND</td>
<td>Average daily wind speed in miles per hour</td>
</tr>
<tr class="odd">
<td>WDF2</td>
<td>Direction of fastest two minute wind speed in degrees</td>
</tr>
<tr class="even">
<td>WDF5</td>
<td>Direction of fastest five minute wind speed in degrees</td>
</tr>
<tr class="odd">
<td>WSF2</td>
<td>Fastest two minute wind speed in miles per hour</td>
</tr>
<tr class="even">
<td>WSF5</td>
<td>Fastest five minute wind speed in miles per hour</td>
</tr>
</tbody>
</table>

The full data dictionary can be found
[here](raw_data/GSOM_documentation.pdf) in the raw_data sub-directory.
This applies to all data sets and may include variables not present in
the data sets.

## Workflow

To start, we clean the data using
[APA_weather_clean.ipynb](./APA_weather_clean.ipynb),
[central_park_weather_clean.ipynb](./central_park_weather_clean.ipynb),
[DEN_weather_clean.ipynb](./DEN_weather_clean.ipynb), and
[water_dept_weather_clean.ipynb](./water_dept_weather_clean.ipynb).
These will generate the `csv` files found in the
[clean_data](./clean_data) subdirectory. Next we merge our data by
running [data_merge.ipynb](./data_merge.ipynb) to generate the data in
[merged_data](./merged_data). This data will be used for EDA in [Project
2](../Project2) Finally, we split the data in [clean_data](./clean_data)
by running [split_data.ipynb](./split_data.ipynb) to generate the
training, validation, and test data sets in [train_data](./train_data),
[validation_data](./validation_data), and [test_data](./test_data).
