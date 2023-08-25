{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "20b52443",
   "metadata": {
    "_cell_guid": "b1076dfc-b9ad-4769-8c92-a6c4dae69d19",
    "_uuid": "8f2839f25d086af736a60e9eeb907d3b93b6e0e5",
    "execution": {
     "iopub.execute_input": "2022-12-09T21:06:35.196282Z",
     "iopub.status.busy": "2022-12-09T21:06:35.194558Z",
     "iopub.status.idle": "2022-12-09T21:06:38.833835Z",
     "shell.execute_reply": "2022-12-09T21:06:38.832312Z"
    },
    "papermill": {
     "duration": 3.64983,
     "end_time": "2022-12-09T21:06:38.836102",
     "exception": false,
     "start_time": "2022-12-09T21:06:35.186272",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "── \u001b[1mAttaching packages\u001b[22m ─────────────────────────────────────── tidyverse 1.3.2 ──\n",
      "\u001b[32m✔\u001b[39m \u001b[34mggplot2\u001b[39m 3.3.6      \u001b[32m✔\u001b[39m \u001b[34mpurrr  \u001b[39m 0.3.5 \n",
      "\u001b[32m✔\u001b[39m \u001b[34mtibble \u001b[39m 3.1.8      \u001b[32m✔\u001b[39m \u001b[34mdplyr  \u001b[39m 1.0.10\n",
      "\u001b[32m✔\u001b[39m \u001b[34mtidyr  \u001b[39m 1.2.1      \u001b[32m✔\u001b[39m \u001b[34mstringr\u001b[39m 1.4.1 \n",
      "\u001b[32m✔\u001b[39m \u001b[34mreadr  \u001b[39m 2.1.3      \u001b[32m✔\u001b[39m \u001b[34mforcats\u001b[39m 0.5.2 \n",
      "── \u001b[1mConflicts\u001b[22m ────────────────────────────────────────── tidyverse_conflicts() ──\n",
      "\u001b[31m✖\u001b[39m \u001b[34mdplyr\u001b[39m::\u001b[32mfilter()\u001b[39m masks \u001b[34mstats\u001b[39m::filter()\n",
      "\u001b[31m✖\u001b[39m \u001b[34mdplyr\u001b[39m::\u001b[32mlag()\u001b[39m    masks \u001b[34mstats\u001b[39m::lag()\n",
      "\n",
      "Attaching package: ‘MASS’\n",
      "\n",
      "\n",
      "The following object is masked from ‘package:dplyr’:\n",
      "\n",
      "    select\n",
      "\n",
      "\n",
      "\n",
      "Attaching package: ‘xgboost’\n",
      "\n",
      "\n",
      "The following object is masked from ‘package:dplyr’:\n",
      "\n",
      "    slice\n",
      "\n",
      "\n",
      "Loading required package: lattice\n",
      "\n",
      "\n",
      "Attaching package: ‘caret’\n",
      "\n",
      "\n",
      "The following objects are masked from ‘package:Metrics’:\n",
      "\n",
      "    precision, recall\n",
      "\n",
      "\n",
      "The following object is masked from ‘package:purrr’:\n",
      "\n",
      "    lift\n",
      "\n",
      "\n",
      "The following object is masked from ‘package:httr’:\n",
      "\n",
      "    progress\n",
      "\n",
      "\n",
      "Loading required package: Matrix\n",
      "\n",
      "\n",
      "Attaching package: ‘Matrix’\n",
      "\n",
      "\n",
      "The following objects are masked from ‘package:tidyr’:\n",
      "\n",
      "    expand, pack, unpack\n",
      "\n",
      "\n",
      "Loaded glmnet 4.1-4\n",
      "\n"
     ]
    }
   ],
   "source": [
    "\n",
    "library(tidyverse) # metapackage of all tidyverse packages\n",
    "library(ggplot2)\n",
    "library(dplyr)\n",
    "# install.packages(\"zipcodeR\")\n",
    "# library(zipcodeR)\n",
    "# list.files(path = \"../input\")\n",
    "library(MASS)\n",
    "library(caTools)\n",
    "library(Metrics)\n",
    "library(xgboost)\n",
    "# library(randomForest)\n",
    "# install.packages(\"BART\")\n",
    "# library(BART)\n",
    "# install.packages(\"neuralnet\")\n",
    "# library(neuralnet)\n",
    "library(caret)\n",
    "library(glmnet)\n",
    "# install.packages('bartMachine')\n",
    "# library(bartMachine)\n",
    "# install.packages(\"rpart\")\n",
    "library(rpart)\n",
    "library(rpart.plot)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "7e82d992",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T21:06:38.893339Z",
     "iopub.status.busy": "2022-12-09T21:06:38.849920Z",
     "iopub.status.idle": "2022-12-09T21:08:03.012737Z",
     "shell.execute_reply": "2022-12-09T21:08:03.011174Z"
    },
    "papermill": {
     "duration": 84.172615,
     "end_time": "2022-12-09T21:08:03.014943",
     "exception": false,
     "start_time": "2022-12-09T21:06:38.842328",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "train <- read.csv('/kaggle/input/train-test-stat/stat_5600_train_df.csv')\n",
    "test <- read.csv('/kaggle/input/train-test-stat/stat_5600_test_df.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "faf82f19",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T21:08:03.032469Z",
     "iopub.status.busy": "2022-12-09T21:08:03.030870Z",
     "iopub.status.idle": "2022-12-09T21:08:03.060083Z",
     "shell.execute_reply": "2022-12-09T21:08:03.058842Z"
    },
    "papermill": {
     "duration": 0.039439,
     "end_time": "2022-12-09T21:08:03.062012",
     "exception": false,
     "start_time": "2022-12-09T21:08:03.022573",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<table class=\"dataframe\">\n",
       "<caption>A data.frame: 6 × 20</caption>\n",
       "<thead>\n",
       "\t<tr><th></th><th scope=col>b2c_c2c</th><th scope=col>seller_id</th><th scope=col>declared_handling_days</th><th scope=col>shipment_method_id</th><th scope=col>shipping_fee</th><th scope=col>item_zip</th><th scope=col>buyer_zip</th><th scope=col>category_id</th><th scope=col>item_price</th><th scope=col>quantity</th><th scope=col>delivery_date</th><th scope=col>weight</th><th scope=col>package_size</th><th scope=col>carrier_average_estimate</th><th scope=col>zip_distance</th><th scope=col>acceptance_date</th><th scope=col>payment_date</th><th scope=col>time_to_process</th><th scope=col>days_to_deliver</th><th scope=col>acceptance_to_delivery</th></tr>\n",
       "\t<tr><th></th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;chr&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;chr&gt;</th><th scope=col>&lt;chr&gt;</th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;int&gt;</th></tr>\n",
       "</thead>\n",
       "<tbody>\n",
       "\t<tr><th scope=row>1</th><td>0</td><td>  4677</td><td>1</td><td>0</td><td>0.00</td><td>90703</td><td>55070</td><td> 1</td><td>25.00</td><td>1</td><td>2018-07-30</td><td>1.360776</td><td>6</td><td>4</td><td>1528.26</td><td>2018-07-27</td><td>2018-07-26</td><td>1</td><td>4</td><td>3</td></tr>\n",
       "\t<tr><th scope=row>2</th><td>0</td><td>   104</td><td>1</td><td>0</td><td>0.00</td><td>91304</td><td>60565</td><td>11</td><td> 5.70</td><td>1</td><td>2019-02-11</td><td>0.000000</td><td>6</td><td>4</td><td>1734.01</td><td>2019-02-08</td><td>2019-02-08</td><td>0</td><td>3</td><td>3</td></tr>\n",
       "\t<tr><th scope=row>3</th><td>0</td><td>340356</td><td>1</td><td>0</td><td>2.95</td><td>49735</td><td>29379</td><td> 1</td><td> 6.00</td><td>1</td><td>2018-04-25</td><td>0.453592</td><td>6</td><td>4</td><td> 728.16</td><td>2018-04-23</td><td>2018-04-22</td><td>1</td><td>3</td><td>2</td></tr>\n",
       "\t<tr><th scope=row>4</th><td>0</td><td>  2101</td><td>1</td><td>0</td><td>0.00</td><td>51031</td><td>28092</td><td>13</td><td> 9.90</td><td>1</td><td>2018-05-14</td><td>0.907184</td><td>6</td><td>4</td><td> 943.44</td><td>2018-05-08</td><td>2018-05-07</td><td>1</td><td>7</td><td>6</td></tr>\n",
       "\t<tr><th scope=row>5</th><td>0</td><td> 12924</td><td>1</td><td>0</td><td>0.00</td><td>77035</td><td>45373</td><td> 8</td><td>23.99</td><td>1</td><td>2018-08-09</td><td>0.453592</td><td>6</td><td>4</td><td> 957.60</td><td>2018-08-06</td><td>2018-08-06</td><td>0</td><td>3</td><td>3</td></tr>\n",
       "\t<tr><th scope=row>6</th><td>0</td><td>  5815</td><td>0</td><td>0</td><td>0.00</td><td>32605</td><td>33166</td><td>11</td><td>22.78</td><td>2</td><td>2019-05-22</td><td>3.628736</td><td>6</td><td>4</td><td> 294.74</td><td>2019-05-21</td><td>2019-05-20</td><td>1</td><td>2</td><td>1</td></tr>\n",
       "</tbody>\n",
       "</table>\n"
      ],
      "text/latex": [
       "A data.frame: 6 × 20\n",
       "\\begin{tabular}{r|llllllllllllllllllll}\n",
       "  & b2c\\_c2c & seller\\_id & declared\\_handling\\_days & shipment\\_method\\_id & shipping\\_fee & item\\_zip & buyer\\_zip & category\\_id & item\\_price & quantity & delivery\\_date & weight & package\\_size & carrier\\_average\\_estimate & zip\\_distance & acceptance\\_date & payment\\_date & time\\_to\\_process & days\\_to\\_deliver & acceptance\\_to\\_delivery\\\\\n",
       "  & <int> & <dbl> & <int> & <int> & <dbl> & <int> & <int> & <int> & <dbl> & <int> & <chr> & <dbl> & <int> & <dbl> & <dbl> & <chr> & <chr> & <int> & <int> & <int>\\\\\n",
       "\\hline\n",
       "\t1 & 0 &   4677 & 1 & 0 & 0.00 & 90703 & 55070 &  1 & 25.00 & 1 & 2018-07-30 & 1.360776 & 6 & 4 & 1528.26 & 2018-07-27 & 2018-07-26 & 1 & 4 & 3\\\\\n",
       "\t2 & 0 &    104 & 1 & 0 & 0.00 & 91304 & 60565 & 11 &  5.70 & 1 & 2019-02-11 & 0.000000 & 6 & 4 & 1734.01 & 2019-02-08 & 2019-02-08 & 0 & 3 & 3\\\\\n",
       "\t3 & 0 & 340356 & 1 & 0 & 2.95 & 49735 & 29379 &  1 &  6.00 & 1 & 2018-04-25 & 0.453592 & 6 & 4 &  728.16 & 2018-04-23 & 2018-04-22 & 1 & 3 & 2\\\\\n",
       "\t4 & 0 &   2101 & 1 & 0 & 0.00 & 51031 & 28092 & 13 &  9.90 & 1 & 2018-05-14 & 0.907184 & 6 & 4 &  943.44 & 2018-05-08 & 2018-05-07 & 1 & 7 & 6\\\\\n",
       "\t5 & 0 &  12924 & 1 & 0 & 0.00 & 77035 & 45373 &  8 & 23.99 & 1 & 2018-08-09 & 0.453592 & 6 & 4 &  957.60 & 2018-08-06 & 2018-08-06 & 0 & 3 & 3\\\\\n",
       "\t6 & 0 &   5815 & 0 & 0 & 0.00 & 32605 & 33166 & 11 & 22.78 & 2 & 2019-05-22 & 3.628736 & 6 & 4 &  294.74 & 2019-05-21 & 2019-05-20 & 1 & 2 & 1\\\\\n",
       "\\end{tabular}\n"
      ],
      "text/markdown": [
       "\n",
       "A data.frame: 6 × 20\n",
       "\n",
       "| <!--/--> | b2c_c2c &lt;int&gt; | seller_id &lt;dbl&gt; | declared_handling_days &lt;int&gt; | shipment_method_id &lt;int&gt; | shipping_fee &lt;dbl&gt; | item_zip &lt;int&gt; | buyer_zip &lt;int&gt; | category_id &lt;int&gt; | item_price &lt;dbl&gt; | quantity &lt;int&gt; | delivery_date &lt;chr&gt; | weight &lt;dbl&gt; | package_size &lt;int&gt; | carrier_average_estimate &lt;dbl&gt; | zip_distance &lt;dbl&gt; | acceptance_date &lt;chr&gt; | payment_date &lt;chr&gt; | time_to_process &lt;int&gt; | days_to_deliver &lt;int&gt; | acceptance_to_delivery &lt;int&gt; |\n",
       "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|\n",
       "| 1 | 0 |   4677 | 1 | 0 | 0.00 | 90703 | 55070 |  1 | 25.00 | 1 | 2018-07-30 | 1.360776 | 6 | 4 | 1528.26 | 2018-07-27 | 2018-07-26 | 1 | 4 | 3 |\n",
       "| 2 | 0 |    104 | 1 | 0 | 0.00 | 91304 | 60565 | 11 |  5.70 | 1 | 2019-02-11 | 0.000000 | 6 | 4 | 1734.01 | 2019-02-08 | 2019-02-08 | 0 | 3 | 3 |\n",
       "| 3 | 0 | 340356 | 1 | 0 | 2.95 | 49735 | 29379 |  1 |  6.00 | 1 | 2018-04-25 | 0.453592 | 6 | 4 |  728.16 | 2018-04-23 | 2018-04-22 | 1 | 3 | 2 |\n",
       "| 4 | 0 |   2101 | 1 | 0 | 0.00 | 51031 | 28092 | 13 |  9.90 | 1 | 2018-05-14 | 0.907184 | 6 | 4 |  943.44 | 2018-05-08 | 2018-05-07 | 1 | 7 | 6 |\n",
       "| 5 | 0 |  12924 | 1 | 0 | 0.00 | 77035 | 45373 |  8 | 23.99 | 1 | 2018-08-09 | 0.453592 | 6 | 4 |  957.60 | 2018-08-06 | 2018-08-06 | 0 | 3 | 3 |\n",
       "| 6 | 0 |   5815 | 0 | 0 | 0.00 | 32605 | 33166 | 11 | 22.78 | 2 | 2019-05-22 | 3.628736 | 6 | 4 |  294.74 | 2019-05-21 | 2019-05-20 | 1 | 2 | 1 |\n",
       "\n"
      ],
      "text/plain": [
       "  b2c_c2c seller_id declared_handling_days shipment_method_id shipping_fee\n",
       "1 0         4677    1                      0                  0.00        \n",
       "2 0          104    1                      0                  0.00        \n",
       "3 0       340356    1                      0                  2.95        \n",
       "4 0         2101    1                      0                  0.00        \n",
       "5 0        12924    1                      0                  0.00        \n",
       "6 0         5815    0                      0                  0.00        \n",
       "  item_zip buyer_zip category_id item_price quantity delivery_date weight  \n",
       "1 90703    55070      1          25.00      1        2018-07-30    1.360776\n",
       "2 91304    60565     11           5.70      1        2019-02-11    0.000000\n",
       "3 49735    29379      1           6.00      1        2018-04-25    0.453592\n",
       "4 51031    28092     13           9.90      1        2018-05-14    0.907184\n",
       "5 77035    45373      8          23.99      1        2018-08-09    0.453592\n",
       "6 32605    33166     11          22.78      2        2019-05-22    3.628736\n",
       "  package_size carrier_average_estimate zip_distance acceptance_date\n",
       "1 6            4                        1528.26      2018-07-27     \n",
       "2 6            4                        1734.01      2019-02-08     \n",
       "3 6            4                         728.16      2018-04-23     \n",
       "4 6            4                         943.44      2018-05-08     \n",
       "5 6            4                         957.60      2018-08-06     \n",
       "6 6            4                         294.74      2019-05-21     \n",
       "  payment_date time_to_process days_to_deliver acceptance_to_delivery\n",
       "1 2018-07-26   1               4               3                     \n",
       "2 2019-02-08   0               3               3                     \n",
       "3 2018-04-22   1               3               2                     \n",
       "4 2018-05-07   1               7               6                     \n",
       "5 2018-08-06   0               3               3                     \n",
       "6 2019-05-20   1               2               1                     "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "head(train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "5bbfb68c",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T21:08:03.078016Z",
     "iopub.status.busy": "2022-12-09T21:08:03.076758Z",
     "iopub.status.idle": "2022-12-09T21:08:03.258734Z",
     "shell.execute_reply": "2022-12-09T21:08:03.257321Z"
    },
    "papermill": {
     "duration": 0.192777,
     "end_time": "2022-12-09T21:08:03.261399",
     "exception": false,
     "start_time": "2022-12-09T21:08:03.068622",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "dev.new(width=5, height=4, unit=\"in\")\n",
    "plot(1:20)\n",
    "dev.new(width = 550, height = 330, unit = \"px\")\n",
    "plot(1:15)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "a8b7621d",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T21:08:03.277696Z",
     "iopub.status.busy": "2022-12-09T21:08:03.276392Z",
     "iopub.status.idle": "2022-12-09T21:08:03.305684Z",
     "shell.execute_reply": "2022-12-09T21:08:03.303721Z"
    },
    "papermill": {
     "duration": 0.040574,
     "end_time": "2022-12-09T21:08:03.308790",
     "exception": false,
     "start_time": "2022-12-09T21:08:03.268216",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "'data.frame':\t5704023 obs. of  20 variables:\n",
      " $ b2c_c2c                 : int  0 0 0 0 0 0 0 0 0 0 ...\n",
      " $ seller_id               : num  4677 104 340356 2101 12924 ...\n",
      " $ declared_handling_days  : int  1 1 1 1 1 0 1 1 1 0 ...\n",
      " $ shipment_method_id      : int  0 0 0 0 0 0 0 1 5 0 ...\n",
      " $ shipping_fee            : num  0 0 2.95 0 0 0 4 0 0 0 ...\n",
      " $ item_zip                : int  90703 91304 49735 51031 77035 32605 20743 77471 83642 92532 ...\n",
      " $ buyer_zip               : int  55070 60565 29379 28092 45373 33166 95122 55420 77488 12508 ...\n",
      " $ category_id             : int  1 11 1 13 8 11 0 5 1 8 ...\n",
      " $ item_price              : num  25 5.7 6 9.9 24 ...\n",
      " $ quantity                : int  1 1 1 1 1 2 1 1 1 1 ...\n",
      " $ delivery_date           : chr  \"2018-07-30\" \"2019-02-11\" \"2018-04-25\" \"2018-05-14\" ...\n",
      " $ weight                  : num  1.361 0 0.454 0.907 0.454 ...\n",
      " $ package_size            : int  6 6 6 6 6 6 6 5 6 6 ...\n",
      " $ carrier_average_estimate: num  4 4 4 4 4 4 4 3.5 3.5 4 ...\n",
      " $ zip_distance            : num  1528 1734 728 943 958 ...\n",
      " $ acceptance_date         : chr  \"2018-07-27\" \"2019-02-08\" \"2018-04-23\" \"2018-05-08\" ...\n",
      " $ payment_date            : chr  \"2018-07-26\" \"2019-02-08\" \"2018-04-22\" \"2018-05-07\" ...\n",
      " $ time_to_process         : int  1 0 1 1 0 1 2 1 2 1 ...\n",
      " $ days_to_deliver         : int  4 3 3 7 3 2 4 3 5 4 ...\n",
      " $ acceptance_to_delivery  : int  3 3 2 6 3 1 2 2 3 3 ...\n"
     ]
    }
   ],
   "source": [
    "str(train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "4629e79e",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T21:08:03.325267Z",
     "iopub.status.busy": "2022-12-09T21:08:03.323823Z",
     "iopub.status.idle": "2022-12-09T21:08:03.336311Z",
     "shell.execute_reply": "2022-12-09T21:08:03.334832Z"
    },
    "papermill": {
     "duration": 0.022488,
     "end_time": "2022-12-09T21:08:03.338076",
     "exception": false,
     "start_time": "2022-12-09T21:08:03.315588",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "\n",
    "#loss function\n",
    "evaluate_loss <- function(preds, actual) {\n",
    "    early_loss = 0\n",
    "    late_loss = 0\n",
    "    for (i in seq(1, length(preds))){\n",
    "        if (preds[i] < actual[i]){\n",
    "            #early shipment\n",
    "            early_loss = early_loss + (actual[i] - preds[i])\n",
    "        }\n",
    "        else if (preds[i] > actual[i]){\n",
    "        #late shipment\n",
    "            late_loss = late_loss + (preds[i] - actual[i])}\n",
    "    loss = (1/length(preds)) * ((0.4 * early_loss) + (0.6 * late_loss))\n",
    "    }\n",
    "    return(loss)\n",
    "}"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f5e956ca",
   "metadata": {
    "papermill": {
     "duration": 0.006403,
     "end_time": "2022-12-09T21:08:03.351107",
     "exception": false,
     "start_time": "2022-12-09T21:08:03.344704",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# Multiple Linear Regression"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "91ce9fcb",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T21:08:03.367879Z",
     "iopub.status.busy": "2022-12-09T21:08:03.366513Z",
     "iopub.status.idle": "2022-12-09T21:08:07.723935Z",
     "shell.execute_reply": "2022-12-09T21:08:07.721925Z"
    },
    "papermill": {
     "duration": 4.368277,
     "end_time": "2022-12-09T21:08:07.726119",
     "exception": false,
     "start_time": "2022-12-09T21:08:03.357842",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "linear_model = lm (days_to_deliver ~ b2c_c2c+ declared_handling_days + shipment_method_id+shipping_fee+item_zip\n",
    "                   +buyer_zip+category_id+item_price+quantity+ weight+package_size+carrier_average_estimate+zip_distance+time_to_process, data=train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "30cede73",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T21:08:07.747115Z",
     "iopub.status.busy": "2022-12-09T21:08:07.745516Z",
     "iopub.status.idle": "2022-12-09T21:08:11.426752Z",
     "shell.execute_reply": "2022-12-09T21:08:11.425401Z"
    },
    "papermill": {
     "duration": 3.693786,
     "end_time": "2022-12-09T21:08:11.428720",
     "exception": false,
     "start_time": "2022-12-09T21:08:07.734934",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\n",
       "Call:\n",
       "lm(formula = days_to_deliver ~ b2c_c2c + declared_handling_days + \n",
       "    shipment_method_id + shipping_fee + item_zip + buyer_zip + \n",
       "    category_id + item_price + quantity + weight + package_size + \n",
       "    carrier_average_estimate + zip_distance + time_to_process, \n",
       "    data = train)\n",
       "\n",
       "Residuals:\n",
       "    Min      1Q  Median      3Q     Max \n",
       "-92.316  -0.859  -0.273   0.465  76.050 \n",
       "\n",
       "Coefficients:\n",
       "                           Estimate Std. Error  t value Pr(>|t|)    \n",
       "(Intercept)               2.216e-01  7.936e-03   27.929  < 2e-16 ***\n",
       "b2c_c2c                  -7.593e-03  1.585e-03   -4.792 1.66e-06 ***\n",
       "declared_handling_days    5.180e-02  4.957e-04  104.497  < 2e-16 ***\n",
       "shipment_method_id        2.122e-02  4.220e-04   50.270  < 2e-16 ***\n",
       "shipping_fee             -4.749e-03  1.388e-04  -34.220  < 2e-16 ***\n",
       "item_zip                  4.180e-07  2.393e-08   17.467  < 2e-16 ***\n",
       "buyer_zip                -8.680e-07  2.462e-08  -35.255  < 2e-16 ***\n",
       "category_id               1.346e-02  1.050e-04  128.253  < 2e-16 ***\n",
       "item_price               -1.827e-04  6.573e-06  -27.795  < 2e-16 ***\n",
       "quantity                 -9.609e-03  7.052e-04  -13.626  < 2e-16 ***\n",
       "weight                    1.390e-04  1.919e-05    7.243 4.38e-13 ***\n",
       "package_size             -2.973e-02  9.121e-04  -32.590  < 2e-16 ***\n",
       "carrier_average_estimate  6.426e-01  1.309e-03  490.969  < 2e-16 ***\n",
       "zip_distance              3.226e-04  9.754e-07  330.713  < 2e-16 ***\n",
       "time_to_process           9.218e-01  2.653e-04 3475.105  < 2e-16 ***\n",
       "---\n",
       "Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1\n",
       "\n",
       "Residual standard error: 1.619 on 5704008 degrees of freedom\n",
       "Multiple R-squared:  0.7134,\tAdjusted R-squared:  0.7134 \n",
       "F-statistic: 1.014e+06 on 14 and 5704008 DF,  p-value: < 2.2e-16\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "summary(linear_model)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "ae02023a",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T21:08:11.451488Z",
     "iopub.status.busy": "2022-12-09T21:08:11.450254Z",
     "iopub.status.idle": "2022-12-09T21:08:11.817130Z",
     "shell.execute_reply": "2022-12-09T21:08:11.815174Z"
    },
    "papermill": {
     "duration": 0.384188,
     "end_time": "2022-12-09T21:08:11.819410",
     "exception": false,
     "start_time": "2022-12-09T21:08:11.435222",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "linear_model_preds =predict(linear_model, test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "295cc2fb",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T21:08:11.840732Z",
     "iopub.status.busy": "2022-12-09T21:08:11.839153Z",
     "iopub.status.idle": "2022-12-09T21:08:11.882488Z",
     "shell.execute_reply": "2022-12-09T21:08:11.879279Z"
    },
    "papermill": {
     "duration": 0.056526,
     "end_time": "2022-12-09T21:08:11.884937",
     "exception": false,
     "start_time": "2022-12-09T21:08:11.828411",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1] 1.619933\n"
     ]
    }
   ],
   "source": [
    "rmse_linear_model = rmse(test$days_to_deliver,linear_model_preds )\n",
    "print(rmse_linear_model)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "1e3977ae",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T21:08:11.906934Z",
     "iopub.status.busy": "2022-12-09T21:08:11.905391Z",
     "iopub.status.idle": "2022-12-09T21:08:19.939561Z",
     "shell.execute_reply": "2022-12-09T21:08:19.938110Z"
    },
    "papermill": {
     "duration": 8.046816,
     "end_time": "2022-12-09T21:08:19.941656",
     "exception": false,
     "start_time": "2022-12-09T21:08:11.894840",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<strong>2:</strong> 0.489647467797008"
      ],
      "text/latex": [
       "\\textbf{2:} 0.489647467797008"
      ],
      "text/markdown": [
       "**2:** 0.489647467797008"
      ],
      "text/plain": [
       "        2 \n",
       "0.4896475 "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "evaluate_loss(round(linear_model_preds,0), test$days_to_deliver)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f3e5ed63",
   "metadata": {
    "papermill": {
     "duration": 0.007255,
     "end_time": "2022-12-09T21:08:19.955994",
     "exception": false,
     "start_time": "2022-12-09T21:08:19.948739",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# XG boost model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "86fa3907",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T21:08:19.972886Z",
     "iopub.status.busy": "2022-12-09T21:08:19.971656Z",
     "iopub.status.idle": "2022-12-09T21:08:23.293834Z",
     "shell.execute_reply": "2022-12-09T21:08:23.292311Z"
    },
    "papermill": {
     "duration": 3.332739,
     "end_time": "2022-12-09T21:08:23.295707",
     "exception": false,
     "start_time": "2022-12-09T21:08:19.962968",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "\n",
    "#define predictor and response variables in training set\n",
    "train_x = data.matrix(train[, c(-11,-16,-17,-19,-20)])\n",
    "train_y = train[,19]\n",
    "\n",
    "#define predictor and response variables in testing set\n",
    "test_x = data.matrix(test[, c(-11,-16,-17,-19,-20)])\n",
    "test_y = test[, 19]\n",
    "\n",
    "#define final training and testing sets\n",
    "xgb_train = xgb.DMatrix(data = train_x, label = train_y)\n",
    "xgb_test = xgb.DMatrix(data = test_x, label = test_y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "b16268f9",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T21:08:23.312437Z",
     "iopub.status.busy": "2022-12-09T21:08:23.311111Z",
     "iopub.status.idle": "2022-12-09T21:08:44.841256Z",
     "shell.execute_reply": "2022-12-09T21:08:44.838644Z"
    },
    "papermill": {
     "duration": 21.54119,
     "end_time": "2022-12-09T21:08:44.843791",
     "exception": false,
     "start_time": "2022-12-09T21:08:23.302601",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1]\ttrain-rmse:4.713490\ttest-rmse:4.713030 \n",
      "[2]\ttrain-rmse:4.304879\ttest-rmse:4.304422 \n",
      "[3]\ttrain-rmse:3.942361\ttest-rmse:3.941937 \n",
      "[4]\ttrain-rmse:3.621455\ttest-rmse:3.620966 \n",
      "[5]\ttrain-rmse:3.338526\ttest-rmse:3.338420 \n",
      "[6]\ttrain-rmse:3.090012\ttest-rmse:3.090187 \n",
      "[7]\ttrain-rmse:2.872045\ttest-rmse:2.872339 \n",
      "[8]\ttrain-rmse:2.680177\ttest-rmse:2.680805 \n",
      "[9]\ttrain-rmse:2.514930\ttest-rmse:2.515797 \n",
      "[10]\ttrain-rmse:2.372085\ttest-rmse:2.373371 \n",
      "[11]\ttrain-rmse:2.247403\ttest-rmse:2.249023 \n",
      "[12]\ttrain-rmse:2.140560\ttest-rmse:2.142447 \n",
      "[13]\ttrain-rmse:2.049502\ttest-rmse:2.051759 \n",
      "[14]\ttrain-rmse:1.972329\ttest-rmse:1.974896 \n",
      "[15]\ttrain-rmse:1.906533\ttest-rmse:1.909567 \n",
      "[16]\ttrain-rmse:1.851778\ttest-rmse:1.855119 \n",
      "[17]\ttrain-rmse:1.805056\ttest-rmse:1.808729 \n",
      "[18]\ttrain-rmse:1.765789\ttest-rmse:1.769625 \n",
      "[19]\ttrain-rmse:1.732547\ttest-rmse:1.736687 \n",
      "[20]\ttrain-rmse:1.704226\ttest-rmse:1.708567 \n"
     ]
    }
   ],
   "source": [
    "#define watchlist\n",
    "watchlist = list(train=xgb_train, test=xgb_test)\n",
    "\n",
    "#fit XGBoost model and display training and testing data at each round\n",
    "Xgb_model = xgb.train(data = xgb_train, max.depth = 4, watchlist=watchlist, nrounds = 20, eta=0.1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "197c974a",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T21:08:44.860830Z",
     "iopub.status.busy": "2022-12-09T21:08:44.859553Z",
     "iopub.status.idle": "2022-12-09T21:08:45.891386Z",
     "shell.execute_reply": "2022-12-09T21:08:45.889700Z"
    },
    "papermill": {
     "duration": 1.042596,
     "end_time": "2022-12-09T21:08:45.893719",
     "exception": false,
     "start_time": "2022-12-09T21:08:44.851123",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "xgb_model_preds <- predict(Xgb_model, test_x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "ba059e7c",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T21:08:45.909974Z",
     "iopub.status.busy": "2022-12-09T21:08:45.908724Z",
     "iopub.status.idle": "2022-12-09T21:08:47.042901Z",
     "shell.execute_reply": "2022-12-09T21:08:47.040866Z"
    },
    "papermill": {
     "duration": 1.145113,
     "end_time": "2022-12-09T21:08:47.045771",
     "exception": false,
     "start_time": "2022-12-09T21:08:45.900658",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "0.437096324876635"
      ],
      "text/latex": [
       "0.437096324876635"
      ],
      "text/markdown": [
       "0.437096324876635"
      ],
      "text/plain": [
       "[1] 0.4370963"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "evaluate_loss(round(xgb_model_preds,0), test$days_to_deliver)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "074dbcf3",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T21:08:47.065741Z",
     "iopub.status.busy": "2022-12-09T21:08:47.064390Z",
     "iopub.status.idle": "2022-12-09T21:08:47.104777Z",
     "shell.execute_reply": "2022-12-09T21:08:47.103344Z"
    },
    "papermill": {
     "duration": 0.053846,
     "end_time": "2022-12-09T21:08:47.106911",
     "exception": false,
     "start_time": "2022-12-09T21:08:47.053065",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<table class=\"dataframe\">\n",
       "<caption>A data.table: 9 × 4</caption>\n",
       "<thead>\n",
       "\t<tr><th scope=col>Feature</th><th scope=col>Gain</th><th scope=col>Cover</th><th scope=col>Frequency</th></tr>\n",
       "\t<tr><th scope=col>&lt;chr&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th></tr>\n",
       "</thead>\n",
       "<tbody>\n",
       "\t<tr><td>time_to_process         </td><td>9.548387e-01</td><td>7.072311e-01</td><td>0.616666667</td></tr>\n",
       "\t<tr><td>carrier_average_estimate</td><td>2.340397e-02</td><td>1.328038e-01</td><td>0.110000000</td></tr>\n",
       "\t<tr><td>zip_distance            </td><td>1.424457e-02</td><td>1.238736e-01</td><td>0.133333333</td></tr>\n",
       "\t<tr><td>seller_id               </td><td>4.792382e-03</td><td>1.745907e-02</td><td>0.080000000</td></tr>\n",
       "\t<tr><td>shipment_method_id      </td><td>1.675396e-03</td><td>1.795486e-02</td><td>0.010000000</td></tr>\n",
       "\t<tr><td>declared_handling_days  </td><td>7.399077e-04</td><td>4.612030e-04</td><td>0.036666667</td></tr>\n",
       "\t<tr><td>item_zip                </td><td>1.566837e-04</td><td>6.683879e-07</td><td>0.003333333</td></tr>\n",
       "\t<tr><td>package_size            </td><td>7.848858e-05</td><td>2.131741e-04</td><td>0.006666667</td></tr>\n",
       "\t<tr><td>item_price              </td><td>6.995132e-05</td><td>2.559597e-06</td><td>0.003333333</td></tr>\n",
       "</tbody>\n",
       "</table>\n"
      ],
      "text/latex": [
       "A data.table: 9 × 4\n",
       "\\begin{tabular}{llll}\n",
       " Feature & Gain & Cover & Frequency\\\\\n",
       " <chr> & <dbl> & <dbl> & <dbl>\\\\\n",
       "\\hline\n",
       "\t time\\_to\\_process          & 9.548387e-01 & 7.072311e-01 & 0.616666667\\\\\n",
       "\t carrier\\_average\\_estimate & 2.340397e-02 & 1.328038e-01 & 0.110000000\\\\\n",
       "\t zip\\_distance             & 1.424457e-02 & 1.238736e-01 & 0.133333333\\\\\n",
       "\t seller\\_id                & 4.792382e-03 & 1.745907e-02 & 0.080000000\\\\\n",
       "\t shipment\\_method\\_id       & 1.675396e-03 & 1.795486e-02 & 0.010000000\\\\\n",
       "\t declared\\_handling\\_days   & 7.399077e-04 & 4.612030e-04 & 0.036666667\\\\\n",
       "\t item\\_zip                 & 1.566837e-04 & 6.683879e-07 & 0.003333333\\\\\n",
       "\t package\\_size             & 7.848858e-05 & 2.131741e-04 & 0.006666667\\\\\n",
       "\t item\\_price               & 6.995132e-05 & 2.559597e-06 & 0.003333333\\\\\n",
       "\\end{tabular}\n"
      ],
      "text/markdown": [
       "\n",
       "A data.table: 9 × 4\n",
       "\n",
       "| Feature &lt;chr&gt; | Gain &lt;dbl&gt; | Cover &lt;dbl&gt; | Frequency &lt;dbl&gt; |\n",
       "|---|---|---|---|\n",
       "| time_to_process          | 9.548387e-01 | 7.072311e-01 | 0.616666667 |\n",
       "| carrier_average_estimate | 2.340397e-02 | 1.328038e-01 | 0.110000000 |\n",
       "| zip_distance             | 1.424457e-02 | 1.238736e-01 | 0.133333333 |\n",
       "| seller_id                | 4.792382e-03 | 1.745907e-02 | 0.080000000 |\n",
       "| shipment_method_id       | 1.675396e-03 | 1.795486e-02 | 0.010000000 |\n",
       "| declared_handling_days   | 7.399077e-04 | 4.612030e-04 | 0.036666667 |\n",
       "| item_zip                 | 1.566837e-04 | 6.683879e-07 | 0.003333333 |\n",
       "| package_size             | 7.848858e-05 | 2.131741e-04 | 0.006666667 |\n",
       "| item_price               | 6.995132e-05 | 2.559597e-06 | 0.003333333 |\n",
       "\n"
      ],
      "text/plain": [
       "  Feature                  Gain         Cover        Frequency  \n",
       "1 time_to_process          9.548387e-01 7.072311e-01 0.616666667\n",
       "2 carrier_average_estimate 2.340397e-02 1.328038e-01 0.110000000\n",
       "3 zip_distance             1.424457e-02 1.238736e-01 0.133333333\n",
       "4 seller_id                4.792382e-03 1.745907e-02 0.080000000\n",
       "5 shipment_method_id       1.675396e-03 1.795486e-02 0.010000000\n",
       "6 declared_handling_days   7.399077e-04 4.612030e-04 0.036666667\n",
       "7 item_zip                 1.566837e-04 6.683879e-07 0.003333333\n",
       "8 package_size             7.848858e-05 2.131741e-04 0.006666667\n",
       "9 item_price               6.995132e-05 2.559597e-06 0.003333333"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "importance_matrix = xgb.importance(colnames(xgb_train), model = Xgb_model)\n",
    "importance_matrix"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "5fa65de6",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T21:08:47.124576Z",
     "iopub.status.busy": "2022-12-09T21:08:47.123307Z",
     "iopub.status.idle": "2022-12-09T21:08:47.133077Z",
     "shell.execute_reply": "2022-12-09T21:08:47.131605Z"
    },
    "papermill": {
     "duration": 0.020402,
     "end_time": "2022-12-09T21:08:47.134873",
     "exception": false,
     "start_time": "2022-12-09T21:08:47.114471",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "# write.csv(importance_matrix,\"/kaggle/working/xgb_importance.csv\", row.names = TRUE)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "3a9680a0",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T21:08:47.152409Z",
     "iopub.status.busy": "2022-12-09T21:08:47.151006Z",
     "iopub.status.idle": "2022-12-09T21:08:47.282407Z",
     "shell.execute_reply": "2022-12-09T21:08:47.280999Z"
    },
    "papermill": {
     "duration": 0.142599,
     "end_time": "2022-12-09T21:08:47.284722",
     "exception": false,
     "start_time": "2022-12-09T21:08:47.142123",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\nplKpQdWLOmTwLi3BVtPF+x/XqyRdXNXivHRAaQghV+9bKJJstb7uNyGEisOrW5wP/MTAEMLb\nz72bp1HZO2FHQZo6bmBTwztzX35v50m2ofaOdZvLqyac1LukvS7pbhKs6Lk5Z3z1f9Yfe+28\n5T+97YheXvhsRVu3WnH4Jyfv7qKJh4YQKo85d/LkyRecNbjjRu/CEtyr04+t2rbxv5bW7fa1\nYivu/X0I4eiP7ZfXaQtFW7daWjEmhPDei4+0OF/34GshhMGjvXLfSTr781Ygic1rvpFKpQaM\nvnHrnz4gPffErWNDCOO++sEnpGcbN69du/aVdes//CXdXNu32viXvUuKe45412eD7VmCe7WF\nDasuCj7HbncJtrrhhS+FEAaffuNrO36swiu//Le+RenSijF+rmCzBFudPqxfCOGKbz6+8zes\nXzrvI2VFRWUH/25rY47OIOwoVD+acnQIYdBJE2+85Zarzz85lUr1+4vJu376aN1rXw4hlPQ6\n7sNfQpu2unXDwhBCUdkhp7Rmxm83dt7fo2tJcK/uSti1KsFWH7h8ZAihx8ARf33hZeeMP6E4\nlcoUV9311NudMX4X1datvv/awuG9S0IIQ0aPu3DyZWeNP6E4nUpnevzjgy930t8AYUcBa3zo\nrutPGHpgj+KSygMO+/Tn7tj5RLxZa/+z/DOX0KatvveHaXt5N+Csp/xs9Z0S3KsfEHZ70Pat\nZhse+sr0McMP6lVaVFE5aPzfTPnZyndb/lu7uzZvdVvts7OnnD98yIDSoqKKysGnTrjywae1\ncmdK5XK+aBQAIAa+eQIAIBLCDgAgEsIOACASwg4AIBLCDgAgEsIOACASwg4AIBLCDgAgEsIO\nACASwg4AIBLCDgAgEsIOACASwg4AIBLCDgAgEsIOACASwg4AIBLCDgAgEsIOACASwg4AIBLC\nDgAgEsIOACASwg4AIBLCDgAgEsIOACASwg4AIBLCDgAgEsIOACASwg4AIBLCDgAgEsIOACAS\nwg4AIBLCDgAgEsIOACASwg4AIBLCDgAgEsIOACASwg4AIBLCDgAgEsIOACASwg4AIBLCDgAg\nEsIOACASwg4AIBLCDgAgEsIOACASwg4AIBLCDgAgEsIOACASwg4AIBLCDgAgEsIOACASwg4A\nIBLCDgAgEsIOACASwg4AIBLCDgAgEsIOACASwg4AIBLCDgAgEsIOACASwg4AIBLCDgAgEsIO\nACASwg4AIBLCDgAgEsIOACASwg4AIBLCDgAgEsIOACASwg4AIBLCDgAgEsIOACASwg4AIBLC\nDgAgEsIOACASwg4AIBL/D/9QBPgmrbfYAAAAAElFTkSuQmCC"
     },
     "metadata": {
      "image/png": {
       "height": 420,
       "width": 420
      }
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "xgb.plot.importance(importance_matrix[1:6,])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9748a5f3",
   "metadata": {
    "papermill": {
     "duration": 0.007725,
     "end_time": "2022-12-09T21:08:47.300207",
     "exception": false,
     "start_time": "2022-12-09T21:08:47.292482",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# Decision Tree\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "af7f4f58",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T21:08:47.318188Z",
     "iopub.status.busy": "2022-12-09T21:08:47.316842Z",
     "iopub.status.idle": "2022-12-09T21:17:56.174721Z",
     "shell.execute_reply": "2022-12-09T21:17:56.173164Z"
    },
    "papermill": {
     "duration": 548.868672,
     "end_time": "2022-12-09T21:17:56.176517",
     "exception": false,
     "start_time": "2022-12-09T21:08:47.307845",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Create decision tree using regression\n",
    "dt_model <- rpart(days_to_deliver ~ b2c_c2c+ declared_handling_days + shipment_method_id+shipping_fee+item_zip\n",
    "            +buyer_zip+category_id+item_price+quantity+ weight+package_size+carrier_average_estimate+zip_distance+time_to_process, data = train)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "de6f568a",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T21:17:56.220895Z",
     "iopub.status.busy": "2022-12-09T21:17:56.219676Z",
     "iopub.status.idle": "2022-12-09T21:18:11.353895Z",
     "shell.execute_reply": "2022-12-09T21:18:11.352427Z"
    },
    "papermill": {
     "duration": 15.171837,
     "end_time": "2022-12-09T21:18:11.355956",
     "exception": false,
     "start_time": "2022-12-09T21:17:56.184119",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n+oyY0KB5m0K7bhj7+52LJ/939YyAx9u6devs2bMrPtSySE5Otre3v3LlirahSetB45r2GKSk\nVqVgNU5Whq/HzRdXXaLYXzt16nTu3DkDA4OKj7Yszp07N3nKlIyMzKY9BrXsN8qoVoNCq4V/\n9X3ldubDAzdVVZXjx44NHTq0guMso4iICFtb26dPn+qa127U165mu14shUJO7mSlJn95dM33\nlmtyTLitra2zs7O6unrFRytGlSyx8/DwGDVqVExMzH+z565yXKta2AnkgjIzM7dt2bR543oN\nDY1Tp05J/zEyKSnJ3t7+6tWrdevWO+l6tlGjxiIu+PLF8wl2Y4KD2ePGjXNycpL+cwNnz551\ncHDIzMpauHzthCkzWKLdW5aSnLRx9dILridMTU0vXrz4tysm0iM8PNzW1vbZs2dWLdps3ONs\nZGwq4oKP799eNX9aUmLC0qVL165dK1dYeiRt3N3dR4wYweFwZy5ZN8xuSrH1Y6IiVs6e4Of9\nulOnTrdv31ZWVq6AIMsuOTm5Z8+eL1++bNSi7YIthzR1irkBVCAQXDvpdHrvJmUV5atXrnTv\n3r1i4iw7JyenWbNmKSqrzFq7q0234neeId+/bJk3KSz4++jRo0+dOlVZTquHhoZ26dr1e0BA\no859B87boKBczM6Tx+XcPbz5xbVTBoaG/7t3r2HDhhUTZ9ktXrx469atVXT1bVfsNmtgXWx9\nts+rixvmpsTHLl++fP369RUQoVi8f/++Z0+bnz9jG/cb13rsPKZcMT8as9NTPQ6sCHzxv9p1\n6ng8fGhkZFQxcZaHypTYHTt2zMHBQVVV9cjREwMGDS7p4vf/d2/CuDHxcXE7duyYO3dueUQo\nFtHR0R06dPj27dvwESMPHDxS0hvMExMSJk6wu33rZpMmTR4/fqyhoVFOcZbdqlWr1q1bZ2Bo\ntO+oa7MWJb5wc+W866pFs3k87pkzZ6T5p+Tnz587d+4cGxs7bsqs2Usc5Up4UioyPHThNDvf\n929tbGzc3d2l/JzW169fmzdvLq+ovOXQmfqNiz9mCHG5nN3rl149c2zChAnHjx8v1wjFZfjw\n4ZcuXRo0fvq4OcuZTFET7o9vX2yaa8+SY3i/e2dubl6eAYrH48ePu3fvbmBisWKfi5GppYhL\nZaSl7lw289Wju+vWrVuxYkW5RigW2dnZHTt2fPXqVZ8ZK1oNtBN9Qb8nt69sXmhmZvru7Vtp\n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\nEl3eyM7T1taWkJAICQm5fSvOympCx2qylJSP0yf/lpqa4u/vb2Nj0/YLfjkSiWRtbR0UFHTl\n0gU1dc3effu3/ZpmWEzmnu2bjvrtMTY2PnfuHPd+ZYKmf//++fn5ERfD3r99Ncp8vKgY77VA\nW/f6eaKni11ZaUlERET//h35t/o1evXqVVpaGnEpjFFHHzbS7IdeW5CX4+Uyg0ImxcXFKSsr\n/5wGdg0REREzM7PAwICnd2PNJtmKif/YJ8nxnRsSbl9fv369m5vbT2phVzE1NX3x4sWNq5cV\nlFX1ew/4odemf0zeuXIBVVMzJiZGMD9sG0hLSw8cOPB0YMDXN88GWU0nkn7gk4TDYZ/btjzr\n45tjx46NH9/2bYH4y9LSMjo6+vHNKz16DVLQ6PFDr/34JP6q32bjYcNCQkIE88O2gZqamrKy\ncvi54JKsNIORNvAj1QKzrvbq1kXVxXmRkRF9+/b9eY38qbpNYUehUGxsbO7cuXMuNOTF82fj\nJ1iLi7d4p6nmKioqXOfP+3fvP3p6elFRUT16/Njf9K9kamrKZDIvnD8fHHSmX7/+evr6P/Ty\nS+FhM6ZOys3N2blzp2Ces+OSkZExNzePiooKPxeUm5M92tzyhz4sCvLz3ObaRoafMzU1vXTp\nksDO4AEAKyurjIyMyMsXb0ZdHmRsqqz6Y/dHDz55eM2yBWwmIzAwcMqUKT+pkV3F0tIyLi4u\nOjK8pKhg2EgzUvu+I98lPV+5YGZRQV5ISAh3sW4Bp6KioqWlFRx09sntmD5DTOWV2nUCjl5X\ne3DLqpsXgy0tLU+ePCmAEyWbIBAI1tbWF8LC4q5eJJJIvQebtPMX9dO7sTu857OYjOjo6JbW\ndBQoenp6HA7n6qWwT88f6g8ZKSbVrknJ1WUloZs9U5/ec3V1FfDxVy4ymWxlZXXq9OkXsZEy\nSmrq+u2djPQs+vzl3WtlZWXj4uIUFRV/aiO7xNChQ9PS0u7GROZ/Tu4xeDSZ0q5f1OV5mVG+\n7gXp7319fefNm/ezG/nzdJvCDgDk5eWdnZ2zs7PDwi6Eh12QlZMzMurZZjVAp9Mvhl2YP8/x\nwf17dnZ2UVFRVKpA31+cQCBYWFgMHTr08uXLpwMDCgsK9A0MFBTafi8lJ7/1Wb/2T58NCgoK\nV65cmTNnzi9obWdoaGjMmzcvKSkp8lL47RsxSkoqujT9Nr/tqqsqw0LPeC2al/LhnZeXV3Bw\n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\nD+NK/A4QbOuoAAAAAElFTkSuQmCC"
     },
     "metadata": {
      "image/png": {
       "height": 420,
       "width": 420
      }
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "rpart.plot(dt_model)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "2a78ff9a",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T21:18:11.376843Z",
     "iopub.status.busy": "2022-12-09T21:18:11.375556Z",
     "iopub.status.idle": "2022-12-09T21:18:12.589316Z",
     "shell.execute_reply": "2022-12-09T21:18:12.587798Z"
    },
    "papermill": {
     "duration": 1.226345,
     "end_time": "2022-12-09T21:18:12.591148",
     "exception": false,
     "start_time": "2022-12-09T21:18:11.364803",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "dt_preds= predict(dt_model,test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "4bfee5bd",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T21:18:12.610563Z",
     "iopub.status.busy": "2022-12-09T21:18:12.609333Z",
     "iopub.status.idle": "2022-12-09T21:18:12.641813Z",
     "shell.execute_reply": "2022-12-09T21:18:12.640443Z"
    },
    "papermill": {
     "duration": 0.044223,
     "end_time": "2022-12-09T21:18:12.643792",
     "exception": false,
     "start_time": "2022-12-09T21:18:12.599569",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1] 1.730644\n"
     ]
    }
   ],
   "source": [
    "rmse_decision_tree = rmse(test$days_to_deliver,dt_preds)\n",
    "print(rmse_decision_tree)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "16758217",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T21:18:12.664356Z",
     "iopub.status.busy": "2022-12-09T21:18:12.663010Z",
     "iopub.status.idle": "2022-12-09T21:18:20.146707Z",
     "shell.execute_reply": "2022-12-09T21:18:20.145326Z"
    },
    "papermill": {
     "duration": 7.49584,
     "end_time": "2022-12-09T21:18:20.148533",
     "exception": false,
     "start_time": "2022-12-09T21:18:12.652693",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<strong>2:</strong> 0.507024013620386"
      ],
      "text/latex": [
       "\\textbf{2:} 0.507024013620386"
      ],
      "text/markdown": [
       "**2:** 0.507024013620386"
      ],
      "text/plain": [
       "       2 \n",
       "0.507024 "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "evaluate_loss(round(dt_preds,0), test$days_to_deliver)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "81e27c77",
   "metadata": {
    "papermill": {
     "duration": 0.008624,
     "end_time": "2022-12-09T21:18:20.165855",
     "exception": false,
     "start_time": "2022-12-09T21:18:20.157231",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# Ridge Regression"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "84084fae",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T21:18:20.186348Z",
     "iopub.status.busy": "2022-12-09T21:18:20.184994Z",
     "iopub.status.idle": "2022-12-09T21:19:43.209156Z",
     "shell.execute_reply": "2022-12-09T21:19:43.207750Z"
    },
    "papermill": {
     "duration": 83.048087,
     "end_time": "2022-12-09T21:19:43.222723",
     "exception": false,
     "start_time": "2022-12-09T21:18:20.174636",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "0.251379050517826"
      ],
      "text/latex": [
       "0.251379050517826"
      ],
      "text/markdown": [
       "0.251379050517826"
      ],
      "text/plain": [
       "[1] 0.2513791"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#perform k-fold cross-validation to find optimal lambda value\n",
    "cv_model <- cv.glmnet(train_x, train_y, alpha = 0)\n",
    "\n",
    "#find optimal lambda value that minimizes test MSE\n",
    "best_lambda <- cv_model$lambda.min\n",
    "best_lambda"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "7e3f07ee",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T21:19:43.243386Z",
     "iopub.status.busy": "2022-12-09T21:19:43.242057Z",
     "iopub.status.idle": "2022-12-09T21:19:44.554381Z",
     "shell.execute_reply": "2022-12-09T21:19:44.552763Z"
    },
    "papermill": {
     "duration": 1.324636,
     "end_time": "2022-12-09T21:19:44.556236",
     "exception": false,
     "start_time": "2022-12-09T21:19:43.231600",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "#ridge model\n",
    "ridge_reg = glmnet(train_x, train_y, nlambda = 25, alpha = 0, family = 'gaussian', lambda = best_lambda)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "3d726973",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T21:19:44.578601Z",
     "iopub.status.busy": "2022-12-09T21:19:44.577250Z",
     "iopub.status.idle": "2022-12-09T21:19:44.761437Z",
     "shell.execute_reply": "2022-12-09T21:19:44.759875Z"
    },
    "papermill": {
     "duration": 0.19761,
     "end_time": "2022-12-09T21:19:44.763311",
     "exception": false,
     "start_time": "2022-12-09T21:19:44.565701",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "# rr_model_preds <-predict(ridge_reg, test_x)\n",
    "rr_model_preds <-predict(ridge_reg, test_x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "1e125f72",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T21:19:44.785317Z",
     "iopub.status.busy": "2022-12-09T21:19:44.783935Z",
     "iopub.status.idle": "2022-12-09T21:19:44.812694Z",
     "shell.execute_reply": "2022-12-09T21:19:44.811246Z"
    },
    "papermill": {
     "duration": 0.041908,
     "end_time": "2022-12-09T21:19:44.814492",
     "exception": false,
     "start_time": "2022-12-09T21:19:44.772584",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1] 1.631548\n"
     ]
    }
   ],
   "source": [
    "rmse_ridge = rmse(test$days_to_deliver,rr_model_preds)\n",
    "print(rmse_ridge)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "5cc234c4",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T21:19:44.835998Z",
     "iopub.status.busy": "2022-12-09T21:19:44.834760Z",
     "iopub.status.idle": "2022-12-09T21:19:47.191730Z",
     "shell.execute_reply": "2022-12-09T21:19:47.190352Z"
    },
    "papermill": {
     "duration": 2.369769,
     "end_time": "2022-12-09T21:19:47.193560",
     "exception": false,
     "start_time": "2022-12-09T21:19:44.823791",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "0.498206597394799"
      ],
      "text/latex": [
       "0.498206597394799"
      ],
      "text/markdown": [
       "0.498206597394799"
      ],
      "text/plain": [
       "[1] 0.4982066"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "evaluate_loss(round(rr_model_preds,0), test$days_to_deliver)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "R",
   "language": "R",
   "name": "ir"
  },
  "language_info": {
   "codemirror_mode": "r",
   "file_extension": ".r",
   "mimetype": "text/x-r-source",
   "name": "R",
   "pygments_lexer": "r",
   "version": "4.0.5"
  },
  "papermill": {
   "default_parameters": {},
   "duration": 796.891878,
   "end_time": "2022-12-09T21:19:48.527348",
   "environment_variables": {},
   "exception": null,
   "input_path": "__notebook__.ipynb",
   "output_path": "__notebook__.ipynb",
   "parameters": {},
   "start_time": "2022-12-09T21:06:31.635470",
   "version": "2.4.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
