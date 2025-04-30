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
following day’s weather. Our model’s goal is to produce <u>sparse and
interpretable</u> model that uncovers the dynamics of the weather system
in Denver, CO.**

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

Below we show a preview of the raw data for DEN. There are 7370 rows and
39 columns in the dataframe.

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
df.raw <- read.csv("./raw_data/DEN_weather_raw.csv")
glimpse(df.raw)
```

    Rows: 7,370
    Columns: 39
    $ STATION <chr> "USW00003017", "USW00003017", "USW00003017", "USW00003017", "U…
    $ NAME    <chr> "DENVER INTERNATIONAL AIRPORT, CO US", "DENVER INTERNATIONAL A…
    $ DATE    <chr> "2005-01-01", "2005-01-02", "2005-01-03", "2005-01-04", "2005-…
    $ AWND    <dbl> 9.40, 5.59, 4.92, 8.50, 4.70, 8.05, 10.96, 10.51, 11.41, 6.26,…
    $ FMTM    <int> 10, 326, 1519, 1031, 2348, 2005, 1122, 1244, 1137, 145, 216, 7…
    $ PGTM    <int> 1048, 325, 1523, 1031, 50, 2004, 2359, 1244, 1137, 1235, 433, …
    $ PRCP    <dbl> 0.00, 0.00, 0.00, 0.02, 0.10, 0.00, 0.00, 0.00, 0.00, 0.00, 0.…
    $ PSUN    <int> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA…
    $ SNOW    <dbl> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA…
    $ SNWD    <dbl> NA, NA, NA, NA, 1, 2, 2, NA, NA, NA, NA, NA, NA, NA, NA, NA, N…
    $ TAVG    <int> 32, 27, 30, 16, 2, 21, 17, 30, 46, 31, 32, 22, 23, 22, 26, 22,…
    $ TMAX    <int> 43, 33, 41, 26, 6, 40, 28, 50, 60, 40, 36, 30, 40, 42, 41, 36,…
    $ TMIN    <int> 20, 20, 18, 5, -3, 1, 6, 10, 31, 22, 27, 14, 6, 2, 10, 7, 17, …
    $ TSUN    <int> 0, 0, 0, 0, 0, NA, 0, 0, 0, 0, 0, 0, 0, 0, NA, 0, 0, 0, 0, 0, …
    $ WDF2    <int> 160, 170, 60, 20, 210, 310, 110, 240, 250, 170, 130, 350, 280,…
    $ WDF5    <int> 20, 170, 60, 20, 30, 300, 300, 240, 250, 310, 130, 350, 280, 7…
    $ WESD    <dbl> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA…
    $ WSF2    <dbl> 16.1, 16.1, 13.0, 17.9, 10.1, 25.1, 19.9, 23.0, 34.9, 15.0, 15…
    $ WSF5    <dbl> 17.0, 17.0, 14.1, 21.0, 12.1, 31.1, 23.9, 29.1, 40.9, 16.1, 16…
    $ WT01    <int> NA, NA, 1, 1, 1, NA, NA, NA, NA, 1, 1, 1, 1, 1, 1, 1, NA, NA, …
    $ WT02    <int> NA, NA, 1, 1, 1, NA, NA, NA, NA, 1, 1, 1, NA, 1, 1, NA, NA, NA…
    $ WT03    <int> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA…
    $ WT04    <int> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA…
    $ WT05    <int> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA…
    $ WT06    <int> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, 1, NA, NA, NA, NA,…
    $ WT07    <int> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA…
    $ WT08    <int> NA, NA, 1, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, 1, NA, …
    $ WT09    <int> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA…
    $ WT10    <int> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA…
    $ WT11    <int> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA…
    $ WT13    <int> NA, NA, 1, 1, 1, NA, NA, NA, NA, 1, 1, 1, 1, 1, 1, 1, NA, NA, …
    $ WT14    <int> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA…
    $ WT15    <int> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA…
    $ WT16    <int> NA, NA, NA, NA, NA, NA, NA, NA, NA, 1, NA, 1, NA, NA, NA, NA, …
    $ WT17    <int> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, 1, NA, NA, NA, NA,…
    $ WT18    <int> NA, NA, NA, 1, 1, NA, NA, NA, NA, NA, NA, 1, NA, 1, 1, NA, NA,…
    $ WT19    <int> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA…
    $ WT21    <int> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA…
    $ WT22    <int> NA, NA, 1, 1, 1, NA, NA, NA, NA, 1, 1, 1, NA, 1, 1, NA, NA, NA…

There are a lot of missing values in the dataset. We clean the data
using the script in the data sub-directory. We removed rows and columns
with many NaN values. There are now 6972 rows and 13 columns. This is
what the data looks like after cleaning.

``` r
library(tidyverse)
df.clean <- read.csv("./clean_data/DEN_weather_clean.csv")
glimpse(df.clean)
```

    Rows: 6,971
    Columns: 14
    $ DATE    <chr> "2006-02-01", "2006-02-02", "2006-02-03", "2006-02-04", "2006-…
    $ STATION <chr> "USW00003017", "USW00003017", "USW00003017", "USW00003017", "U…
    $ NAME    <chr> "DENVER INTERNATIONAL AIRPORT, CO US", "DENVER INTERNATIONAL A…
    $ AWND    <dbl> 8.05, 12.30, 10.96, 9.40, 16.78, 8.95, 7.83, 9.40, 15.88, 12.7…
    $ PRCP    <dbl> 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.03, 0.02, 0.…
    $ SNOW    <dbl> 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.9, 0.2, 0.0, 0.0, 0.…
    $ SNWD    <dbl> 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 1, 1, 1, 1, 0, 0,…
    $ TMAX    <dbl> 53, 47, 44, 53, 46, 45, 51, 61, 57, 25, 35, 53, 51, 60, 45, 21…
    $ TMIN    <dbl> 22, 23, 22, 16, 19, 17, 14, 23, 20, 9, 5, 11, 24, 30, 20, 3, -…
    $ WDF2    <dbl> 20, 310, 340, 140, 10, 220, 170, 280, 30, 10, 300, 30, 210, 60…
    $ WDF5    <dbl> 30, 310, 340, 140, 10, 110, 220, 330, 40, 360, 300, 20, 210, 6…
    $ WSF2    <dbl> 21.0, 25.9, 36.9, 21.0, 36.0, 15.0, 14.1, 16.1, 31.1, 25.9, 14…
    $ WSF5    <dbl> 25.1, 30.0, 46.1, 23.9, 42.9, 17.0, 15.0, 19.9, 36.0, 32.0, 16…
    $ TARGET  <dbl> 47, 44, 53, 46, 45, 51, 61, 57, 25, 35, 53, 51, 60, 45, 21, 14…

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
