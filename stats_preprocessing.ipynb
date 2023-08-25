{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "dd437b43",
   "metadata": {
    "_execution_state": "idle",
    "_uuid": "051d70d956493feee0c6d64651c6a088724dca2a",
    "execution": {
     "iopub.execute_input": "2022-12-09T22:12:58.662120Z",
     "iopub.status.busy": "2022-12-09T22:12:58.660288Z",
     "iopub.status.idle": "2022-12-09T22:13:34.385446Z",
     "shell.execute_reply": "2022-12-09T22:13:34.383926Z"
    },
    "papermill": {
     "duration": 35.739693,
     "end_time": "2022-12-09T22:13:34.389326",
     "exception": false,
     "start_time": "2022-12-09T22:12:58.649633",
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
      "Installing package into ‘/usr/local/lib/R/site-library’\n",
      "(as ‘lib’ is unspecified)\n",
      "\n",
      "\n",
      "Attaching package: ‘MASS’\n",
      "\n",
      "\n",
      "The following object is masked from ‘package:dplyr’:\n",
      "\n",
      "    select\n",
      "\n",
      "\n"
     ]
    }
   ],
   "source": [
    "\n",
    "library(tidyverse) # metapackage of all tidyverse packages\n",
    "library(ggplot2)\n",
    "library(dplyr)\n",
    "install.packages(\"zipcodeR\")\n",
    "library(zipcodeR)\n",
    "# list.files(path = \"../input\")\n",
    "library(MASS)\n",
    "library(caTools)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "69e0ca9e",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T22:13:34.431435Z",
     "iopub.status.busy": "2022-12-09T22:13:34.406690Z",
     "iopub.status.idle": "2022-12-09T22:17:45.575730Z",
     "shell.execute_reply": "2022-12-09T22:17:45.574076Z"
    },
    "papermill": {
     "duration": 251.180582,
     "end_time": "2022-12-09T22:17:45.577848",
     "exception": false,
     "start_time": "2022-12-09T22:13:34.397266",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "df <- read.csv(file='../input/ebay-delivery-date-prediction/eBay Delivery date prediction.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "4c71054d",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T22:17:45.600043Z",
     "iopub.status.busy": "2022-12-09T22:17:45.598645Z",
     "iopub.status.idle": "2022-12-09T22:17:45.628223Z",
     "shell.execute_reply": "2022-12-09T22:17:45.626906Z"
    },
    "papermill": {
     "duration": 0.042613,
     "end_time": "2022-12-09T22:17:45.630420",
     "exception": false,
     "start_time": "2022-12-09T22:17:45.587807",
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
       "\t<tr><th></th><th scope=col>X</th><th scope=col>b2c_c2c</th><th scope=col>seller_id</th><th scope=col>declared_handling_days</th><th scope=col>acceptance_scan_timestamp</th><th scope=col>shipment_method_id</th><th scope=col>shipping_fee</th><th scope=col>carrier_min_estimate</th><th scope=col>carrier_max_estimate</th><th scope=col>item_zip</th><th scope=col>buyer_zip</th><th scope=col>category_id</th><th scope=col>item_price</th><th scope=col>quantity</th><th scope=col>payment_datetime</th><th scope=col>delivery_date</th><th scope=col>weight</th><th scope=col>weight_units</th><th scope=col>package_size</th><th scope=col>record_number</th></tr>\n",
       "\t<tr><th></th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;chr&gt;</th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;chr&gt;</th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;chr&gt;</th><th scope=col>&lt;chr&gt;</th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;chr&gt;</th><th scope=col>&lt;chr&gt;</th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;chr&gt;</th><th scope=col>&lt;int&gt;</th></tr>\n",
       "</thead>\n",
       "<tbody>\n",
       "\t<tr><th scope=row>1</th><td>0</td><td>B2C</td><td>  25454</td><td>3</td><td>2019-03-26 15:11:00.000-07:00</td><td>0</td><td>0.0</td><td>3</td><td>5</td><td>97219     </td><td>49040</td><td>13</td><td>27.95</td><td>1</td><td>2019-03-24 03:56:49.000-07:00</td><td>2019-03-29</td><td>5</td><td>1</td><td>LETTER                </td><td>1</td></tr>\n",
       "\t<tr><th scope=row>2</th><td>1</td><td>C2C</td><td>6727381</td><td>2</td><td>2018-06-02 12:53:00.000-07:00</td><td>0</td><td>3.0</td><td>3</td><td>5</td><td>11415-3528</td><td>62521</td><td> 0</td><td>20.50</td><td>1</td><td>2018-06-01 13:43:54.000-07:00</td><td>2018-06-05</td><td>0</td><td>1</td><td>PACKAGE_THICK_ENVELOPE</td><td>2</td></tr>\n",
       "\t<tr><th scope=row>3</th><td>2</td><td>B2C</td><td>  18507</td><td>1</td><td>2019-01-07 16:22:00.000-05:00</td><td>0</td><td>4.5</td><td>3</td><td>5</td><td>27292     </td><td>53010</td><td> 1</td><td>19.90</td><td>1</td><td>2019-01-06 00:02:00.000-05:00</td><td>2019-01-10</td><td>9</td><td>1</td><td>PACKAGE_THICK_ENVELOPE</td><td>3</td></tr>\n",
       "\t<tr><th scope=row>4</th><td>3</td><td>B2C</td><td>   4677</td><td>1</td><td>2018-12-17 16:56:00.000-08:00</td><td>0</td><td>0.0</td><td>3</td><td>5</td><td>90703     </td><td>80022</td><td> 1</td><td>35.50</td><td>1</td><td>2018-12-16 10:28:28.000-08:00</td><td>2018-12-21</td><td>8</td><td>1</td><td>PACKAGE_THICK_ENVELOPE</td><td>4</td></tr>\n",
       "\t<tr><th scope=row>5</th><td>4</td><td>B2C</td><td>   4677</td><td>1</td><td>2018-07-27 16:48:00.000-07:00</td><td>0</td><td>0.0</td><td>3</td><td>5</td><td>90703     </td><td>55070</td><td> 1</td><td>25.00</td><td>1</td><td>2018-07-26 18:20:02.000-07:00</td><td>2018-07-30</td><td>3</td><td>1</td><td>PACKAGE_THICK_ENVELOPE</td><td>5</td></tr>\n",
       "\t<tr><th scope=row>6</th><td>5</td><td>B2C</td><td>  10514</td><td>1</td><td>2019-04-19 19:42:00.000-04:00</td><td>0</td><td>0.0</td><td>3</td><td>5</td><td>43215     </td><td>77063</td><td> 3</td><td>10.39</td><td>1</td><td>2019-04-18 14:11:09.000-04:00</td><td>2019-04-22</td><td>1</td><td>1</td><td>PACKAGE_THICK_ENVELOPE</td><td>6</td></tr>\n",
       "</tbody>\n",
       "</table>\n"
      ],
      "text/latex": [
       "A data.frame: 6 × 20\n",
       "\\begin{tabular}{r|llllllllllllllllllll}\n",
       "  & X & b2c\\_c2c & seller\\_id & declared\\_handling\\_days & acceptance\\_scan\\_timestamp & shipment\\_method\\_id & shipping\\_fee & carrier\\_min\\_estimate & carrier\\_max\\_estimate & item\\_zip & buyer\\_zip & category\\_id & item\\_price & quantity & payment\\_datetime & delivery\\_date & weight & weight\\_units & package\\_size & record\\_number\\\\\n",
       "  & <int> & <chr> & <int> & <dbl> & <chr> & <int> & <dbl> & <int> & <int> & <chr> & <chr> & <int> & <dbl> & <int> & <chr> & <chr> & <int> & <int> & <chr> & <int>\\\\\n",
       "\\hline\n",
       "\t1 & 0 & B2C &   25454 & 3 & 2019-03-26 15:11:00.000-07:00 & 0 & 0.0 & 3 & 5 & 97219      & 49040 & 13 & 27.95 & 1 & 2019-03-24 03:56:49.000-07:00 & 2019-03-29 & 5 & 1 & LETTER                 & 1\\\\\n",
       "\t2 & 1 & C2C & 6727381 & 2 & 2018-06-02 12:53:00.000-07:00 & 0 & 3.0 & 3 & 5 & 11415-3528 & 62521 &  0 & 20.50 & 1 & 2018-06-01 13:43:54.000-07:00 & 2018-06-05 & 0 & 1 & PACKAGE\\_THICK\\_ENVELOPE & 2\\\\\n",
       "\t3 & 2 & B2C &   18507 & 1 & 2019-01-07 16:22:00.000-05:00 & 0 & 4.5 & 3 & 5 & 27292      & 53010 &  1 & 19.90 & 1 & 2019-01-06 00:02:00.000-05:00 & 2019-01-10 & 9 & 1 & PACKAGE\\_THICK\\_ENVELOPE & 3\\\\\n",
       "\t4 & 3 & B2C &    4677 & 1 & 2018-12-17 16:56:00.000-08:00 & 0 & 0.0 & 3 & 5 & 90703      & 80022 &  1 & 35.50 & 1 & 2018-12-16 10:28:28.000-08:00 & 2018-12-21 & 8 & 1 & PACKAGE\\_THICK\\_ENVELOPE & 4\\\\\n",
       "\t5 & 4 & B2C &    4677 & 1 & 2018-07-27 16:48:00.000-07:00 & 0 & 0.0 & 3 & 5 & 90703      & 55070 &  1 & 25.00 & 1 & 2018-07-26 18:20:02.000-07:00 & 2018-07-30 & 3 & 1 & PACKAGE\\_THICK\\_ENVELOPE & 5\\\\\n",
       "\t6 & 5 & B2C &   10514 & 1 & 2019-04-19 19:42:00.000-04:00 & 0 & 0.0 & 3 & 5 & 43215      & 77063 &  3 & 10.39 & 1 & 2019-04-18 14:11:09.000-04:00 & 2019-04-22 & 1 & 1 & PACKAGE\\_THICK\\_ENVELOPE & 6\\\\\n",
       "\\end{tabular}\n"
      ],
      "text/markdown": [
       "\n",
       "A data.frame: 6 × 20\n",
       "\n",
       "| <!--/--> | X &lt;int&gt; | b2c_c2c &lt;chr&gt; | seller_id &lt;int&gt; | declared_handling_days &lt;dbl&gt; | acceptance_scan_timestamp &lt;chr&gt; | shipment_method_id &lt;int&gt; | shipping_fee &lt;dbl&gt; | carrier_min_estimate &lt;int&gt; | carrier_max_estimate &lt;int&gt; | item_zip &lt;chr&gt; | buyer_zip &lt;chr&gt; | category_id &lt;int&gt; | item_price &lt;dbl&gt; | quantity &lt;int&gt; | payment_datetime &lt;chr&gt; | delivery_date &lt;chr&gt; | weight &lt;int&gt; | weight_units &lt;int&gt; | package_size &lt;chr&gt; | record_number &lt;int&gt; |\n",
       "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|\n",
       "| 1 | 0 | B2C |   25454 | 3 | 2019-03-26 15:11:00.000-07:00 | 0 | 0.0 | 3 | 5 | 97219      | 49040 | 13 | 27.95 | 1 | 2019-03-24 03:56:49.000-07:00 | 2019-03-29 | 5 | 1 | LETTER                 | 1 |\n",
       "| 2 | 1 | C2C | 6727381 | 2 | 2018-06-02 12:53:00.000-07:00 | 0 | 3.0 | 3 | 5 | 11415-3528 | 62521 |  0 | 20.50 | 1 | 2018-06-01 13:43:54.000-07:00 | 2018-06-05 | 0 | 1 | PACKAGE_THICK_ENVELOPE | 2 |\n",
       "| 3 | 2 | B2C |   18507 | 1 | 2019-01-07 16:22:00.000-05:00 | 0 | 4.5 | 3 | 5 | 27292      | 53010 |  1 | 19.90 | 1 | 2019-01-06 00:02:00.000-05:00 | 2019-01-10 | 9 | 1 | PACKAGE_THICK_ENVELOPE | 3 |\n",
       "| 4 | 3 | B2C |    4677 | 1 | 2018-12-17 16:56:00.000-08:00 | 0 | 0.0 | 3 | 5 | 90703      | 80022 |  1 | 35.50 | 1 | 2018-12-16 10:28:28.000-08:00 | 2018-12-21 | 8 | 1 | PACKAGE_THICK_ENVELOPE | 4 |\n",
       "| 5 | 4 | B2C |    4677 | 1 | 2018-07-27 16:48:00.000-07:00 | 0 | 0.0 | 3 | 5 | 90703      | 55070 |  1 | 25.00 | 1 | 2018-07-26 18:20:02.000-07:00 | 2018-07-30 | 3 | 1 | PACKAGE_THICK_ENVELOPE | 5 |\n",
       "| 6 | 5 | B2C |   10514 | 1 | 2019-04-19 19:42:00.000-04:00 | 0 | 0.0 | 3 | 5 | 43215      | 77063 |  3 | 10.39 | 1 | 2019-04-18 14:11:09.000-04:00 | 2019-04-22 | 1 | 1 | PACKAGE_THICK_ENVELOPE | 6 |\n",
       "\n"
      ],
      "text/plain": [
       "  X b2c_c2c seller_id declared_handling_days acceptance_scan_timestamp    \n",
       "1 0 B2C       25454   3                      2019-03-26 15:11:00.000-07:00\n",
       "2 1 C2C     6727381   2                      2018-06-02 12:53:00.000-07:00\n",
       "3 2 B2C       18507   1                      2019-01-07 16:22:00.000-05:00\n",
       "4 3 B2C        4677   1                      2018-12-17 16:56:00.000-08:00\n",
       "5 4 B2C        4677   1                      2018-07-27 16:48:00.000-07:00\n",
       "6 5 B2C       10514   1                      2019-04-19 19:42:00.000-04:00\n",
       "  shipment_method_id shipping_fee carrier_min_estimate carrier_max_estimate\n",
       "1 0                  0.0          3                    5                   \n",
       "2 0                  3.0          3                    5                   \n",
       "3 0                  4.5          3                    5                   \n",
       "4 0                  0.0          3                    5                   \n",
       "5 0                  0.0          3                    5                   \n",
       "6 0                  0.0          3                    5                   \n",
       "  item_zip   buyer_zip category_id item_price quantity\n",
       "1 97219      49040     13          27.95      1       \n",
       "2 11415-3528 62521      0          20.50      1       \n",
       "3 27292      53010      1          19.90      1       \n",
       "4 90703      80022      1          35.50      1       \n",
       "5 90703      55070      1          25.00      1       \n",
       "6 43215      77063      3          10.39      1       \n",
       "  payment_datetime              delivery_date weight weight_units\n",
       "1 2019-03-24 03:56:49.000-07:00 2019-03-29    5      1           \n",
       "2 2018-06-01 13:43:54.000-07:00 2018-06-05    0      1           \n",
       "3 2019-01-06 00:02:00.000-05:00 2019-01-10    9      1           \n",
       "4 2018-12-16 10:28:28.000-08:00 2018-12-21    8      1           \n",
       "5 2018-07-26 18:20:02.000-07:00 2018-07-30    3      1           \n",
       "6 2019-04-18 14:11:09.000-04:00 2019-04-22    1      1           \n",
       "  package_size           record_number\n",
       "1 LETTER                 1            \n",
       "2 PACKAGE_THICK_ENVELOPE 2            \n",
       "3 PACKAGE_THICK_ENVELOPE 3            \n",
       "4 PACKAGE_THICK_ENVELOPE 4            \n",
       "5 PACKAGE_THICK_ENVELOPE 5            \n",
       "6 PACKAGE_THICK_ENVELOPE 6            "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "head(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "bcddb468",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T22:17:45.648876Z",
     "iopub.status.busy": "2022-12-09T22:17:45.647465Z",
     "iopub.status.idle": "2022-12-09T22:17:45.662329Z",
     "shell.execute_reply": "2022-12-09T22:17:45.660974Z"
    },
    "papermill": {
     "duration": 0.026636,
     "end_time": "2022-12-09T22:17:45.664801",
     "exception": false,
     "start_time": "2022-12-09T22:17:45.638165",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "15000000"
      ],
      "text/latex": [
       "15000000"
      ],
      "text/markdown": [
       "15000000"
      ],
      "text/plain": [
       "[1] 15000000"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "nrow(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "19b8718c",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T22:17:45.684503Z",
     "iopub.status.busy": "2022-12-09T22:17:45.683042Z",
     "iopub.status.idle": "2022-12-09T22:17:45.695851Z",
     "shell.execute_reply": "2022-12-09T22:17:45.694407Z"
    },
    "papermill": {
     "duration": 0.024777,
     "end_time": "2022-12-09T22:17:45.697853",
     "exception": false,
     "start_time": "2022-12-09T22:17:45.673076",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "#creating a copy of the datframe\n",
    "data <- data.frame(df)     "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "d6167932",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T22:17:45.717212Z",
     "iopub.status.busy": "2022-12-09T22:17:45.715832Z",
     "iopub.status.idle": "2022-12-09T22:17:45.731582Z",
     "shell.execute_reply": "2022-12-09T22:17:45.730071Z"
    },
    "papermill": {
     "duration": 0.02717,
     "end_time": "2022-12-09T22:17:45.733446",
     "exception": false,
     "start_time": "2022-12-09T22:17:45.706276",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<style>\n",
       ".list-inline {list-style: none; margin:0; padding: 0}\n",
       ".list-inline>li {display: inline-block}\n",
       ".list-inline>li:not(:last-child)::after {content: \"\\00b7\"; padding: 0 .5ex}\n",
       "</style>\n",
       "<ol class=list-inline><li>'X'</li><li>'b2c_c2c'</li><li>'seller_id'</li><li>'declared_handling_days'</li><li>'acceptance_scan_timestamp'</li><li>'shipment_method_id'</li><li>'shipping_fee'</li><li>'carrier_min_estimate'</li><li>'carrier_max_estimate'</li><li>'item_zip'</li><li>'buyer_zip'</li><li>'category_id'</li><li>'item_price'</li><li>'quantity'</li><li>'payment_datetime'</li><li>'delivery_date'</li><li>'weight'</li><li>'weight_units'</li><li>'package_size'</li><li>'record_number'</li></ol>\n"
      ],
      "text/latex": [
       "\\begin{enumerate*}\n",
       "\\item 'X'\n",
       "\\item 'b2c\\_c2c'\n",
       "\\item 'seller\\_id'\n",
       "\\item 'declared\\_handling\\_days'\n",
       "\\item 'acceptance\\_scan\\_timestamp'\n",
       "\\item 'shipment\\_method\\_id'\n",
       "\\item 'shipping\\_fee'\n",
       "\\item 'carrier\\_min\\_estimate'\n",
       "\\item 'carrier\\_max\\_estimate'\n",
       "\\item 'item\\_zip'\n",
       "\\item 'buyer\\_zip'\n",
       "\\item 'category\\_id'\n",
       "\\item 'item\\_price'\n",
       "\\item 'quantity'\n",
       "\\item 'payment\\_datetime'\n",
       "\\item 'delivery\\_date'\n",
       "\\item 'weight'\n",
       "\\item 'weight\\_units'\n",
       "\\item 'package\\_size'\n",
       "\\item 'record\\_number'\n",
       "\\end{enumerate*}\n"
      ],
      "text/markdown": [
       "1. 'X'\n",
       "2. 'b2c_c2c'\n",
       "3. 'seller_id'\n",
       "4. 'declared_handling_days'\n",
       "5. 'acceptance_scan_timestamp'\n",
       "6. 'shipment_method_id'\n",
       "7. 'shipping_fee'\n",
       "8. 'carrier_min_estimate'\n",
       "9. 'carrier_max_estimate'\n",
       "10. 'item_zip'\n",
       "11. 'buyer_zip'\n",
       "12. 'category_id'\n",
       "13. 'item_price'\n",
       "14. 'quantity'\n",
       "15. 'payment_datetime'\n",
       "16. 'delivery_date'\n",
       "17. 'weight'\n",
       "18. 'weight_units'\n",
       "19. 'package_size'\n",
       "20. 'record_number'\n",
       "\n",
       "\n"
      ],
      "text/plain": [
       " [1] \"X\"                         \"b2c_c2c\"                  \n",
       " [3] \"seller_id\"                 \"declared_handling_days\"   \n",
       " [5] \"acceptance_scan_timestamp\" \"shipment_method_id\"       \n",
       " [7] \"shipping_fee\"              \"carrier_min_estimate\"     \n",
       " [9] \"carrier_max_estimate\"      \"item_zip\"                 \n",
       "[11] \"buyer_zip\"                 \"category_id\"              \n",
       "[13] \"item_price\"                \"quantity\"                 \n",
       "[15] \"payment_datetime\"          \"delivery_date\"            \n",
       "[17] \"weight\"                    \"weight_units\"             \n",
       "[19] \"package_size\"              \"record_number\"            "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#cheking all columns\n",
    "colnames(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "5e9acc3c",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T22:17:45.753217Z",
     "iopub.status.busy": "2022-12-09T22:17:45.751795Z",
     "iopub.status.idle": "2022-12-09T22:17:55.999666Z",
     "shell.execute_reply": "2022-12-09T22:17:55.998297Z"
    },
    "papermill": {
     "duration": 10.259654,
     "end_time": "2022-12-09T22:17:56.001472",
     "exception": false,
     "start_time": "2022-12-09T22:17:45.741818",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<style>\n",
       ".dl-inline {width: auto; margin:0; padding: 0}\n",
       ".dl-inline>dt, .dl-inline>dd {float: none; width: auto; display: inline-block}\n",
       ".dl-inline>dt::after {content: \":\\0020\"; padding-right: .5ex}\n",
       ".dl-inline>dt:not(:first-of-type) {padding-left: .5ex}\n",
       "</style><dl class=dl-inline><dt>X</dt><dd>0</dd><dt>b2c_c2c</dt><dd>0</dd><dt>seller_id</dt><dd>0</dd><dt>declared_handling_days</dt><dd>702886</dd><dt>acceptance_scan_timestamp</dt><dd>0</dd><dt>shipment_method_id</dt><dd>0</dd><dt>shipping_fee</dt><dd>0</dd><dt>carrier_min_estimate</dt><dd>0</dd><dt>carrier_max_estimate</dt><dd>0</dd><dt>item_zip</dt><dd>0</dd><dt>buyer_zip</dt><dd>0</dd><dt>category_id</dt><dd>0</dd><dt>item_price</dt><dd>0</dd><dt>quantity</dt><dd>0</dd><dt>payment_datetime</dt><dd>0</dd><dt>delivery_date</dt><dd>0</dd><dt>weight</dt><dd>0</dd><dt>weight_units</dt><dd>0</dd><dt>package_size</dt><dd>0</dd><dt>record_number</dt><dd>0</dd></dl>\n"
      ],
      "text/latex": [
       "\\begin{description*}\n",
       "\\item[X] 0\n",
       "\\item[b2c\\textbackslash{}\\_c2c] 0\n",
       "\\item[seller\\textbackslash{}\\_id] 0\n",
       "\\item[declared\\textbackslash{}\\_handling\\textbackslash{}\\_days] 702886\n",
       "\\item[acceptance\\textbackslash{}\\_scan\\textbackslash{}\\_timestamp] 0\n",
       "\\item[shipment\\textbackslash{}\\_method\\textbackslash{}\\_id] 0\n",
       "\\item[shipping\\textbackslash{}\\_fee] 0\n",
       "\\item[carrier\\textbackslash{}\\_min\\textbackslash{}\\_estimate] 0\n",
       "\\item[carrier\\textbackslash{}\\_max\\textbackslash{}\\_estimate] 0\n",
       "\\item[item\\textbackslash{}\\_zip] 0\n",
       "\\item[buyer\\textbackslash{}\\_zip] 0\n",
       "\\item[category\\textbackslash{}\\_id] 0\n",
       "\\item[item\\textbackslash{}\\_price] 0\n",
       "\\item[quantity] 0\n",
       "\\item[payment\\textbackslash{}\\_datetime] 0\n",
       "\\item[delivery\\textbackslash{}\\_date] 0\n",
       "\\item[weight] 0\n",
       "\\item[weight\\textbackslash{}\\_units] 0\n",
       "\\item[package\\textbackslash{}\\_size] 0\n",
       "\\item[record\\textbackslash{}\\_number] 0\n",
       "\\end{description*}\n"
      ],
      "text/markdown": [
       "X\n",
       ":   0b2c_c2c\n",
       ":   0seller_id\n",
       ":   0declared_handling_days\n",
       ":   702886acceptance_scan_timestamp\n",
       ":   0shipment_method_id\n",
       ":   0shipping_fee\n",
       ":   0carrier_min_estimate\n",
       ":   0carrier_max_estimate\n",
       ":   0item_zip\n",
       ":   0buyer_zip\n",
       ":   0category_id\n",
       ":   0item_price\n",
       ":   0quantity\n",
       ":   0payment_datetime\n",
       ":   0delivery_date\n",
       ":   0weight\n",
       ":   0weight_units\n",
       ":   0package_size\n",
       ":   0record_number\n",
       ":   0\n",
       "\n"
      ],
      "text/plain": [
       "                        X                   b2c_c2c                 seller_id \n",
       "                        0                         0                         0 \n",
       "   declared_handling_days acceptance_scan_timestamp        shipment_method_id \n",
       "                   702886                         0                         0 \n",
       "             shipping_fee      carrier_min_estimate      carrier_max_estimate \n",
       "                        0                         0                         0 \n",
       "                 item_zip                 buyer_zip               category_id \n",
       "                        0                         0                         0 \n",
       "               item_price                  quantity          payment_datetime \n",
       "                        0                         0                         0 \n",
       "            delivery_date                    weight              weight_units \n",
       "                        0                         0                         0 \n",
       "             package_size             record_number \n",
       "                        0                         0 "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#checkig how many null values exist is datafram\n",
    "# sum(is.na(df))\n",
    "colSums(is.na(data))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d2a98572",
   "metadata": {
    "papermill": {
     "duration": 0.007957,
     "end_time": "2022-12-09T22:17:56.017648",
     "exception": false,
     "start_time": "2022-12-09T22:17:56.009691",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "declared_handling_days is the only column with missing values =702886.\n",
    "declared_handling_days - The number of days taken by the seller to ship the carrier from the day of acceptance.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "784d17b2",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T22:17:56.036319Z",
     "iopub.status.busy": "2022-12-09T22:17:56.034986Z",
     "iopub.status.idle": "2022-12-09T22:18:12.336750Z",
     "shell.execute_reply": "2022-12-09T22:18:12.335226Z"
    },
    "papermill": {
     "duration": 16.31339,
     "end_time": "2022-12-09T22:18:12.338979",
     "exception": false,
     "start_time": "2022-12-09T22:17:56.025589",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "#dropping column since imputing such a large number of missing values might create a bias in the data\n",
    "data = subset(df, select = -c(X) )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "6fdb1c2a",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T22:18:12.358650Z",
     "iopub.status.busy": "2022-12-09T22:18:12.357277Z",
     "iopub.status.idle": "2022-12-09T22:18:12.387723Z",
     "shell.execute_reply": "2022-12-09T22:18:12.386374Z"
    },
    "papermill": {
     "duration": 0.04253,
     "end_time": "2022-12-09T22:18:12.389835",
     "exception": false,
     "start_time": "2022-12-09T22:18:12.347305",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "'data.frame':\t15000000 obs. of  19 variables:\n",
      " $ b2c_c2c                  : chr  \"B2C\" \"C2C\" \"B2C\" \"B2C\" ...\n",
      " $ seller_id                : int  25454 6727381 18507 4677 4677 10514 104 340356 113915 130301 ...\n",
      " $ declared_handling_days   : num  3 2 1 1 1 1 1 1 5 1 ...\n",
      " $ acceptance_scan_timestamp: chr  \"2019-03-26 15:11:00.000-07:00\" \"2018-06-02 12:53:00.000-07:00\" \"2019-01-07 16:22:00.000-05:00\" \"2018-12-17 16:56:00.000-08:00\" ...\n",
      " $ shipment_method_id       : int  0 0 0 0 0 0 0 0 3 1 ...\n",
      " $ shipping_fee             : num  0 3 4.5 0 0 0 0 2.95 0 0 ...\n",
      " $ carrier_min_estimate     : int  3 3 3 3 3 3 3 3 2 2 ...\n",
      " $ carrier_max_estimate     : int  5 5 5 5 5 5 5 5 8 5 ...\n",
      " $ item_zip                 : chr  \"97219\" \"11415-3528\" \"27292\" \"90703\" ...\n",
      " $ buyer_zip                : chr  \"49040\" \"62521\" \"53010\" \"80022\" ...\n",
      " $ category_id              : int  13 0 1 1 1 3 11 1 18 13 ...\n",
      " $ item_price               : num  27.9 20.5 19.9 35.5 25 ...\n",
      " $ quantity                 : int  1 1 1 1 1 1 1 1 1 1 ...\n",
      " $ payment_datetime         : chr  \"2019-03-24 03:56:49.000-07:00\" \"2018-06-01 13:43:54.000-07:00\" \"2019-01-06 00:02:00.000-05:00\" \"2018-12-16 10:28:28.000-08:00\" ...\n",
      " $ delivery_date            : chr  \"2019-03-29\" \"2018-06-05\" \"2019-01-10\" \"2018-12-21\" ...\n",
      " $ weight                   : int  5 0 9 8 3 1 0 1 0 112 ...\n",
      " $ weight_units             : int  1 1 1 1 1 1 1 1 1 1 ...\n",
      " $ package_size             : chr  \"LETTER\" \"PACKAGE_THICK_ENVELOPE\" \"PACKAGE_THICK_ENVELOPE\" \"PACKAGE_THICK_ENVELOPE\" ...\n",
      " $ record_number            : int  1 2 3 4 5 6 7 8 9 10 ...\n"
     ]
    }
   ],
   "source": [
    "str(data)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bc64f19f",
   "metadata": {
    "papermill": {
     "duration": 0.008336,
     "end_time": "2022-12-09T22:18:12.407111",
     "exception": false,
     "start_time": "2022-12-09T22:18:12.398775",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "#Overall columnwise analysis \n",
    "\n",
    "1) b2c_c2c - It of type string with values b2c or c2c. This explains if the transaction happening is between business to customers or between customers and other customers.\n",
    "\n",
    "2) seller_id - This is a unique ID given to each seller for identification. It is of type Long Int.\n",
    "\n",
    "3) declared_handling_days - The number of days taken by the seller to ship the carrier from the day of acceptance.\n",
    "\n",
    "4) acceptance_scan_timestamp - The date and time when the carrier has accepted the package for the final shipment. The values in this are of type timestamp.\n",
    "\n",
    "5) shipment_method_id - The integer type attribute defines the type of shipping service declared by the seller.\n",
    "\n",
    "6) shipping_fee - Transportation and handling charges charged by the seller for shipping the items. All the values are in USD.\n",
    "\n",
    "7) carrier_min_estimate - The minimum estimate of the number of required days by the carrier for the specified service.\n",
    "\n",
    "8) carrier_max_estimate - The maximum estimate of the number of required days by the carrier for the specified service.\n",
    "\n",
    "9) item_zip - The US Postal zip code of the package origin/source.\n",
    "\n",
    "10) buyer_zip - The US Postal zip code of the package destination.\n",
    "\n",
    "11) category_id - An integer type data attribute that categorizes the package by its type.\n",
    "\n",
    "12) item_price - The price per item involved in the transaction.\n",
    "\n",
    "13) quantity - Number of items involved in the transaction.\n",
    "\n",
    "15) payment_datetime - A timestamp attribute that clocks in the time when the payment has been done for the particular transaction.\n",
    "\n",
    "16) delivery_date - The actual delivery date of the package. This is the attribute that we need to predict using the other attributes.\n",
    "\n",
    "17) weight - A scalar value that determines the sum of the weight of all quantities involved in the transaction.\n",
    "\n",
    "18) weight_units - It defines the weight scalar value by telling if the measurements are in kilograms or pounds. Pounds are represented as 1 and Kilograms are denoted by 2.\n",
    "\n",
    "19) package_size - It is a categorical value which categorizes the packages based on its sizes.\n",
    "\n",
    "20) record_number - Unique integer number given to the transaction to identify them."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "620ea0f8",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T22:18:12.426719Z",
     "iopub.status.busy": "2022-12-09T22:18:12.425618Z",
     "iopub.status.idle": "2022-12-09T22:18:12.640245Z",
     "shell.execute_reply": "2022-12-09T22:18:12.638493Z"
    },
    "papermill": {
     "duration": 0.227134,
     "end_time": "2022-12-09T22:18:12.643031",
     "exception": false,
     "start_time": "2022-12-09T22:18:12.415897",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<style>\n",
       ".list-inline {list-style: none; margin:0; padding: 0}\n",
       ".list-inline>li {display: inline-block}\n",
       ".list-inline>li:not(:last-child)::after {content: \"\\00b7\"; padding: 0 .5ex}\n",
       "</style>\n",
       "<ol class=list-inline><li>'B2C'</li><li>'C2C'</li></ol>\n"
      ],
      "text/latex": [
       "\\begin{enumerate*}\n",
       "\\item 'B2C'\n",
       "\\item 'C2C'\n",
       "\\end{enumerate*}\n"
      ],
      "text/markdown": [
       "1. 'B2C'\n",
       "2. 'C2C'\n",
       "\n",
       "\n"
      ],
      "text/plain": [
       "[1] \"B2C\" \"C2C\""
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#we will encode this value \n",
    "unique(data$b2c_c2c) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "d77e62d4",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T22:18:12.663016Z",
     "iopub.status.busy": "2022-12-09T22:18:12.661671Z",
     "iopub.status.idle": "2022-12-09T22:18:13.238761Z",
     "shell.execute_reply": "2022-12-09T22:18:13.237198Z"
    },
    "papermill": {
     "duration": 0.589033,
     "end_time": "2022-12-09T22:18:13.240682",
     "exception": false,
     "start_time": "2022-12-09T22:18:12.651649",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "#encoding B2C as 0 and c2c as 1\n",
    "data$b2c_c2c<-ifelse(data$b2c_c2c==\"B2C\",0,1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "26267a2d",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T22:18:13.261032Z",
     "iopub.status.busy": "2022-12-09T22:18:13.259690Z",
     "iopub.status.idle": "2022-12-09T22:18:13.283558Z",
     "shell.execute_reply": "2022-12-09T22:18:13.282190Z"
    },
    "papermill": {
     "duration": 0.036153,
     "end_time": "2022-12-09T22:18:13.285441",
     "exception": false,
     "start_time": "2022-12-09T22:18:13.249288",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<table class=\"dataframe\">\n",
       "<caption>A data.frame: 6 × 19</caption>\n",
       "<thead>\n",
       "\t<tr><th></th><th scope=col>b2c_c2c</th><th scope=col>seller_id</th><th scope=col>declared_handling_days</th><th scope=col>acceptance_scan_timestamp</th><th scope=col>shipment_method_id</th><th scope=col>shipping_fee</th><th scope=col>carrier_min_estimate</th><th scope=col>carrier_max_estimate</th><th scope=col>item_zip</th><th scope=col>buyer_zip</th><th scope=col>category_id</th><th scope=col>item_price</th><th scope=col>quantity</th><th scope=col>payment_datetime</th><th scope=col>delivery_date</th><th scope=col>weight</th><th scope=col>weight_units</th><th scope=col>package_size</th><th scope=col>record_number</th></tr>\n",
       "\t<tr><th></th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;chr&gt;</th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;chr&gt;</th><th scope=col>&lt;chr&gt;</th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;chr&gt;</th><th scope=col>&lt;chr&gt;</th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;chr&gt;</th><th scope=col>&lt;int&gt;</th></tr>\n",
       "</thead>\n",
       "<tbody>\n",
       "\t<tr><th scope=row>1</th><td>0</td><td>  25454</td><td>3</td><td>2019-03-26 15:11:00.000-07:00</td><td>0</td><td>0.0</td><td>3</td><td>5</td><td>97219     </td><td>49040</td><td>13</td><td>27.95</td><td>1</td><td>2019-03-24 03:56:49.000-07:00</td><td>2019-03-29</td><td>5</td><td>1</td><td>LETTER                </td><td>1</td></tr>\n",
       "\t<tr><th scope=row>2</th><td>1</td><td>6727381</td><td>2</td><td>2018-06-02 12:53:00.000-07:00</td><td>0</td><td>3.0</td><td>3</td><td>5</td><td>11415-3528</td><td>62521</td><td> 0</td><td>20.50</td><td>1</td><td>2018-06-01 13:43:54.000-07:00</td><td>2018-06-05</td><td>0</td><td>1</td><td>PACKAGE_THICK_ENVELOPE</td><td>2</td></tr>\n",
       "\t<tr><th scope=row>3</th><td>0</td><td>  18507</td><td>1</td><td>2019-01-07 16:22:00.000-05:00</td><td>0</td><td>4.5</td><td>3</td><td>5</td><td>27292     </td><td>53010</td><td> 1</td><td>19.90</td><td>1</td><td>2019-01-06 00:02:00.000-05:00</td><td>2019-01-10</td><td>9</td><td>1</td><td>PACKAGE_THICK_ENVELOPE</td><td>3</td></tr>\n",
       "\t<tr><th scope=row>4</th><td>0</td><td>   4677</td><td>1</td><td>2018-12-17 16:56:00.000-08:00</td><td>0</td><td>0.0</td><td>3</td><td>5</td><td>90703     </td><td>80022</td><td> 1</td><td>35.50</td><td>1</td><td>2018-12-16 10:28:28.000-08:00</td><td>2018-12-21</td><td>8</td><td>1</td><td>PACKAGE_THICK_ENVELOPE</td><td>4</td></tr>\n",
       "\t<tr><th scope=row>5</th><td>0</td><td>   4677</td><td>1</td><td>2018-07-27 16:48:00.000-07:00</td><td>0</td><td>0.0</td><td>3</td><td>5</td><td>90703     </td><td>55070</td><td> 1</td><td>25.00</td><td>1</td><td>2018-07-26 18:20:02.000-07:00</td><td>2018-07-30</td><td>3</td><td>1</td><td>PACKAGE_THICK_ENVELOPE</td><td>5</td></tr>\n",
       "\t<tr><th scope=row>6</th><td>0</td><td>  10514</td><td>1</td><td>2019-04-19 19:42:00.000-04:00</td><td>0</td><td>0.0</td><td>3</td><td>5</td><td>43215     </td><td>77063</td><td> 3</td><td>10.39</td><td>1</td><td>2019-04-18 14:11:09.000-04:00</td><td>2019-04-22</td><td>1</td><td>1</td><td>PACKAGE_THICK_ENVELOPE</td><td>6</td></tr>\n",
       "</tbody>\n",
       "</table>\n"
      ],
      "text/latex": [
       "A data.frame: 6 × 19\n",
       "\\begin{tabular}{r|lllllllllllllllllll}\n",
       "  & b2c\\_c2c & seller\\_id & declared\\_handling\\_days & acceptance\\_scan\\_timestamp & shipment\\_method\\_id & shipping\\_fee & carrier\\_min\\_estimate & carrier\\_max\\_estimate & item\\_zip & buyer\\_zip & category\\_id & item\\_price & quantity & payment\\_datetime & delivery\\_date & weight & weight\\_units & package\\_size & record\\_number\\\\\n",
       "  & <dbl> & <int> & <dbl> & <chr> & <int> & <dbl> & <int> & <int> & <chr> & <chr> & <int> & <dbl> & <int> & <chr> & <chr> & <int> & <int> & <chr> & <int>\\\\\n",
       "\\hline\n",
       "\t1 & 0 &   25454 & 3 & 2019-03-26 15:11:00.000-07:00 & 0 & 0.0 & 3 & 5 & 97219      & 49040 & 13 & 27.95 & 1 & 2019-03-24 03:56:49.000-07:00 & 2019-03-29 & 5 & 1 & LETTER                 & 1\\\\\n",
       "\t2 & 1 & 6727381 & 2 & 2018-06-02 12:53:00.000-07:00 & 0 & 3.0 & 3 & 5 & 11415-3528 & 62521 &  0 & 20.50 & 1 & 2018-06-01 13:43:54.000-07:00 & 2018-06-05 & 0 & 1 & PACKAGE\\_THICK\\_ENVELOPE & 2\\\\\n",
       "\t3 & 0 &   18507 & 1 & 2019-01-07 16:22:00.000-05:00 & 0 & 4.5 & 3 & 5 & 27292      & 53010 &  1 & 19.90 & 1 & 2019-01-06 00:02:00.000-05:00 & 2019-01-10 & 9 & 1 & PACKAGE\\_THICK\\_ENVELOPE & 3\\\\\n",
       "\t4 & 0 &    4677 & 1 & 2018-12-17 16:56:00.000-08:00 & 0 & 0.0 & 3 & 5 & 90703      & 80022 &  1 & 35.50 & 1 & 2018-12-16 10:28:28.000-08:00 & 2018-12-21 & 8 & 1 & PACKAGE\\_THICK\\_ENVELOPE & 4\\\\\n",
       "\t5 & 0 &    4677 & 1 & 2018-07-27 16:48:00.000-07:00 & 0 & 0.0 & 3 & 5 & 90703      & 55070 &  1 & 25.00 & 1 & 2018-07-26 18:20:02.000-07:00 & 2018-07-30 & 3 & 1 & PACKAGE\\_THICK\\_ENVELOPE & 5\\\\\n",
       "\t6 & 0 &   10514 & 1 & 2019-04-19 19:42:00.000-04:00 & 0 & 0.0 & 3 & 5 & 43215      & 77063 &  3 & 10.39 & 1 & 2019-04-18 14:11:09.000-04:00 & 2019-04-22 & 1 & 1 & PACKAGE\\_THICK\\_ENVELOPE & 6\\\\\n",
       "\\end{tabular}\n"
      ],
      "text/markdown": [
       "\n",
       "A data.frame: 6 × 19\n",
       "\n",
       "| <!--/--> | b2c_c2c &lt;dbl&gt; | seller_id &lt;int&gt; | declared_handling_days &lt;dbl&gt; | acceptance_scan_timestamp &lt;chr&gt; | shipment_method_id &lt;int&gt; | shipping_fee &lt;dbl&gt; | carrier_min_estimate &lt;int&gt; | carrier_max_estimate &lt;int&gt; | item_zip &lt;chr&gt; | buyer_zip &lt;chr&gt; | category_id &lt;int&gt; | item_price &lt;dbl&gt; | quantity &lt;int&gt; | payment_datetime &lt;chr&gt; | delivery_date &lt;chr&gt; | weight &lt;int&gt; | weight_units &lt;int&gt; | package_size &lt;chr&gt; | record_number &lt;int&gt; |\n",
       "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|\n",
       "| 1 | 0 |   25454 | 3 | 2019-03-26 15:11:00.000-07:00 | 0 | 0.0 | 3 | 5 | 97219      | 49040 | 13 | 27.95 | 1 | 2019-03-24 03:56:49.000-07:00 | 2019-03-29 | 5 | 1 | LETTER                 | 1 |\n",
       "| 2 | 1 | 6727381 | 2 | 2018-06-02 12:53:00.000-07:00 | 0 | 3.0 | 3 | 5 | 11415-3528 | 62521 |  0 | 20.50 | 1 | 2018-06-01 13:43:54.000-07:00 | 2018-06-05 | 0 | 1 | PACKAGE_THICK_ENVELOPE | 2 |\n",
       "| 3 | 0 |   18507 | 1 | 2019-01-07 16:22:00.000-05:00 | 0 | 4.5 | 3 | 5 | 27292      | 53010 |  1 | 19.90 | 1 | 2019-01-06 00:02:00.000-05:00 | 2019-01-10 | 9 | 1 | PACKAGE_THICK_ENVELOPE | 3 |\n",
       "| 4 | 0 |    4677 | 1 | 2018-12-17 16:56:00.000-08:00 | 0 | 0.0 | 3 | 5 | 90703      | 80022 |  1 | 35.50 | 1 | 2018-12-16 10:28:28.000-08:00 | 2018-12-21 | 8 | 1 | PACKAGE_THICK_ENVELOPE | 4 |\n",
       "| 5 | 0 |    4677 | 1 | 2018-07-27 16:48:00.000-07:00 | 0 | 0.0 | 3 | 5 | 90703      | 55070 |  1 | 25.00 | 1 | 2018-07-26 18:20:02.000-07:00 | 2018-07-30 | 3 | 1 | PACKAGE_THICK_ENVELOPE | 5 |\n",
       "| 6 | 0 |   10514 | 1 | 2019-04-19 19:42:00.000-04:00 | 0 | 0.0 | 3 | 5 | 43215      | 77063 |  3 | 10.39 | 1 | 2019-04-18 14:11:09.000-04:00 | 2019-04-22 | 1 | 1 | PACKAGE_THICK_ENVELOPE | 6 |\n",
       "\n"
      ],
      "text/plain": [
       "  b2c_c2c seller_id declared_handling_days acceptance_scan_timestamp    \n",
       "1 0         25454   3                      2019-03-26 15:11:00.000-07:00\n",
       "2 1       6727381   2                      2018-06-02 12:53:00.000-07:00\n",
       "3 0         18507   1                      2019-01-07 16:22:00.000-05:00\n",
       "4 0          4677   1                      2018-12-17 16:56:00.000-08:00\n",
       "5 0          4677   1                      2018-07-27 16:48:00.000-07:00\n",
       "6 0         10514   1                      2019-04-19 19:42:00.000-04:00\n",
       "  shipment_method_id shipping_fee carrier_min_estimate carrier_max_estimate\n",
       "1 0                  0.0          3                    5                   \n",
       "2 0                  3.0          3                    5                   \n",
       "3 0                  4.5          3                    5                   \n",
       "4 0                  0.0          3                    5                   \n",
       "5 0                  0.0          3                    5                   \n",
       "6 0                  0.0          3                    5                   \n",
       "  item_zip   buyer_zip category_id item_price quantity\n",
       "1 97219      49040     13          27.95      1       \n",
       "2 11415-3528 62521      0          20.50      1       \n",
       "3 27292      53010      1          19.90      1       \n",
       "4 90703      80022      1          35.50      1       \n",
       "5 90703      55070      1          25.00      1       \n",
       "6 43215      77063      3          10.39      1       \n",
       "  payment_datetime              delivery_date weight weight_units\n",
       "1 2019-03-24 03:56:49.000-07:00 2019-03-29    5      1           \n",
       "2 2018-06-01 13:43:54.000-07:00 2018-06-05    0      1           \n",
       "3 2019-01-06 00:02:00.000-05:00 2019-01-10    9      1           \n",
       "4 2018-12-16 10:28:28.000-08:00 2018-12-21    8      1           \n",
       "5 2018-07-26 18:20:02.000-07:00 2018-07-30    3      1           \n",
       "6 2019-04-18 14:11:09.000-04:00 2019-04-22    1      1           \n",
       "  package_size           record_number\n",
       "1 LETTER                 1            \n",
       "2 PACKAGE_THICK_ENVELOPE 2            \n",
       "3 PACKAGE_THICK_ENVELOPE 3            \n",
       "4 PACKAGE_THICK_ENVELOPE 4            \n",
       "5 PACKAGE_THICK_ENVELOPE 5            \n",
       "6 PACKAGE_THICK_ENVELOPE 6            "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "head(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "e37b3659",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T22:18:13.313973Z",
     "iopub.status.busy": "2022-12-09T22:18:13.312678Z",
     "iopub.status.idle": "2022-12-09T22:18:25.091221Z",
     "shell.execute_reply": "2022-12-09T22:18:25.089817Z"
    },
    "papermill": {
     "duration": 11.79887,
     "end_time": "2022-12-09T22:18:25.093113",
     "exception": false,
     "start_time": "2022-12-09T22:18:13.294243",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "    b2c_c2c        seller_id       declared_handling_days\n",
       " Min.   :0.000   Min.   :      0   Min.   : 0.0          \n",
       " 1st Qu.:0.000   1st Qu.:   5018   1st Qu.: 1.0          \n",
       " Median :0.000   Median :  37436   Median : 1.0          \n",
       " Mean   :0.291   Mean   : 271104   Mean   : 1.6          \n",
       " 3rd Qu.:1.000   3rd Qu.: 203533   3rd Qu.: 2.0          \n",
       " Max.   :1.000   Max.   :7266448   Max.   :40.0          \n",
       "                                   NA's   :702886        \n",
       " acceptance_scan_timestamp shipment_method_id  shipping_fee     \n",
       " Length:15000000           Min.   : 0.0000    Min.   :  -3.000  \n",
       " Class :character          1st Qu.: 0.0000    1st Qu.:   0.000  \n",
       " Mode  :character          Median : 0.0000    Median :   0.000  \n",
       "                           Mean   : 0.8819    Mean   :   2.812  \n",
       "                           3rd Qu.: 1.0000    3rd Qu.:   4.000  \n",
       "                           Max.   :26.0000    Max.   :2000.000  \n",
       "                                                                \n",
       " carrier_min_estimate carrier_max_estimate   item_zip        \n",
       " Min.   :-1.000       Min.   :-1.000       Length:15000000   \n",
       " 1st Qu.: 2.000       1st Qu.: 5.000       Class :character  \n",
       " Median : 3.000       Median : 5.000       Mode  :character  \n",
       " Mean   : 2.622       Mean   : 5.462                         \n",
       " 3rd Qu.: 3.000       3rd Qu.: 5.000                         \n",
       " Max.   : 6.000       Max.   :25.000                         \n",
       "                                                             \n",
       "  buyer_zip          category_id       item_price          quantity      \n",
       " Length:15000000    Min.   : 0.000   Min.   :    0.00   Min.   :  1.000  \n",
       " Class :character   1st Qu.: 1.000   1st Qu.:    8.75   1st Qu.:  1.000  \n",
       " Mode  :character   Median : 5.000   Median :   15.00   Median :  1.000  \n",
       "                    Mean   : 6.755   Mean   :   36.14   Mean   :  1.106  \n",
       "                    3rd Qu.:11.000   3rd Qu.:   30.25   3rd Qu.:  1.000  \n",
       "                    Max.   :32.000   Max.   :60000.00   Max.   :775.000  \n",
       "                                                                         \n",
       " payment_datetime   delivery_date          weight          weight_units\n",
       " Length:15000000    Length:15000000    Min.   :     0.0   Min.   :1    \n",
       " Class :character   Class :character   1st Qu.:     0.0   1st Qu.:1    \n",
       " Mode  :character   Mode  :character   Median :     4.0   Median :1    \n",
       "                                       Mean   :    16.1   Mean   :1    \n",
       "                                       3rd Qu.:    16.0   3rd Qu.:1    \n",
       "                                       Max.   :695664.0   Max.   :2    \n",
       "                                                                       \n",
       " package_size       record_number     \n",
       " Length:15000000    Min.   :       1  \n",
       " Class :character   1st Qu.: 3750001  \n",
       " Mode  :character   Median : 7500000  \n",
       "                    Mean   : 7500000  \n",
       "                    3rd Qu.:11250000  \n",
       "                    Max.   :15000000  \n",
       "                                      "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#checking for the summary of the data to understand columnwise what is happening in each column\n",
    "summary(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "26c0ec39",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T22:18:25.113609Z",
     "iopub.status.busy": "2022-12-09T22:18:25.112323Z",
     "iopub.status.idle": "2022-12-09T22:18:26.003558Z",
     "shell.execute_reply": "2022-12-09T22:18:26.002000Z"
    },
    "papermill": {
     "duration": 0.903605,
     "end_time": "2022-12-09T22:18:26.005628",
     "exception": false,
     "start_time": "2022-12-09T22:18:25.102023",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "# library(tidyverse)\n",
    "#preparing data for conversion to numeric values, truncating zipcode value\n",
    "data$item_zip <- str_trunc(data$item_zip, 5, side = c(\"right\"),  ellipsis = \"\")\n",
    "data$buyer_zip <- str_trunc(data$buyer_zip, 5, side = c(\"right\"),  ellipsis = \"\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "af2e084d",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T22:18:26.027590Z",
     "iopub.status.busy": "2022-12-09T22:18:26.026274Z",
     "iopub.status.idle": "2022-12-09T22:18:26.036194Z",
     "shell.execute_reply": "2022-12-09T22:18:26.034844Z"
    },
    "papermill": {
     "duration": 0.022881,
     "end_time": "2022-12-09T22:18:26.038146",
     "exception": false,
     "start_time": "2022-12-09T22:18:26.015265",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "# #preparing data for conversion to numeric values\n",
    "# data$item_zip <- gsub(\"-\", \"\", data$item_zip)\n",
    "# data$buyer_zip <- gsub(\"-\", \"\", data$buyer_zip)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "83f3bd05",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T22:18:26.060030Z",
     "iopub.status.busy": "2022-12-09T22:18:26.058799Z",
     "iopub.status.idle": "2022-12-09T22:18:30.284395Z",
     "shell.execute_reply": "2022-12-09T22:18:30.282773Z"
    },
    "papermill": {
     "duration": 4.239215,
     "end_time": "2022-12-09T22:18:30.287131",
     "exception": false,
     "start_time": "2022-12-09T22:18:26.047916",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Warning message in eval(expr, envir, enclos):\n",
      "“NAs introduced by coercion”\n",
      "Warning message in eval(expr, envir, enclos):\n",
      "“NAs introduced by coercion”\n"
     ]
    }
   ],
   "source": [
    "#converting to numeric\n",
    "data$item_zip = as.numeric(as.character(data$item_zip))\n",
    "data$buyer_zip = as.numeric(as.character(data$buyer_zip))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "990b5e70",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T22:18:30.309130Z",
     "iopub.status.busy": "2022-12-09T22:18:30.307691Z",
     "iopub.status.idle": "2022-12-09T22:18:30.331859Z",
     "shell.execute_reply": "2022-12-09T22:18:30.330499Z"
    },
    "papermill": {
     "duration": 0.037097,
     "end_time": "2022-12-09T22:18:30.333604",
     "exception": false,
     "start_time": "2022-12-09T22:18:30.296507",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<table class=\"dataframe\">\n",
       "<caption>A data.frame: 6 × 19</caption>\n",
       "<thead>\n",
       "\t<tr><th></th><th scope=col>b2c_c2c</th><th scope=col>seller_id</th><th scope=col>declared_handling_days</th><th scope=col>acceptance_scan_timestamp</th><th scope=col>shipment_method_id</th><th scope=col>shipping_fee</th><th scope=col>carrier_min_estimate</th><th scope=col>carrier_max_estimate</th><th scope=col>item_zip</th><th scope=col>buyer_zip</th><th scope=col>category_id</th><th scope=col>item_price</th><th scope=col>quantity</th><th scope=col>payment_datetime</th><th scope=col>delivery_date</th><th scope=col>weight</th><th scope=col>weight_units</th><th scope=col>package_size</th><th scope=col>record_number</th></tr>\n",
       "\t<tr><th></th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;chr&gt;</th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;chr&gt;</th><th scope=col>&lt;chr&gt;</th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;chr&gt;</th><th scope=col>&lt;int&gt;</th></tr>\n",
       "</thead>\n",
       "<tbody>\n",
       "\t<tr><th scope=row>1</th><td>0</td><td>  25454</td><td>3</td><td>2019-03-26 15:11:00.000-07:00</td><td>0</td><td>0.0</td><td>3</td><td>5</td><td>97219</td><td>49040</td><td>13</td><td>27.95</td><td>1</td><td>2019-03-24 03:56:49.000-07:00</td><td>2019-03-29</td><td>5</td><td>1</td><td>LETTER                </td><td>1</td></tr>\n",
       "\t<tr><th scope=row>2</th><td>1</td><td>6727381</td><td>2</td><td>2018-06-02 12:53:00.000-07:00</td><td>0</td><td>3.0</td><td>3</td><td>5</td><td>11415</td><td>62521</td><td> 0</td><td>20.50</td><td>1</td><td>2018-06-01 13:43:54.000-07:00</td><td>2018-06-05</td><td>0</td><td>1</td><td>PACKAGE_THICK_ENVELOPE</td><td>2</td></tr>\n",
       "\t<tr><th scope=row>3</th><td>0</td><td>  18507</td><td>1</td><td>2019-01-07 16:22:00.000-05:00</td><td>0</td><td>4.5</td><td>3</td><td>5</td><td>27292</td><td>53010</td><td> 1</td><td>19.90</td><td>1</td><td>2019-01-06 00:02:00.000-05:00</td><td>2019-01-10</td><td>9</td><td>1</td><td>PACKAGE_THICK_ENVELOPE</td><td>3</td></tr>\n",
       "\t<tr><th scope=row>4</th><td>0</td><td>   4677</td><td>1</td><td>2018-12-17 16:56:00.000-08:00</td><td>0</td><td>0.0</td><td>3</td><td>5</td><td>90703</td><td>80022</td><td> 1</td><td>35.50</td><td>1</td><td>2018-12-16 10:28:28.000-08:00</td><td>2018-12-21</td><td>8</td><td>1</td><td>PACKAGE_THICK_ENVELOPE</td><td>4</td></tr>\n",
       "\t<tr><th scope=row>5</th><td>0</td><td>   4677</td><td>1</td><td>2018-07-27 16:48:00.000-07:00</td><td>0</td><td>0.0</td><td>3</td><td>5</td><td>90703</td><td>55070</td><td> 1</td><td>25.00</td><td>1</td><td>2018-07-26 18:20:02.000-07:00</td><td>2018-07-30</td><td>3</td><td>1</td><td>PACKAGE_THICK_ENVELOPE</td><td>5</td></tr>\n",
       "\t<tr><th scope=row>6</th><td>0</td><td>  10514</td><td>1</td><td>2019-04-19 19:42:00.000-04:00</td><td>0</td><td>0.0</td><td>3</td><td>5</td><td>43215</td><td>77063</td><td> 3</td><td>10.39</td><td>1</td><td>2019-04-18 14:11:09.000-04:00</td><td>2019-04-22</td><td>1</td><td>1</td><td>PACKAGE_THICK_ENVELOPE</td><td>6</td></tr>\n",
       "</tbody>\n",
       "</table>\n"
      ],
      "text/latex": [
       "A data.frame: 6 × 19\n",
       "\\begin{tabular}{r|lllllllllllllllllll}\n",
       "  & b2c\\_c2c & seller\\_id & declared\\_handling\\_days & acceptance\\_scan\\_timestamp & shipment\\_method\\_id & shipping\\_fee & carrier\\_min\\_estimate & carrier\\_max\\_estimate & item\\_zip & buyer\\_zip & category\\_id & item\\_price & quantity & payment\\_datetime & delivery\\_date & weight & weight\\_units & package\\_size & record\\_number\\\\\n",
       "  & <dbl> & <int> & <dbl> & <chr> & <int> & <dbl> & <int> & <int> & <dbl> & <dbl> & <int> & <dbl> & <int> & <chr> & <chr> & <int> & <int> & <chr> & <int>\\\\\n",
       "\\hline\n",
       "\t1 & 0 &   25454 & 3 & 2019-03-26 15:11:00.000-07:00 & 0 & 0.0 & 3 & 5 & 97219 & 49040 & 13 & 27.95 & 1 & 2019-03-24 03:56:49.000-07:00 & 2019-03-29 & 5 & 1 & LETTER                 & 1\\\\\n",
       "\t2 & 1 & 6727381 & 2 & 2018-06-02 12:53:00.000-07:00 & 0 & 3.0 & 3 & 5 & 11415 & 62521 &  0 & 20.50 & 1 & 2018-06-01 13:43:54.000-07:00 & 2018-06-05 & 0 & 1 & PACKAGE\\_THICK\\_ENVELOPE & 2\\\\\n",
       "\t3 & 0 &   18507 & 1 & 2019-01-07 16:22:00.000-05:00 & 0 & 4.5 & 3 & 5 & 27292 & 53010 &  1 & 19.90 & 1 & 2019-01-06 00:02:00.000-05:00 & 2019-01-10 & 9 & 1 & PACKAGE\\_THICK\\_ENVELOPE & 3\\\\\n",
       "\t4 & 0 &    4677 & 1 & 2018-12-17 16:56:00.000-08:00 & 0 & 0.0 & 3 & 5 & 90703 & 80022 &  1 & 35.50 & 1 & 2018-12-16 10:28:28.000-08:00 & 2018-12-21 & 8 & 1 & PACKAGE\\_THICK\\_ENVELOPE & 4\\\\\n",
       "\t5 & 0 &    4677 & 1 & 2018-07-27 16:48:00.000-07:00 & 0 & 0.0 & 3 & 5 & 90703 & 55070 &  1 & 25.00 & 1 & 2018-07-26 18:20:02.000-07:00 & 2018-07-30 & 3 & 1 & PACKAGE\\_THICK\\_ENVELOPE & 5\\\\\n",
       "\t6 & 0 &   10514 & 1 & 2019-04-19 19:42:00.000-04:00 & 0 & 0.0 & 3 & 5 & 43215 & 77063 &  3 & 10.39 & 1 & 2019-04-18 14:11:09.000-04:00 & 2019-04-22 & 1 & 1 & PACKAGE\\_THICK\\_ENVELOPE & 6\\\\\n",
       "\\end{tabular}\n"
      ],
      "text/markdown": [
       "\n",
       "A data.frame: 6 × 19\n",
       "\n",
       "| <!--/--> | b2c_c2c &lt;dbl&gt; | seller_id &lt;int&gt; | declared_handling_days &lt;dbl&gt; | acceptance_scan_timestamp &lt;chr&gt; | shipment_method_id &lt;int&gt; | shipping_fee &lt;dbl&gt; | carrier_min_estimate &lt;int&gt; | carrier_max_estimate &lt;int&gt; | item_zip &lt;dbl&gt; | buyer_zip &lt;dbl&gt; | category_id &lt;int&gt; | item_price &lt;dbl&gt; | quantity &lt;int&gt; | payment_datetime &lt;chr&gt; | delivery_date &lt;chr&gt; | weight &lt;int&gt; | weight_units &lt;int&gt; | package_size &lt;chr&gt; | record_number &lt;int&gt; |\n",
       "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|\n",
       "| 1 | 0 |   25454 | 3 | 2019-03-26 15:11:00.000-07:00 | 0 | 0.0 | 3 | 5 | 97219 | 49040 | 13 | 27.95 | 1 | 2019-03-24 03:56:49.000-07:00 | 2019-03-29 | 5 | 1 | LETTER                 | 1 |\n",
       "| 2 | 1 | 6727381 | 2 | 2018-06-02 12:53:00.000-07:00 | 0 | 3.0 | 3 | 5 | 11415 | 62521 |  0 | 20.50 | 1 | 2018-06-01 13:43:54.000-07:00 | 2018-06-05 | 0 | 1 | PACKAGE_THICK_ENVELOPE | 2 |\n",
       "| 3 | 0 |   18507 | 1 | 2019-01-07 16:22:00.000-05:00 | 0 | 4.5 | 3 | 5 | 27292 | 53010 |  1 | 19.90 | 1 | 2019-01-06 00:02:00.000-05:00 | 2019-01-10 | 9 | 1 | PACKAGE_THICK_ENVELOPE | 3 |\n",
       "| 4 | 0 |    4677 | 1 | 2018-12-17 16:56:00.000-08:00 | 0 | 0.0 | 3 | 5 | 90703 | 80022 |  1 | 35.50 | 1 | 2018-12-16 10:28:28.000-08:00 | 2018-12-21 | 8 | 1 | PACKAGE_THICK_ENVELOPE | 4 |\n",
       "| 5 | 0 |    4677 | 1 | 2018-07-27 16:48:00.000-07:00 | 0 | 0.0 | 3 | 5 | 90703 | 55070 |  1 | 25.00 | 1 | 2018-07-26 18:20:02.000-07:00 | 2018-07-30 | 3 | 1 | PACKAGE_THICK_ENVELOPE | 5 |\n",
       "| 6 | 0 |   10514 | 1 | 2019-04-19 19:42:00.000-04:00 | 0 | 0.0 | 3 | 5 | 43215 | 77063 |  3 | 10.39 | 1 | 2019-04-18 14:11:09.000-04:00 | 2019-04-22 | 1 | 1 | PACKAGE_THICK_ENVELOPE | 6 |\n",
       "\n"
      ],
      "text/plain": [
       "  b2c_c2c seller_id declared_handling_days acceptance_scan_timestamp    \n",
       "1 0         25454   3                      2019-03-26 15:11:00.000-07:00\n",
       "2 1       6727381   2                      2018-06-02 12:53:00.000-07:00\n",
       "3 0         18507   1                      2019-01-07 16:22:00.000-05:00\n",
       "4 0          4677   1                      2018-12-17 16:56:00.000-08:00\n",
       "5 0          4677   1                      2018-07-27 16:48:00.000-07:00\n",
       "6 0         10514   1                      2019-04-19 19:42:00.000-04:00\n",
       "  shipment_method_id shipping_fee carrier_min_estimate carrier_max_estimate\n",
       "1 0                  0.0          3                    5                   \n",
       "2 0                  3.0          3                    5                   \n",
       "3 0                  4.5          3                    5                   \n",
       "4 0                  0.0          3                    5                   \n",
       "5 0                  0.0          3                    5                   \n",
       "6 0                  0.0          3                    5                   \n",
       "  item_zip buyer_zip category_id item_price quantity\n",
       "1 97219    49040     13          27.95      1       \n",
       "2 11415    62521      0          20.50      1       \n",
       "3 27292    53010      1          19.90      1       \n",
       "4 90703    80022      1          35.50      1       \n",
       "5 90703    55070      1          25.00      1       \n",
       "6 43215    77063      3          10.39      1       \n",
       "  payment_datetime              delivery_date weight weight_units\n",
       "1 2019-03-24 03:56:49.000-07:00 2019-03-29    5      1           \n",
       "2 2018-06-01 13:43:54.000-07:00 2018-06-05    0      1           \n",
       "3 2019-01-06 00:02:00.000-05:00 2019-01-10    9      1           \n",
       "4 2018-12-16 10:28:28.000-08:00 2018-12-21    8      1           \n",
       "5 2018-07-26 18:20:02.000-07:00 2018-07-30    3      1           \n",
       "6 2019-04-18 14:11:09.000-04:00 2019-04-22    1      1           \n",
       "  package_size           record_number\n",
       "1 LETTER                 1            \n",
       "2 PACKAGE_THICK_ENVELOPE 2            \n",
       "3 PACKAGE_THICK_ENVELOPE 3            \n",
       "4 PACKAGE_THICK_ENVELOPE 4            \n",
       "5 PACKAGE_THICK_ENVELOPE 5            \n",
       "6 PACKAGE_THICK_ENVELOPE 6            "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "head(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "9c2b91ee",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T22:18:30.355317Z",
     "iopub.status.busy": "2022-12-09T22:18:30.353904Z",
     "iopub.status.idle": "2022-12-09T22:18:35.422570Z",
     "shell.execute_reply": "2022-12-09T22:18:35.421176Z"
    },
    "papermill": {
     "duration": 5.081579,
     "end_time": "2022-12-09T22:18:35.424479",
     "exception": false,
     "start_time": "2022-12-09T22:18:30.342900",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<style>\n",
       ".dl-inline {width: auto; margin:0; padding: 0}\n",
       ".dl-inline>dt, .dl-inline>dd {float: none; width: auto; display: inline-block}\n",
       ".dl-inline>dt::after {content: \":\\0020\"; padding-right: .5ex}\n",
       ".dl-inline>dt:not(:first-of-type) {padding-left: .5ex}\n",
       "</style><dl class=dl-inline><dt>b2c_c2c</dt><dd>0</dd><dt>seller_id</dt><dd>0</dd><dt>declared_handling_days</dt><dd>702886</dd><dt>acceptance_scan_timestamp</dt><dd>0</dd><dt>shipment_method_id</dt><dd>0</dd><dt>shipping_fee</dt><dd>0</dd><dt>carrier_min_estimate</dt><dd>0</dd><dt>carrier_max_estimate</dt><dd>0</dd><dt>item_zip</dt><dd>5001</dd><dt>buyer_zip</dt><dd>606</dd><dt>category_id</dt><dd>0</dd><dt>item_price</dt><dd>0</dd><dt>quantity</dt><dd>0</dd><dt>payment_datetime</dt><dd>0</dd><dt>delivery_date</dt><dd>0</dd><dt>weight</dt><dd>0</dd><dt>weight_units</dt><dd>0</dd><dt>package_size</dt><dd>0</dd><dt>record_number</dt><dd>0</dd></dl>\n"
      ],
      "text/latex": [
       "\\begin{description*}\n",
       "\\item[b2c\\textbackslash{}\\_c2c] 0\n",
       "\\item[seller\\textbackslash{}\\_id] 0\n",
       "\\item[declared\\textbackslash{}\\_handling\\textbackslash{}\\_days] 702886\n",
       "\\item[acceptance\\textbackslash{}\\_scan\\textbackslash{}\\_timestamp] 0\n",
       "\\item[shipment\\textbackslash{}\\_method\\textbackslash{}\\_id] 0\n",
       "\\item[shipping\\textbackslash{}\\_fee] 0\n",
       "\\item[carrier\\textbackslash{}\\_min\\textbackslash{}\\_estimate] 0\n",
       "\\item[carrier\\textbackslash{}\\_max\\textbackslash{}\\_estimate] 0\n",
       "\\item[item\\textbackslash{}\\_zip] 5001\n",
       "\\item[buyer\\textbackslash{}\\_zip] 606\n",
       "\\item[category\\textbackslash{}\\_id] 0\n",
       "\\item[item\\textbackslash{}\\_price] 0\n",
       "\\item[quantity] 0\n",
       "\\item[payment\\textbackslash{}\\_datetime] 0\n",
       "\\item[delivery\\textbackslash{}\\_date] 0\n",
       "\\item[weight] 0\n",
       "\\item[weight\\textbackslash{}\\_units] 0\n",
       "\\item[package\\textbackslash{}\\_size] 0\n",
       "\\item[record\\textbackslash{}\\_number] 0\n",
       "\\end{description*}\n"
      ],
      "text/markdown": [
       "b2c_c2c\n",
       ":   0seller_id\n",
       ":   0declared_handling_days\n",
       ":   702886acceptance_scan_timestamp\n",
       ":   0shipment_method_id\n",
       ":   0shipping_fee\n",
       ":   0carrier_min_estimate\n",
       ":   0carrier_max_estimate\n",
       ":   0item_zip\n",
       ":   5001buyer_zip\n",
       ":   606category_id\n",
       ":   0item_price\n",
       ":   0quantity\n",
       ":   0payment_datetime\n",
       ":   0delivery_date\n",
       ":   0weight\n",
       ":   0weight_units\n",
       ":   0package_size\n",
       ":   0record_number\n",
       ":   0\n",
       "\n"
      ],
      "text/plain": [
       "                  b2c_c2c                 seller_id    declared_handling_days \n",
       "                        0                         0                    702886 \n",
       "acceptance_scan_timestamp        shipment_method_id              shipping_fee \n",
       "                        0                         0                         0 \n",
       "     carrier_min_estimate      carrier_max_estimate                  item_zip \n",
       "                        0                         0                      5001 \n",
       "                buyer_zip               category_id                item_price \n",
       "                      606                         0                         0 \n",
       "                 quantity          payment_datetime             delivery_date \n",
       "                        0                         0                         0 \n",
       "                   weight              weight_units              package_size \n",
       "                        0                         0                         0 \n",
       "            record_number \n",
       "                        0 "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#checkig how many null values exist is datafram\n",
    "# sum(is.na(df))\n",
    "colSums(is.na(data))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "9131ac11",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T22:18:35.447991Z",
     "iopub.status.busy": "2022-12-09T22:18:35.446205Z",
     "iopub.status.idle": "2022-12-09T22:18:59.909733Z",
     "shell.execute_reply": "2022-12-09T22:18:59.908242Z"
    },
    "papermill": {
     "duration": 24.477816,
     "end_time": "2022-12-09T22:18:59.911876",
     "exception": false,
     "start_time": "2022-12-09T22:18:35.434060",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "# drop values where zip codes are NA\n",
    "data <- data[!is.na(data$item_zip),]\n",
    "data <- data[!is.na(data$buyer_zip),]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "2694590e",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T22:18:59.934404Z",
     "iopub.status.busy": "2022-12-09T22:18:59.933156Z",
     "iopub.status.idle": "2022-12-09T22:19:02.115387Z",
     "shell.execute_reply": "2022-12-09T22:19:02.114026Z"
    },
    "papermill": {
     "duration": 2.195825,
     "end_time": "2022-12-09T22:19:02.117558",
     "exception": false,
     "start_time": "2022-12-09T22:18:59.921733",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "21"
      ],
      "text/latex": [
       "21"
      ],
      "text/markdown": [
       "21"
      ],
      "text/plain": [
       "[1] 21"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#minimum shipping fee should not be negative so checking to see how any such values exist, neither should the carrier values.\n",
    "nrow(data[data$shipping_fee < 0,])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "65eb17bd",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T22:19:02.140192Z",
     "iopub.status.busy": "2022-12-09T22:19:02.138930Z",
     "iopub.status.idle": "2022-12-09T22:19:11.574229Z",
     "shell.execute_reply": "2022-12-09T22:19:11.572753Z"
    },
    "papermill": {
     "duration": 9.448764,
     "end_time": "2022-12-09T22:19:11.576119",
     "exception": false,
     "start_time": "2022-12-09T22:19:02.127355",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "#replacing neg values of shipping with zero\n",
    "data[data$shipping_fee < 0,] <- 0     # Set negative values to 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "b3fd5467",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T22:19:11.598403Z",
     "iopub.status.busy": "2022-12-09T22:19:11.597122Z",
     "iopub.status.idle": "2022-12-09T22:19:11.812323Z",
     "shell.execute_reply": "2022-12-09T22:19:11.810933Z"
    },
    "papermill": {
     "duration": 0.228166,
     "end_time": "2022-12-09T22:19:11.814109",
     "exception": false,
     "start_time": "2022-12-09T22:19:11.585943",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<style>\n",
       ".list-inline {list-style: none; margin:0; padding: 0}\n",
       ".list-inline>li {display: inline-block}\n",
       ".list-inline>li:not(:last-child)::after {content: \"\\00b7\"; padding: 0 .5ex}\n",
       "</style>\n",
       "<ol class=list-inline><li>'LETTER'</li><li>'PACKAGE_THICK_ENVELOPE'</li><li>'NONE'</li><li>'LARGE_PACKAGE'</li><li>'LARGE_ENVELOPE'</li><li>'0'</li><li>'EXTRA_LARGE_PACKAGE'</li><li>'VERY_LARGE_PACKAGE'</li></ol>\n"
      ],
      "text/latex": [
       "\\begin{enumerate*}\n",
       "\\item 'LETTER'\n",
       "\\item 'PACKAGE\\_THICK\\_ENVELOPE'\n",
       "\\item 'NONE'\n",
       "\\item 'LARGE\\_PACKAGE'\n",
       "\\item 'LARGE\\_ENVELOPE'\n",
       "\\item '0'\n",
       "\\item 'EXTRA\\_LARGE\\_PACKAGE'\n",
       "\\item 'VERY\\_LARGE\\_PACKAGE'\n",
       "\\end{enumerate*}\n"
      ],
      "text/markdown": [
       "1. 'LETTER'\n",
       "2. 'PACKAGE_THICK_ENVELOPE'\n",
       "3. 'NONE'\n",
       "4. 'LARGE_PACKAGE'\n",
       "5. 'LARGE_ENVELOPE'\n",
       "6. '0'\n",
       "7. 'EXTRA_LARGE_PACKAGE'\n",
       "8. 'VERY_LARGE_PACKAGE'\n",
       "\n",
       "\n"
      ],
      "text/plain": [
       "[1] \"LETTER\"                 \"PACKAGE_THICK_ENVELOPE\" \"NONE\"                  \n",
       "[4] \"LARGE_PACKAGE\"          \"LARGE_ENVELOPE\"         \"0\"                     \n",
       "[7] \"EXTRA_LARGE_PACKAGE\"    \"VERY_LARGE_PACKAGE\"    "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#only pacakge_size column has character values that need to be encoded before feeding it into the model\n",
    "unique(data$package_size)#checking values in it"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "bae44e7d",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T22:19:11.836646Z",
     "iopub.status.busy": "2022-12-09T22:19:11.835262Z",
     "iopub.status.idle": "2022-12-09T22:19:20.410694Z",
     "shell.execute_reply": "2022-12-09T22:19:20.409247Z"
    },
    "papermill": {
     "duration": 8.588896,
     "end_time": "2022-12-09T22:19:20.412841",
     "exception": false,
     "start_time": "2022-12-09T22:19:11.823945",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "21"
      ],
      "text/latex": [
       "21"
      ],
      "text/markdown": [
       "21"
      ],
      "text/plain": [
       "[1] 21"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#checking how many zero values and if theyre of any significance\n",
    "nrow(data[data$package_size==0,]) #only 21 data points which seems to be incorrect so dropping these rows.\n",
    "data <- data[!(data$package_size ==0),]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "7676a551",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T22:19:20.436669Z",
     "iopub.status.busy": "2022-12-09T22:19:20.435305Z",
     "iopub.status.idle": "2022-12-09T22:19:32.763444Z",
     "shell.execute_reply": "2022-12-09T22:19:32.761957Z"
    },
    "papermill": {
     "duration": 12.342451,
     "end_time": "2022-12-09T22:19:32.765554",
     "exception": false,
     "start_time": "2022-12-09T22:19:20.423103",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "#converting all package weights to kg and then dropping weight units column.\n",
    "#if values in weight unit column = 1, then multiply weight*0.453592.\n",
    "\n",
    "data$weight<-ifelse(data$weight_units==1,data$weight*0.453592,data$weight)\n",
    "data = subset(data, select = -c(weight_units) )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "485bc0da",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T22:19:32.788810Z",
     "iopub.status.busy": "2022-12-09T22:19:32.787532Z",
     "iopub.status.idle": "2022-12-09T22:19:40.904192Z",
     "shell.execute_reply": "2022-12-09T22:19:40.902672Z"
    },
    "papermill": {
     "duration": 8.131084,
     "end_time": "2022-12-09T22:19:40.906729",
     "exception": false,
     "start_time": "2022-12-09T22:19:32.775645",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "#also weight of items cannot be 0 so checking how many such datapoints exist\n",
    "# nrow(data[data$weight==0,])\n",
    "# data <- data[!(data$weight ==0),]\n",
    "data <- data[!is.na(data$declared_handling_days),]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "69a1cf30",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T22:19:40.930184Z",
     "iopub.status.busy": "2022-12-09T22:19:40.928941Z",
     "iopub.status.idle": "2022-12-09T22:19:49.045512Z",
     "shell.execute_reply": "2022-12-09T22:19:49.044070Z"
    },
    "papermill": {
     "duration": 8.13097,
     "end_time": "2022-12-09T22:19:49.047904",
     "exception": false,
     "start_time": "2022-12-09T22:19:40.916934",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "# reset index of data table\n",
    "rownames(data) <- 1:nrow(data)  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "96ac5396",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T22:19:49.072385Z",
     "iopub.status.busy": "2022-12-09T22:19:49.070986Z",
     "iopub.status.idle": "2022-12-09T22:20:05.373230Z",
     "shell.execute_reply": "2022-12-09T22:20:05.369757Z"
    },
    "papermill": {
     "duration": 16.321499,
     "end_time": "2022-12-09T22:20:05.379788",
     "exception": false,
     "start_time": "2022-12-09T22:19:49.058289",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\nEEcYBQAAAADiCKMAAAAAQBxhFAAAAACII4wCAAAAAHGEUQAAAAAgjjAKAAAAAMQRRgEAAACA\nOMIoAAAAABBHGAUAAAAA4gijAAAAAEAcYRQAAAAAiCOMAgAAAABxhFEAAAAAII4wCgAAAADE\nEUYBAAAAgDjCKAAAAAAQRxgFAAAAAOIIowAAAABAHGEUAAAAAIgjjAIAAAAAcYRRAAAAACCO\nMAoAAAAAxBFGAQAAAIA4wigAAAAAEEcYBQAAAADiCKMAAAAAQBxhFAAAAACII4wCAAAAAHGE\nUQAAAAAgjjAKAAAAAMQRRgEAAACAOMIoAAAAABBHGAUAAAAA4gijAAAAAEAcYRQAAAAAiCOM\nAgAAAABxhFEAAAAAII4wCgAAAADEEUYBAAAAgDjCKAAAAAAQRxgFAAAAAOIIowAAAABAHGEU\nAAAAAIgjjAIAAAAAcYRRAAAAACCOMAoAAAAAxBFGAQAAAIA4wigAAAAAEEcYBQAAAADiCKMA\nAAAAQBxhFAAAAACII4wCAAAAAHGEUQAAAAAgjjAKAAAAAMQRRgEAAACAOMIoAAAAABBHGAUA\nAAAA4gijAAAAAEAcYRQAAAAAiCOMAgAAAABxhFEAAAAAII4wCgAAAADEEUYBAAAAgDjCKAAA\nAAAQRxgFAAAAAOIIowAAAABAHGEUAAAAAIgjjAIAAAAAcYRRAAAAACCOMAoAAAAAxBFGAQAA\nAIA4wigAAAAAEEcYBQAAAADiCKMAAAAAQBxhFAAAAACII4wCAAAAAHGEUQAAAAAgjjAKAAAA\nAMQRRgEAAACAOMIoAAAAABBHGAUAAAAA4gijAAAAAEAcYRQAAAAAiCOMAgAAAABxhFEAAAAA\nII4wCgAAAADEEUYBAAAAgDjCKAAAAAAQRxgFAAAAAOIIowAAAABAHGEUAAAAAIgjjAIAAAAA\ncYRRAAAAACCOMAoAAAAAxBFGAQAAAIA4wigAAAAAEEcYBQAAAADiCKMAAAAAQBxhFAAAAACI\nI4wCAAAAAHGEUQAAAAAgjjAKAAAAAMQRRgEAAACAOMIoAAAAABBHGAUAAAAA4gijAAAAAEAc\nYRQAAAAAiCOMAgAAAABxhFEAAAAAII4wCgAAAADEEUYBAAAAgDjCKAAAAAAQRxgFAAAAAOII\nowAAAABAHGEUAAAAAIgjjAIAAAAAcYRRAAAAACCOMAoAAAAAxBFGAQAAAIA4wigAAAAAEEcY\n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\nAAAA4gijAAAAAEAcYRQAAAAAiCOMAgAAAABxhFEAAAAAII4wCgAAAADEEUYBAAAAgDjCKAAA\nAAAQRxgFAAAAAOIIowAAAABAHGEUAAAAAIgjjAIAAAAAcYRRAAAAACCOMAoAAAAAxBFGAQAA\nAIA4wigAAAAAEEcYBQAAAADiCKMAAAAAQBxhFAAAAACII4wCAAAAAHGEUQAAAAAgjjAKAAAA\nAMQRRgEAAACAOMIoAAAAABBHGAUAAAAA4gijAAAAAEAcYRQAAAAAiCOMAgAAAABxhFEAAAAA\nII4wCgAAAADEEUYBAAAAgDjCKAAAAAAQRxgFAAAAAOIIowAAAABAHGEUAAAAAIgjjAIAAAAA\ncYRRAAAAACCOMAoAAAAAxBFGAQAAAIA4wigAAAAAEEcYBQAAAADiCKMAAAAAQBxhFAAAAACI\nI4wCAAAAAHGEUQAAAAAgjjAKAAAAAMQRRgEAAACAOMIoAAAAABBHGAUAAAAA4gijAAAAAEAc\nYRQAAAAAiCOMAgAAAABxhFEAAAAAII4wCgAAAADEEUYBAAAAgDjCKAAAAAAQRxgFAAAAAOII\nowAAAABAHGEUAAAAAIgjjAIAAAAAcYRRAAAAACCOMAoAAAAAxBFGAQAAAIA4wigAAAAAEEcY\nBQAAAADiCKMAAAAAQBxhFAAAAACII4wCAAAAAHGEUQAAAAAgjjAKAAAAAMQRRgEAAACAOMIo\nAAAAABBHGAUAAAAA4gijAAAAAEAcYRQAAAAAiCOMAgAAAABxhFEAAAAAII4wCgAAAADEEUYB\nAAAAgDjCKAAAAAAQRxgFAAAAAOIIowAAAABAHGEUAAAAAIgjjAIAAAAAcYRRAAAAACCOMAoA\nAAAAxBFGAQAAAIA4wigAAAAAEEcYBQAAAADiCKMAAAAAQBxhFAAAAACII4wCAAAAAHGEUQAA\nAAAgjjAKAAAAAMQRRgEAAACAOMIoAAAAABBHGAUAAAAA4gijAAAAAEAcYRQAAAAAiCOMAgAA\nAABxhFEAAAAAII4wCgAAAADEEUYBAAAAgDjCKAAAAAAQRxgFAAAAAOIIowAAAABAHGEUAAAA\nAIgjjAIAAAAAcYRRAAAAACCOMAoAAAAAxBFGAQAAAIA4wigAAAAAEEcYBQAAAADiCKMAAAAA\nQBxhFAAAAACII4wCAAAAAHGEUQAAAAAgzkCFf/bxf/y9f/+aO39gcHDsoukO1boAACAASURB\n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\nAIBwhFEAAAAAIBxhFAAAAAAIRxgFAAAAAMIRRgEAAACAcIRRAAAAACAcYRQAAAAACEcYBQAA\nAADCEUYBAAAAgHCEUQAAAAAgHGEUAAAAAAhHGAUAAAAAwhFGAQAAAIBwhFEAAAAAIBxhFAAA\nAAAIRxgFAAAAAMIRRgEAAACAcIRRAAAAACAcYRQAAAAACEcYBQAAAADCEUYBAAAAgHCEUQAA\nAAAgHGEUAAAAAAhHGAUAAAAAwhFGAQAAAIBwhFEAAAAAIBxhFAAAAAAIRxgFAAAAAMIRRgEA\nAACAcIRRAAAAACAcYRQAAAAACEcYBQAAAADCEUYBAAAAgHCEUQAAAAAgHGEUAAAAAAhHGAUA\nAAAAwhFGAQAAAIBwhFEAAAAAIBxhFAAAAAAIRxgFAAAAAMIRRgEAAACAcIRRAAAAACAcYRQA\nAAAACEcYBQAAAADCEUYBAAAAgHCEUQAAAAAgHGEUAAAAAAhHGAUAAAAAwhFGAQAAAIBwhFEA\nAAAAIBxhFAAAAAAIRxgFAAAAAMIRRgEAAACAcIRRAAAAACAcYRQAAAAACEcYBQAAAADCEUYB\nAAAAgHCEUQAAAAAgHGEUAAAAAAhHGAUAAAAAwhFGAQAAAIBwhFEAAAAAIBxhFAAAAAAIRxgF\nAAAAAMIRRgEAAACAcIRRAAAAACAcYRQAAAAACEcYBQAAAADCEUYBAAAAgHCEUQAAAAAgHGEU\nAAAAAAhHGAUAAAAAwhFGAQAAAIBwhFEAAAAAIBxhFAAAAAAIRxgFAAAAAMIRRgEAAACAcIRR\nAAAAACAcYRQAAAAACEcYBQAAAADCEUYBAAAAgHCEUQAAAAAgHGEUAAAAAAhHGAUAAAAAwhFG\nAQAAAIBwhFEAAAAAIBxhFAAAAAAIRxgFAAAAAMIRRgEAAACAcIRRAAAAACAcYRQAAAAACEcY\nBQAAAADCEUYBAAAAgHCEUQAAAAAgHGEUAAAAAAhHGAUAAAAAwsnVarWsZ2hslUol6xF4BYVC\nIaVUrVbd22ksuVwun88nP2doQPl8PpfL1Wq1arWa9SwwPO69NC6b3swVCodnPQJBVSo/ynqE\noGwbGkK1Wm1qatrV0eJojvJatX379qxHYJdyudy4ceNSSt3d3X19fVmPA8NQLBZbW1tTSp2d\nnf6FQ2Npbm4ulUrVatVDJA2nra0tl8v19vZ2d3dnPQsMg03vWDB+fNYTEJUdV1ZsehtCrVYT\n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\nEUYBAAAAgHCEUQAAAAAgHGEUAAAAAAhHGAUAAAAAwhFGAQAAAIBwhFEAAAAAIBxhFAAAAAAI\nRxgFAAAAAMIRRgEAAACAcIRRAAAAACAcYRQAAAAACEcYBQAAAADCEUYBAAAAgHCEUQAAAAAg\nHGEUAAAAAAhHGAUAAAAAwhFGAQAAAIBwhFEAAAAAIBxhFAAAAAAIRxgFAAAAAMIRRgEAAACA\ncIRRAAAAACAcYRQAAAAACEcYBQAAAADCEUYBAAAAgHCEUQAAAAAgHGEUAAAAAAhHGAUAAAAA\nwhFGAQAAAIBwhFEAAAAAIBxhFAAAAAAIRxgFAAAAAMIRRgEAAACAcIRRAAAAACAcYRQAAAAA\nCEcYBQAAAADCEUYBAAAAgHCEUQAAAAAgHGEUAAAAAAhHGAUAAAAAwhFGAQAAAIBwhFEAAAAA\nIBxhFAAAAAAIRxgFAAAAAMIRRgEAAACAcIRRAAAAACAcYRQAAAAACEcYBQAAAADCEUYBAAAA\ngHCEUQAAAAAgHGEUAAAAAAhHGAUAAAAAwhFGAQAAAIBwhFEAAAAAIBxhFAAAAAAIRxgFAAAA\nAMIRRgEAAACAcIRRAAAAACAcYRQAAAAACEcYBQAAAADCEUYBAAAAgHCEUQAAAAAgHGEUAAAA\nAAhHGAUAAAAAwhFGAQAAAIBwhFEAAAAAIBxhFAAAAAAIRxgFAAAAAMIRRgEAAACAcIRRAAAA\nACAcYRQAAAAACEcYBQAAAADCEUYBAAAAgHCEUQAAAAAgHGEUAAAAAAhHGAUAAAAAwhFGAQAA\nAIBwitn+8WuWX3DW53+248q8629+36SWlFJK1R8s/OrtSx9ctbXw5gMPP/2cM97YWtit9ZE9\nBQAAAABoeBk/Y3TTQ5taJ7///B0c1lbqP7Ty1guvWLR8zgfPuvi8Pys/dfcFn7q2tlvrI3sK\nAAAAAPAakPEzRp97bEv7AW9/+9tn/+6BWs/lix6fcerlJ/7BG1NKM76QTjrtH25afeqHpjQN\nb32vtmF/q0FO2attdG8eAAAAAKAuMn7G6MNbuicd0l7p3PKb5zbt+JTM7s1Lf9VVOe6Yqf1X\nmycddfC40n33rBnu+m58q0FOqfONAQAAAACMkoyfMfqT53urP7zqT7/8RG+tVmzb8z0fOnfe\n+w9KKfVs+2lK6YDyS+PNLhfvfGRzz1HDW9+NbzXIKQNXly9fvnr16v7Lra2tRx111EjcGNRF\nLpfrv1AqlfJ5nzZGIykWX/gp1NLSUqt5Pw8aSf+9N5/Pt7S0ZD0LDE//bqFYLLr30lhseiEy\nj1lZseltCIP/azrLMFrpeWZzrrDvHnO+8M1LJ1a23Pvd67507YXN+91w+qz2ave2lFJH00uf\nd9TRVOjd0jvc9ZTSCJ4ycPWWW25ZunRp/+WpU6ced9xxI3KDUFd+TtG42tq8jwcNKZ/Pjxs3\nLuspYHc0NTU1NTVlPQXsDpteCMiOK1s2vWNcpVIZ5GiWYbRQmrZ48eIXr3XMPeX8FXeevOS6\nR07/4jvyzeWU0obe6pTSC7/tXNdbKU4qDnc9pTSCpwxMXi6XJ0yY0H+5ra3NM7nGuP7fn/tr\nohG599KgBp645N5Lw3HvpXHZNmTuxZ8fMNr8j58V24aGMHafMbqzw17XumTj2pRSU/ktKd3z\nRGfvlFJz/6EVnX0TZ08c7vpufKtBThmY87LLLhu4XKlU1q9fX7ebhFcrl8tNnjw5pbR169ae\nnp6sx4FhKJVK/b+D2bBhgwdaGktbW1tra2tfX9+mTZuyngWGp729vVgsdnZ2btu2LetZYBhs\neseCjo6sJyAqUSIrNr2NomPXP6CzfPeZTSu+cubHPrmmp/rC9VrlntXb2w/YP6XU0n70tFLh\njmVr+4/0Pv/g/Vt7Dj16ynDXd+NbDXJK/W8SAAAAAGA0FBYsWJDVn12aOH3ZzYu+/fCGvV8/\ncdvaVXfe+KU7nqp96tLT9ioVUq4wq/rwwhvveN2MWc2dz970d19cXX7nJae8Izfc9ZSG/a0G\nOeXl/itqtVpXV9fo3nIMQy6XK5fLKaXu7u7B31cCxppCodDc3JxS6uzszHoWGJ5SqdTU1FSt\nVj1E0nBaWlry+XxfX19vb+8rfzWMGTa9Y0G5/O9Zj0BQ27d/JOsRgrLpbRT9D5EvK5ftyzO7\nNz76L9fc+F8Pr+gqTpg+48Djz5x3xD4vfsZIrXLXDVcuuuvH67tybzp47vxPnzWj/2Pih7s+\nsqfspFKpbNy4sX43Ea/SwKuKtmzZ4lVFNJaBl9KvX7/eS+lpLF5VROPyUnoalE3vWNDRcWzW\nIxDUunX/mfUIQdn0NopBXkqfcRh9DRBGxzh7RBqXMErjskekcQmjNCib3rFAGCUrwmhWbHob\nxRh9j1EAAAAAgEwIowAAAABAOMIoAAAAABCOMAoAAAAAhCOMAgAAAADhCKMAAAAAQDjCKAAA\nAAAQjjAKAAAAAIQjjAIAAAAA4QijAAAAAEA4wigAAAAAEI4wCgAAAACEI4wCAAAAAOEIowAA\nAABAOMIoAAAAABCOMAoAAAAAhCOMAgAAAADhCKMAAAAAQDjCKAAAAAAQjjAKAAAAAIQjjAIA\nAAAA4QijAAAAAEA4wigAAAAAEI4wCgAAAACEI4wCAAAAAOEIowAAAABAOMIoAAAAABCOMAoA\nAAAAhCOMAgAAAADhCKMAAAAAQDjCKAAAAAAQjjAKAAAAAIQjjAIAAAAA4QijAAAAAEA4wigA\nAAAAEI4wCgAAAACEI4wCAAAAAOEIowAAAABAOMIoAAAAABCOMAoAAAAAhCOMAgAAAADhCKMA\nAAAAQDjCKAAAAAAQjjAKAAAAAIQjjAIAAAAA4QijAAAAAEA4wigAAAAAEI4wCgAAAACEI4wC\nAAAAAOEIowAAAABAOMIoAAAAABCOMAoAAAAAhCOMAgAAAADhCKMAAAAAQDjCKAAAAAAQjjAK\nAAAAAIQjjAIAAAAA4QijAAAAAEA4wigAAAAAEI4wCgAAAACEI4wCAAAAAOEIowAAAABAOMIo\nAAAAABCOMAoAAAAAhCOMAgAAAADhCKMAAAAAQDjCKAAAAAAQjjAKAAAAAIQjjAIAAAAA4Qij\nAAAAAEA4wigAAAAAEI4wCgAAAACEI4wCAAAAAOEIowAAAABAOMIoAAAAABCOMAoAAAAAhCOM\nAgAAAADhCKMAAAAAQDjCKAAAAAAQjjAKAAAAAIQjjAIAAAAA4QijAAAAAEA4wigAAAAAEI4w\nCgAAAACEI4wCAAAAAOEIowAAAABAOMIoAAAAABCOMAoAAAAAhCOMAgAAAADhCKMAAAAAQDjC\nKAAAAAAQjjAKAAAAAIQjjAIAAAAA4QijAAAAAEA4wigAAAAAEI4wCgAAAACEI4wCAAAAAOEI\nowAAAABAOMIoAAAAABCOMAoAAAAAhCOMAgAAAADhCKMAAAAAQDjCKAAAAAAQjjAKAAAAAIQj\njAIAAAAA4QijAAAAAEA4wigAAAAAEI4wCgAAAACEI4wCAAAAAOEIowAAAABAOMIoAAAAABCO\nMAoAAAAAhCOMAgAAAADhCKMAAAAAQDjCKAAAAAAQjjAKAAAAAIQjjAIAAAAA4QijAAAAAEA4\nwigAAAAAEI4wCgAAAACEI4wCAAAAAOEIowAAAABAOMIoAAAAABCOMAoAAAAAhCOMAgAAAADh\n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\nP4896ar8rf7vX6cdvEgqOuvTK0f+9fCfSsp/XTX5wg8/t1+rZ0H7LbvlZT/+ytSKxaXz3nlr\nbskftuxa0/IQQhNu0qy9AQAAAAAsMZn8xOjPP9720c+lI/sVvf3WW5ULc1ut2b9vu7ar793p\n50NOOPOaI/bdql3i57eeum38/Dan/bVnSOSOHtL7uBvOeG7543u3X/jQ5RcVddvmgBWLQgg1\nLW/aTQAAAACAZUAig1/P/P75kw65+MNFFrZb/dTbLtkghLBw5oc3Xf3vlyd8WpzTdvUea+82\nctTG3YtCCCGVfPrWS+5++o3pxYk1+m9+yOiDelT8fHxNy5t2k8Ukk8mZM2c2eefQVHyriJbL\nV+lpuXyriJbLV+lpoUx6lwadO/850yUQqWnTnsh0CZEy6W0p0nyVPpPB6LJBMLqUM0ek5RKM\n0nKZI9JyCUZpoUx6lwaCUTJFMJopJr0txVJ6jVEAAAAAgIwQjAIAAAAA0RGMAgAAAADREYwC\nAAAAANERjAIAAAAA0RGMAgAAAADREYwCAAAAANERjAIAAAAA0RGMAgAAAADREYwCAAAAANER\njAIAAAAA0RGMAgAAAADREYwCAAAAANERjAIAAAAA0RGMAgAAAADREYwCAAAAANERjAIAAAAA\n0RGMAgAAAADREYwCAAAAANERjAIAAAAA0RGMAgAAAADREYwCAAAAANERjAIAAAAA0RGMAgAA\nAADREYwCAAAAANERjAIAAAAA0RGMAgAAAADREYwCAAAAANERjAIAAAAA0RGMAgAAAADREYwC\nAAAAANERjAIAAAAA0RGMAgAAAADREYwCAAAAANERjAIAAAAA0RGMAgAAAADREYwCAAAAANER\njAIAAAAA0RGMAgAAAADREYwCAAAAANERjAIAAAAA0RGMAgAAAADREYwCAAAAANERjAIAAAAA\n0RGMAgAAAADREYwCAAAAANERjAIAAAAA0RGMAgAAAADREYwCAAAAANERjAIAAAAA0RGMAgAA\nAADREYwCAAAAANERjAIAAAAA0RGMAgAAAADREYwCAAAAANERjAIAAAAA0RGMAgAAAADREYwC\nAAAAANERjAIAAAAA0RGMAgAAAADREYwCAAAAANERjAIAAAAA0RGMAgAAAADREYwCAAAAANER\njAIAAAAA0RGMAgAAAADREYwCAAAAANERjAIAAAAA0RGMAgAAAADREYwCAAAAANERjAIAAAAA\n0RGMAgAAAADREYwCAAAAANERjAIAAAAA0RGMAgAAAADREYwCAAAAANERjAIAAAAA0RGMAgAA\nAADREYwCAAAAANERjAIAAAAA0RGMAgAAAADREYwCAAAAANERjAIAAAAA0RGMAgAAAADREYwC\nAAAAANERjAIAAAAA0RGMAgAAAADREYwCAAAAANERjAIAAAAA0RGMAgAAAADREYwCAAAAANER\njAIAAAAA0RGMAgAAAADREYwCAAAAANERjAIAAAAA0RGMAgAAAADREYwCAAAAANERjAIAAAAA\n0RGMAgAAAADREYwCAAAAANERjAIAAAAA0RGMAgAAAADREYwCAAAAANERjAIAAAAA0RGMAgAA\nAADREYwCAAAAANERjAIAAAAA0RGMAgAAAADREYwCAAAAANERjAIAAAAA0RGMAgAAAADREYwC\nAAAAANERjAIAAAAA0RGMAgAAAADREYwCAAAAANERjAIAAAAA0RGMAgAAAADREYwCAAAAANER\njAIAAAAA0RGMAgAAAADREYwCAAAAANERjAIAAAAA0RGMAgAAAADREYwCAAAAANERjAIAAAAA\n0RGMAgAAAADREYwCAAAAANERjAIAAAAA0RGMAgAAAADREYwCAAAAANERjAIAAAAA0RGMAgAA\nAADREYwCAAAAANERjAIAAAAA0RGMAgAAAADREYwCAAAAANERjAIAAAAA0RGMAgAAAADREYwC\nAAAAANERjAIAAAAA0RGMAgAAAADREYwCAAAAANERjAIAAAAA0RGMAgAAAADREYwCAAAAANER\njAIAAAAA0RGMAgAAAADREYwCAAAAANERjAIAAAAA0RGMAgAAAADREYwCAAAAANERjAIAAAAA\n0RGMAgAAAADREYwCAAAAANERjAIAAAAA0RGMAgAAAADREYwCAAAAANFJpFKpTNfQsiWTyfLy\n8kxXQTq5ubnBK0ULlJWVlZ2dHUIoLS3NdC1QP9nZ2VlZWalUqqysLNO1QP3k5OQkEony8vJk\nMpnpWqB+THozLjd3k0yXQKRKS1/NdAmRMultEcrLy/Pz82t6NGdJlrKsWrhwYaZLoEaJRKJi\njlhaWupURcuSk5NTEYyWlJT4JxYtS35+fsUc0RBJi5OdnZ1IJJLJpKOXlsWkd2mQm5vpCoiV\nMStTTHpbhFQqJRhtXsXFxZkugRolEomioqIQQklJSUlJSabLgXrIy8srKCgIIRQXFwtGaVmy\n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\nVVI3iUSiY8eOIYS5c+eWlJRkuhyoh7y8vIr//c6YMSP9h/9haVNUVFRQUFBWVjZ7tk/t08K0\na9cuJyenuLh4/nw/vElLYtJLy2XSS8tl0ttSdOrUqaaHBKPVKGi/Zbe8qx5/ZeoWg1cKIZTO\ne+etuSVDtuxauUJhYWHl7WQyOXPmzAxUST2lUimjLC1L5RHr6KXFqXr0ZrYSaBgnXlouRy8t\njkkvLZdJ7zLAr9JXJ5E7ekjvz24447l3Pv3+y/evP/Wiom7bHLBiUabLAgAAAACahk+MVq/H\n3ucctvCSOy46dXpxYo3+m589+iA/Zw4AAAAAywzBaA0S2dsMH73N8EyXAQAAAAA0A1+lBwAA\nAACiIxgFAAAAAKIjGAUAAAAAoiMYBQAAAACiIxgFAAAAAKIjGAUAAAAAoiMYBQAAAACiIxgF\nAAAAAKIjGAUAAAAAoiMYBQAAAACiIxgFAAAAAKIjGAUAAAAAoiMYBQAAAACiIxgFAAAAAKIj\nGAUAAAAAoiMYBQAAAACiIxgFAAAAAKIjGAUAAAAAoiMYBQAAAACiIxgFAAAAAKIjGAUAAAAA\noiMYBQAAAACiIxgFAAAAAKIjGAUAAAAAoiMYBQAAAACiIxgFAAAAAKIjGAUAAAAAoiMYBQAA\nAACiIxgFAAAAAKIjGAUAAAAAoiMYBQAAAACiIxgFAAAAAKIjGAUAAAAAoiMYBQAAAACiIxgF\nAAAAAKIjGAUAAAAAoiMYBQAAAACiIxgFAAAAAKIjGAUAAAAAoiMYBQAAAACiIxgFAAAAAKIj\nGAUAAAAAoiMYBQAAAACiIxgFAAAAAKIjGAUAAAAAoiMYBQAAAACiIxgFAAAAAKIjGAUAAAAA\noiMYBQAAAACiIxgFAAAAAKIjGAUAAAAAoiMYBQAAAACiIxgFAAAAAKIjGAUAAAAAoiMYBQAA\nAACiIxgFAAAAAKIjGAUAAAAAoiMYBQAAAACiIxgFAAAAAKIjGAUAAAAAoiMYBQAAAACiIxgF\nAAAAAKIjGAUAAAAAoiMYBQAAAACiIxgFAAAAAKIjGAUAAAAAoiMYBQAAAACiIxgFAAAAAKIj\nGAUAAAAAoiMYBQAAAACiIxgFAAAAAKIjGAUAAAAAopNIpVKZrqFlSyaTM2fOzHQV1Ki8vPzz\nzz8PIay44oqtW7fOdDlQD/Pnz588eXIIoUePHllZ/o9FSzJt2rQZM2YUFBSsvPLKma4F6mfS\npEnFxcUdO3bs3LlzpmuBekgmk1988UUIoVu3bkVFRZkuB+ph3rx533//fQhhzTXXTCQSmS4H\n6mHq1KkzZ85s1apV9+7dM10L6aSZ1wlGWcbNnTt3yy23DCFcdNFFm222WabLgXoYN27cscce\nG0J44YUX/IVDy3LRRRfdcccdvXv3vv322zNdC9TPfvvt9+mnnw4dOvToo4/OdC1QD3PmzBk0\naFAw6aUFev7554877rgQwvjx4wsLCzNdDtTDhRdeeOedd/bp0+e2227LdC00kI8gAQAAAADR\nEYwCAAAAANERjAIAAAAA0XGNUZZxZWVl48aNCyH079+/S5cumS4H6mHKlCnvvfdeCGGLLbbI\nycnJdDlQD59++umkSZPatm274YYbZroWqJ/XX3997ty5K6+8cs+ePTNdC9RDaWnpCy+8EEx6\naYEqJ71bbrlldnZ2psuBejDpXQYIRgEAAACA6PgqPQAAAAAQHcEoAAAAABAdF61bprx93PAz\nP5m5+PKHH364ZM47B404q9XA0VcfPbBy+ZRXLz/o788MGXvzAWt3ePGwof/8bu7i2yYSeQ89\ndO/75x405rWfqizMLurYdb2BOx4+YvuCrETl8lRyzoF7DZtRWn7Mbfds0S6/1oKvGbHXG6uO\nueGM/jWtUFODdaknlVr40oN3PDbu1a8mTy1L5C/ffY1NBu287w4b5SRq6av0Nb8z5sAz3p9e\neTevoM0qa60/9NBD/rB8q/Q1p5Jznv7PbU+Nf3vSlJmp3Dar9h6w89CRA9dsV/HoFcP3mtDr\n1OtOXqdy/S+evHL0v57a4uB/HLVD71o7JP3ONmZ/W6LmO66ar5/Tb3jW0CHvlq5w+e2XrJT3\n20WXJl51+OlvbnD3jSOmvfv3kWe8eurt96zfJq/qXh6/z5BZ65167XED0jeeprtSybkvPHj3\nk+Pf+Or7acnswhVW6zVwm132GNSv4l9q6d8LUR1yzcQZ0hmSukjzTknzyqaZ9hzbLT/NjCj9\n0VLH+RKkkX7Qr7ibfoCuSyPOe82kweNgaIqhMF3jzTDup//78Z6/7vNw69G3XbJB1YfePOqA\nC+ftfNf1e4YQvrzz6NH3zX/g3mubavcX1xIn2CHtUbRUvXMb2UVpRsxv7jnx+DsmHnjZ7buu\n0qZyhfLSqccMHTVrzWE3j901TVXp58/NN3kODX0fRXXSWGoJRpc1Be0HnXb81osvz2v7h3MO\n3eSIKy64Z6d+e/ZoF0JIFn95+kXPdRt07AFrdwgh9Dv61HMXloUQUsm5Y049r9ehJw3v3iaE\nkEj8corOa7P+GSftXnE7lSyZ9N5z19577XdZa1484refJpj50bUzyxKdc7Pvu/ebLUY2wU8W\npGkwfT2p5OzrT/nb45/lbrvbjrv1WjW7dO7XH7z+wA3nvjhh+DVjdk+k7ata5bcbePoJg0MI\nIZTP+unLR2++feyRP9z873+0yU7UVHOq/Ocrjzt83JROu+01dL+VO8yfMeXdFx644PhDF1x5\n/bYrFi7+FF8+c9Xofz215cHnH7lDr1o7pC4725j9XfY07Lhq7n5Ov2Gy+JszL37huhMGLf5Q\np3VGtct+7Y4nJq+/52qVCxdMeWDiz6VDD+jZ4KrKS368YPToV38q+vNuO+3Wc+Xs5NxPJ7x8\n3+Wnjntz/8uO3zM7EUJt7wWHXHNzhnSGpFY1vbJppj0r5WWlnxGlP1rqMl+C9NIM+qFuA3St\njQTnvWbTgHEwNNFQWGPjzTPu1/r3Y9011UxgcS1xgh1qPooa9qTNpPFdVNOIedGwMzd9Ytgd\nZ16z/Q3H5v3aJ+/fdNbXZW3GjtmxMTU36+S51v2tSTwnjaWWYHRZk5XbZe211672oe7bHL/P\n0yPuPv2CbW89q1124tFzz5lW0P/aI/5U8Wi7NXtX/GchlZwZQmizRp+1e7b/Xcs5Hau2vE7/\nPyx88e27nn8iVJnov3LDhMLlhxzS7bnzn7klNXJs4z8akabB9PW8e/0pj3/e+oxrLuzfqaBi\nhfU3GTho424jxtx83WdbHbxmu5C2r9L73YZr9+vfY9bQ/7v/nqkL/tK1sKaaP7l1zLPftf/H\nTf/sWZRbsd3ALbfOP2j/W897YtvLd1+k/W+eu2b05U8MGvXPv22/6B9R1TZel51tzP4uexp2\nXDV3P6ffcLk/bTbl5Uvv/HS9fXu2W+ShRE6Hg/t2vPThe8Oex1Uu/Oo/z+QW9tmza2GDq3r+\n72Ne+2m5c6/7R592v/wTeL0N/7T9wMcPOvGasx/f+Iwdui/quuwhAAAbtklEQVTa7GLvBYdc\nc3OGrEuHOENGrqZXNv20p5YZUdqjpS7zJUgvzaAf6jZA19pIcN5rNg0YB0MTDYU1Nd5M436t\nfz/WXVPNBBbXEifYi7Zc5SjqvzS9cxvfRTWNmIkRfzv8rOEHHHHtuY/vecYOq4QQFs589ZzH\nJ/UbeWnfwkZFWM06ea51f2sSz0ljqeUao1FJ7HnGmE4LPzjlurenvnnVjRNmH3jusR2yG55e\nLl+Yk8gqqrybXDjp5q/nrHnAVr2HbVAy//17f/q5keXWt8HKelLJmRc+8e1ao06ufBtX6LjO\nvmecfNJGudk1NNBAuW2XDyHMLEvWWHOq9KJHv15j6LGV56wQQkjk7DP6oN0HLXrBgW/HXX/0\npf/d8pBqRvpqG1/CO7sMaNhxlfF+brvGkNGbLX/fGefPSqYWf7T/X/+4cPaLz85a+OuC1O0v\n/9R18wMbfIovWzDxirenrXfUiZWTtgrtem9/4mYrvH/bFdVuVfW9QHNzhlzkIWdIllqLzJeg\nVmkG/boP0OlnDiwxtY+DoWmGwpoabwFDYRPNBBqgRUyww1I8x27yLqocMVt33+GkbVeacOOZ\nnxUnQwj3n/2vrE6bn7Ljqo2pdtmZPIfoTxpNzSdGlzXlpVM//vjjqkuycjv16rFcxe2cwp5n\nj976oL+PPfmZ0HPIWdt3b92wZ0mVFk/68KVrJs3d5IjtKxdOefW60lTuyA27tMkd1jn3yadv\n/WTP49Zt8I7Uq8FF6lkw/bG5yfKdN+qy+Jp/2HiTytvp+6puUnOmfnXfJXclsot27VxYU80L\nZ7/wY0ly+z8tv8jG7fpstXuf3y357sUbj7z4kY7rHf+3wdWM9NU2XsedbaL9XRY07LhaAv1c\n64Z/+r8zH9j/8FOvf+fyUestsm2blYetXvDYg/d9s9XIniGE4mmPfDC/9NB9Vm1wVfMnP5BM\npfb9Q+fFH+q597ql4x773/zS3y9e9L3QgCelXpwhF+EMSbWa45Wte5vVzpegLmoa9OsyQA/4\n9e/kNDOH4Ly3JNRpHAwhNMlQWFPjS3DcX1Sy+NuPP/7d35vfFlcT7TXVTKBaLW6CPaBqzhXC\nIkfRrKXsnduEXbT4iLn+qDN7vjjqH/987vydv7zri3mj/jUqr3HfSG3uyXNoglcn9pNGpghG\nlzXFs5474YTnqi5p1Xn3yiu1hxC6bDiie/4z3y4MR+3RZ9GN07c886mdd36q6pI+u59y1KAV\nKu/+97bPWnfff5X87BAKD+zV/qI3rl+YuiI/0fCzV/oG09STXDg5hNC1ylW0T913yIT5JRW3\ni7qOvPPaXUId+qomC6bdv/PO91fezS5YYZ9jz12jILummpMLvwshrJRXy3/O5n79n6Pe+nyr\n7VZ76ul/vTZjvY07FiyyQg2N12lnG7O/y5iGHVdzv232fq51w6y8FcacsO3Is8Y+sdPtf17k\nwjGJ3IMGLn/6M7elRp6dCOGb+57Ma7PR4A6/HUL1rWrBT/MSicSqBdX8PzCncNUQwrcLk93S\nvhca8KTUizNkXTrEGZLmeGXTt1nrfAnqoqZBvy4DdGWwkm7m4LzXbOo7DuYnEk0yFNbcePOO\n+2nM+/7mE05YdGHhYrFJU80EqtXiJtgV79+ajqK3l7Z3buO6KP2ImZXT+cRTdhox5oox72Wt\nOOj47bs19rsXzT15rnV/a+KkkXGC0WVNYZe977phaJoV3rlxzOTUiuu2nXL+Offfcu5edW/5\n91cjLp70v6euvf+8e7e+bchKrUMIJXPfemjagl4jV540aVIIof3W3ZMf/O/mr+aOWr1tw3ak\n1gbT1JOdv1IIYeLPpavk//JmHnnamfOSqRDC5Ccvu/mTX56i1r6qSZWrI4ecgjbdVu7eJi8r\nTc3DOywfQvi+pHyRdlLJOd9OntW+W/e22YkQwoKpnw87/fI9+rdNvT/8khOvvvmaIwuqxMo1\nNX5A6zrtbGP2d1nS4ONq+7odVKER/VyXDTuvd8iItV+76ZQrt7jh2EUeWmPoziVPX/XA1AW7\nd2n17xd+WmnH0fVtvKqC5YpSqdSk4uTiU7fkgm9DCN3yskPN74WGPSl15wzpDEkdNccrm77N\n9PMlqLtqB/06DtDpG6ngvNdM6jsOjlq9bVZeY4fCNI0397ifRrvVT63uV+kXXa3xu59GS5xg\nh7Rz7KXtnduYLqp1xOyw9oiRvZ6/6cvcqw7dqJF1LoHJc637WxMnjYwTjMZlzhf3n/PoV1uf\nfN2wrq8P+9v1/3zmj8dt3a2O2y52NeL133t6z+cfmzxkVK8QwneP/zuVSk28/owjqmzy2g0T\nRo0d2LBSa20wTT2tOu3YJvs/Tz7zw3a//kDeqn36VtyYduvC0Gg1XWa4ppoPPnuLDjnXjH/p\np513WaXq+j+9+s8jzp8w9q771inMDSF0WffEPQZ0DiEcdO7Rr/3l3FNu2+qCYevU3vhZzbuz\ny5gGH1d7/HVp6eedxpz46AEnnXnPZ8N/v7yg4+A/trvx6X9/vv2w7/43r+TEHVdqzLO07rZL\nVuL1OydMP2mjRf+t//l9b+cW9l23de67y9Ylt1sWZ0hnSJZa6edLUC+LD/p1GaBrbYRmVd9x\ncNTYgfntGjsUpmm8ucf9xmv87jfe0jPBrrjbgubYjemiuoyYPVdrnT15+a61fTSyVsvS5NlJ\no8n58aWIlJdOOe+UOzr0O/DwjZZrs8pOJw9e+eV/nfzOnJIGN9irVU7xD8UVt+94+Ns2q4x4\nuIoT1u088+NrZ5Y18HLvDWiwsp5EdrvRW3b76u6xb00trrrC3K+evvLTWQ2rpzE1zyovOGbr\nbl/8+58T51bp7VTykVs/K+i0VcU5K4SQyPnl/ZjfYcOxB2/w2X2nP/rN3NobT7XNyM62UA0+\nrjJ1UC0up7D3WYds+NGdp702Y9FhaZ/dVv7plRu/vP/xgg7bbdo2r9rN6/wsfQ8d0Omti8//\nZO7vThGzP3vivOe+7z/isMZd4YfGcoZ0hqQFqTpfgnpZfNBvwACdZubAkpRm7E5ktWrkUJiu\n8aVmEluTxu9+45lgN0YTdlHzjZjL0uTZSaPJ+cTosmbxK+CGEDqs0atrXtZzl5wysbTLBWN2\nqli4/kHn9Htx5IUn3XjLFYfkNOgcnJ+VWDhtZgiheNojb8wtGXTyllUf7X/wVuWH3n3thzNO\n6N8pTSOl8yZ9/PHvzp49evdJTm9Ig5X1hBDWPXzsZl8eMfbQw7feZXDfHqu3Tcz76tP/PfLE\nJ4MHd3v67V/WT9NXte774tJ3wvEHn/PHDw8/ZdSxu+y18zprdC2d++Or/7372SnlB15wYLWt\nrTL45D2fHXbzyedvcsuZnXKyamm8Djvb5Pu7lGuO46ouB1VoRD/XfcNu25yw48MH3P/6lFa/\nv3T7itsNL7/l1LGPhVX/eny9Gq+2u7Yec/Y7Rx970kFH7jBk5wFrrpSc89PnE9995PGXOm96\n4Jjtuqffl/ruETVxhqy2NWdIFlHtOyU3EULzvLL1bbPquw/qa/FBvwEDdLUzB+e9JanWP5f6\nNWIoLJr1WPrGl/y4X1+N2f1OOekqNMFeAhrcRYtrkhFz8Z5fqcvnS2DyHJr01XHSWJIEo8ua\nxa+AG0LY4do79/j+zste/HHrE6+v/F2URHa7Y8/ad9gxt55+36CxQ+r6u35VrdqzzbxXbvnf\n/D9m3/54dsHKo/q0r/po62779W/9wPs3vBIu2ylNI7M+vW6Ra3Jff9+DPzWowcp6BhTlJrI7\nHHXhVf3uveO/4x5/4YGZWa3a9RywySnXXNy9/JWpC/Mr1q+pr0Z1bch1nT9LW3Pisp1GX3rF\no7ff+vRjtz40bU5WQdtVe607+vwDN+tR0zVYE/ucNWb8sJPGXDb+6mO2qLXxWne2yfd3Kdc8\nx1XtB1VoRD/XZ8OsYWf937N/OW+R/2/mFvXbc/nC//y0YPiWi/7KR/rGq+2u5fK6nXjZ1c/d\nd/fTL9z39F3TE0WdVlpplT2OOHuPrfrV8T8pUR1yzcQZsob2nCH5nepPYrlZoXle2fq2WfXd\n1+AnJWKLDvrZDRmgq5k5OO8tSemHqnDZTomcDg0eCg/Pqq3xJT7u11djdv/qY7ZI07IJ9hLQ\n4C5aXJOMmIv3/JEDuy6ByXNo0lfHSWNJSqRSDfymMwAAAABAC9XyPuMKAAAAANBIvkpP85r/\nwy1nX7rohScqFHTY7owTtqz2oQxqcQXTIjiuWGY4mAEgHkv5uL+Ul0eTa4mveEusOTa+Sg8A\nAAAARMdX6QEAAACA6AhGAQAAAIDoCEYBAAAAgOgIRgEAAACA6AhGAQBoiLtP2bd7l9ade/wl\n04X8IpWcvXPXNld/Nae5n6hvUd6Km/y3uZ+laZ22Srs2KxzUyEbKfn5/5barvDy7pElKAgDI\nOMEoAAD1Nv/H6/YZe1fOnw694MyhjWxqyuun7LTTTq/MaWzc9vLp273d+++HrNa2ke0sk7Jy\ncrJzGjvzzylc556/dd5r18uapCQAgIxLpFKpTNcAAEALM+39Xbv0e2jspDknd2/TyKa+fmir\n1XZ97r5pP+/eqVWDGymZ+8ZyHTc57YtZx6zc2Hpq1bcob2a/h75/dXBzP9FSqGzBxA5t+p7w\n/rRT+nTIdC0AAI3lE6MAANRbqrw8hJCflchsGeVls5IhhBAmjD2opN2Oi6eiqWRJ0scAmk5O\nq94XrtflihF3Z7oQAIAmIBgFAIjIxw9fuesWf+jcrignr9UKa/QbfvxlM8p+Cw7LS6ddeeJf\n+q3RtSA3t22n7lvt/bfXphUv3siDfbssN+CREMKxK7Up6rJnXVoOIfzw8r/32mb9Tm0KCtt1\n2Xjw0HvenBpCOHe19qvt+lwIYY/OhW27H1+x5k+v/2fo4E26tG+dV9Su5wZbn3XzuKrt3NSr\nU4c1Ll446439t1irdX7HeclUCOG4qz/pceAplesUZmdtevWEK47csXNRYW52XpfufYcdf+W0\n0vK6d0W11VYjVXLhPn2ysvNH3/lxnZp96Za9t99spfaFXVbqe9gFj3/90FaJROLHKoXN+2b8\nUftst3KX9vlFHXuvO+jMax4vX/Qpa5Tm5Tt3tfYV1xhNJWcnqrPHx9PrWMBOF/xxylvHfLqg\nrM51AQAspXyVHgAgFt8+dviqO13Vttfmf91jy455ZR+9fP/tT3245tBHP719h4oVLtpmpWOf\n/XHLvQ/eol/3OZPeuvq6B1PL7TRz8oO5v/9g6JSXnx/33sl7H/baQbc/sNeKq2695YBaW/7x\npXN6bHF6qvMGw/bfbrnsGfffcP1Hcwqv/eSrQd++9eKzo4ef9b9T/vPwFsv12mrznlPfuqDH\nJicsyO+x3/BdV2+z4MWHbntm4qytTxn39NmbVzR1U69ORxUfNjhx5fSBB+ywcZ/DDjukbOqt\nRcsPP/jD6des1bFincLsrPw+XWd/NHWbPYdtuGb798bf+/CLk7r+6fjvXvxHdh26oqZqR67W\nNlT9Kn2q7NIDBhx956d/u+XdS/bvW2uzM967dLX1jkkuv+mI/bfOn/nZbTfdVdi37Tf/m/lD\nSbJrblYIYf73D/bvsdekRLehBw7p0Tl7wrh77nnhywHDbnr3lhF1eX3TvHznrtb+vOI95/5w\nXUiV3nLrHVW3uv34w56dlrzyu+mHrlBUlwIWznqmoMM2Q176/p4/rlD3Yw8AYGmUAgAgDrf0\n7ZxTsPI3xWWVS47u1qZVp50qbpf+/ElWIrHy4PsqH33luE07d+5815SfF29qyv92CiFc8N3c\nurScKl+4dYeCVp3+/PG8kooFC6aP65ib1XXjO1Op1FcPDgoh3Det4lnK91quMLewz/gf5les\nmSydOnrdzomsgvGzF1YsubFnx0Qisd3lb1c+19cPbR1CmPBr46lUqlVWIoTwt3s+/rWA0hsP\nWTuEMGLc5NoLTlttKpVaqzB3hY0fT5WXXjF8nUQi9/9ueb+OPXxgt9b5bTeaOL+04u7Ut65I\nJBIhhB9KkhVLzujbKbewzyvTFlRu/sAxA0II53wxa/GXYBHpX76xq7Zr3fWvi2/1xsW7hhB2\nveTNehXQtyh3zf3H11oSAMBSzlfpAQBiMeSlT376/qOV8ys+NBlS5fMXplKp5M8VdxNZrfIS\nYdbH97/17dyKJZuc//LUqVP37lL7byKlb3nu5IufmVm83vmX9i7KrVhS0HHzB6+64tSRnRdp\nZ8G0+/8z5edeB900sGthxZKsnM5j7hiRKi8+/cnvflsvkX/rqAGV975/bHJ2bpd+vzZeoWj5\nAy4d0vvX9XMOuPiBwuysJ096pdaC61JtKiSv/usGR9zy/io733PZsLXr0g/FMx65afK8tY66\nqldhTsWjndc7/JQqF0Ut+/nDsz+a0fvQWzbpVFC5cPvTLg0h3H3Vp9X1+u804OX78cXzBo5+\naM19r37gyPXrVcDW7QumvfZerSUBACzlcjJdAAAAS0hh+44z3nzilifGf/jpF99M+vrj9yZM\nnrWwoP0vj2bnd3/yvAN2PPn2DVe5c5W1N9p04403G7TdnkO27ZhT+y8spW95zmfPhxD+OGj5\nqpsMHHnowMXaKZ75RAhh9WGrVV3YuvuwEC744akfw56rVyzJaz1gudzf/sE/9/O52QUrL9JU\n+177Vb2bU9Bjh44F//3m+RCGpC+4LtVOfWf/w98KG7bPf/uJw16ZM3jTtnm19sOCafeHENbY\n63d1brVRl7O/mfPLvs/4bzKVev/CDRMXLtots9+fvVhXLaq+L9/PPz75p+1OK+w5/PVbD65v\nASvnZ5ctqD2rBQBYyglGAQBicd/orfa8+Plu6w7aacuNd/zjn0ef1X/ywdscMeW3FTY7/pYp\nI0568MFHx41/6eWnb77juouPOXrjBz94fpsqHyFsQMvlC8tDCHmJuvyEfTWXv08kckIIqSo/\nYZTIKqq6QlZeVigvXXyzRRbkJkKqfGGtBdel2lR54tzH3/9L+xuX2/D0vYdc++1TR9TabOVT\n/67GqqllVl4IYZ3jb/znoBUXWS2/3YBQB3V/+ZILv913gyHfZq897tWrO1TWUOcCylIhJPLq\nUhIAwNJMMAoAEIWSua/tffHz3be/+ptHD65ceFOVFUrnffLOh7M69V9vn4OP3efgY0MIH//3\n7LW2P+3IU9796KpNGtNy255/COHpl9+YFlZpW7nwuRMOvW16h5uuP7dqUwUdtgvhhq/+/XX4\nw3KVC+d9d1sIYfmtfvcRzqo6DOhQ9vQXZalQNWac9cndIWxXeTe58JtHphcX9du81oLrUu1y\n691+wjYrhXDatTvecPCj/zfmlT3Hbrp8+mYLOmwVwp1f3v9t6Nup8tGXX5/227533D47cVTZ\nrF7bbbdp5cKyBRPve3hC1/6FNe17pXq8fKmysTtt8ugP4bI3n9mkfX4DCpi4oDS/U79aSwIA\nWMq5xigAQBTKfp6YTKU6DlivcsnPP7xy4eS5lR/SnP/TVRtvvPFef3+3coVV198ghFA2v6yR\nLbdd5aT+rfNe/9uxXxUnK5aUzH512KXXPfrGb+lnKhVCCK0677F7l8KJ14x8dWrxL8vLZpw3\n9PpEVv5pO3avqYBuO/UoT857elZx1YXzf7zpuIc+//Ve+V3H7zo3Wb7FOZvXWnBdqk0kfplF\nj7jz/lUKci7eediMsvL0zRYuN3yXzq0+vODwLxf80p8z3r/u1C9/+4p6TkGPM9bq+Nltw5/9\n8efKhXcevsu+++47qQ5z9rq/fE+cvMXpT0/e7+pXD1+3U9XldS0gVfLEjOIVd+hTe00AAEu3\nRCpVzfeVAABY1pQXb7Ncx+fntjvk5GPXW6nwyw9fu/7qh9fomnz12+yLb7525L5DClNztl1h\nhWenp/489MCN+65ePuvrB6+/8YPZhbd++fV+K7X+4aXdeg5+ZpUdH/vgzs1CCFMn7LzcgEcu\n+G7u6G6ta225KCvxzUNHr7nbpXkrbnrg/tt1zZ31wHVXvzs958oPvzmkZ/vJz/15pa2e3Pa0\ny4b32XC/fTaa8vrf1/jjmJLC3sNH7rZa6wUv3H/Tkx/NHDTm2WfPGVSxHzf16nTYlHUXzHym\ncs9K5rxS0P5Pu7ww+YGBK1QsKczOylrhDyU/vr/tvn/ZsEe7CeP+c/+4r5bb8MhvX7skL1F7\nV0x75Jiaqg0h9C3Km9nvoe9fHVzxXBOv3bnPqEc2GPPiG2etn77ZBf+7tPfGxy5cYeBBw7fN\nn/XZrdfdtWH/1g++PnV2WXnb7EQIYd6k//TtOfSH7O677bPzemt2/OC5u297+qN1Rtz23k37\n1/ryppKz07x8567W/rziPef+cN3Ut8csv8F5RSvtcvV5Q6pu3rr71rtstnxdCvj5pxuLuo48\n8uPpl/Tu2JjjEQAg85r/h+8BAFgqzJv0zPA/b9StU1HbrqtvscP+j3w4Y+pb56/aoTCv9f+3\nd7ehVZUBHMDv29zdzbtXpS3DNpSZYuJGRs2N21aSA5Nh5co+GDoQkt5ZfYl0UVAgK4xCbGSk\n1SJpitmCyPqQfrOEqCyXrJi5SiNZLFqbpw+DNaS9SKvbur/ft+fhnnP+z3k+nT/3nju757fB\nIAj6ew/f03jj3Fm5sUg0WXR5qmFjxydnho899eHKUChU1nBoePjDsZtDodC2nr5JnjkIgq7O\nHatrFucmsrIvKaisa9x95PTw/MAvx1ZVlsajsZIlLcMz33306u0rrinKzYnFk/Mqa1t2fTB6\nFS+VF8bzb7hgaZvnJMvWdI4McyLhsoZDJw48XbVwTjyWVXjZgnUPPnN6YGjyt2KstEEQLEpk\nlVz7zp/XPj/QNC8vEsvd/33/hKf96dM3G2qXzUrklJRXPbXv+Hv1c8PRnNEL+fnLdzc1pIrz\nZ85IFF65tHrLi52/n5/s/o6zfU+W5s0sbgqCoKs99ZcPBSM7O2GAE7tTsXjpucFJxwIA+K/y\njVEAAKa9r1+rX9h08mzf8WQ0HAqFEtFI8er3T3bUpjvXaMHRox/PyCu/an5yZKptQdG9Z67r\nP/t2GmNdrIeuyDtQs/erPSvSHQQA4O/yjlEAAKa9srV7lsS67z/Sm+4g4whvrlteXbd1ZDzY\n//mWb85duvzu9EW6aL/++Nazp4a2P1eT7iAAAFPAv9IDADDtRWJFHa9vWHTHIzt7XommO8xY\ndjyaqni4tfqunE31FeG+b9tbH+8dSrbvvH7CA7s7VlVsODzOB7LzUr3d+6Ys6NjeWP9AZfPB\nlQXxf+FaAAD/ND+lBwDgf+KF9bdkt7y8sTR5Z+Pa/Ksfe755cboTXejg9uYn2vZ/0dU9mF24\ntOqm+7Zuu23Z7HSHmqzB/s9uXde6a29bQSyc7iwAAFNAMQoAAAAAZBzvGAUAAAAAMo5iFAAA\nAADIOIpRAAAAACDjKEYBAAAAgIyjGAUAAAAAMo5iFAAAAADIOIpRAAAAACDjKEYBAAAAgIyj\nGAUAAAAAMs4fdkqJrNWMEsMAAAAASUVORK5CYII="
     },
     "metadata": {
      "image/png": {
       "height": 900,
       "width": 900
      }
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#checking distribution of package types\n",
    "options(repr.plot.width = 15, repr.plot.height =15)\n",
    "ggplot(data, aes(x=as.factor(package_size), fill=as.factor(package_size) )) + \n",
    "  geom_bar( ) +\n",
    "  scale_fill_brewer(palette = \"Set1\") +\n",
    "  theme(legend.position=\"none\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "ba915120",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T22:20:05.409551Z",
     "iopub.status.busy": "2022-12-09T22:20:05.407514Z",
     "iopub.status.idle": "2022-12-09T22:20:41.323247Z",
     "shell.execute_reply": "2022-12-09T22:20:41.320884Z"
    },
    "papermill": {
     "duration": 35.93348,
     "end_time": "2022-12-09T22:20:41.327123",
     "exception": false,
     "start_time": "2022-12-09T22:20:05.393643",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "#factorizing categorical columns\n",
    "data$declared_handling_days <-as.factor(data$declared_handling_days)\n",
    "data$shipment_method_id<-as.factor(data$shipment_method_id)\n",
    "data$package_size<- as.factor(as.numeric(as.factor(data$package_size)))\n",
    "data$category_id <- as.factor(data$category_id)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "ff235399",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T22:20:41.352922Z",
     "iopub.status.busy": "2022-12-09T22:20:41.351434Z",
     "iopub.status.idle": "2022-12-09T22:22:45.008624Z",
     "shell.execute_reply": "2022-12-09T22:22:45.006994Z"
    },
    "papermill": {
     "duration": 123.672652,
     "end_time": "2022-12-09T22:22:45.011120",
     "exception": false,
     "start_time": "2022-12-09T22:20:41.338468",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "#adding new column with average estimate of delivery time by using max and min of the column\n",
    "\n",
    "data$carrier_average_estimate <-apply(data[,7:8],1,mean)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "224dbd51",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T22:22:45.038181Z",
     "iopub.status.busy": "2022-12-09T22:22:45.036722Z",
     "iopub.status.idle": "2022-12-09T22:22:45.049914Z",
     "shell.execute_reply": "2022-12-09T22:22:45.047912Z"
    },
    "papermill": {
     "duration": 0.029951,
     "end_time": "2022-12-09T22:22:45.053204",
     "exception": false,
     "start_time": "2022-12-09T22:22:45.023253",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "library(zipcodeR)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "3ddace22",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T22:22:45.078233Z",
     "iopub.status.busy": "2022-12-09T22:22:45.076819Z",
     "iopub.status.idle": "2022-12-09T22:23:35.081972Z",
     "shell.execute_reply": "2022-12-09T22:23:35.080337Z"
    },
    "papermill": {
     "duration": 50.021168,
     "end_time": "2022-12-09T22:23:35.085076",
     "exception": false,
     "start_time": "2022-12-09T22:22:45.063908",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "#adding new column measuring distance between item and buyer zipcodes\n",
    "zip_distance <- data.frame(zip_distance(data$item_zip,data$buyer_zip)) #creating df of distance\n",
    "\n",
    "#appending distance to data table\n",
    "data <- data %>%\n",
    "  add_column(Add_Column = zip_distance$distance)\n",
    "\n",
    "\n",
    "#renaming column to \"zip_distance\"\n",
    "names(data)[names(data) == \"Add_Column\"] = \"zip_distance\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "c7056159",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T22:23:35.111476Z",
     "iopub.status.busy": "2022-12-09T22:23:35.110023Z",
     "iopub.status.idle": "2022-12-09T22:24:05.194571Z",
     "shell.execute_reply": "2022-12-09T22:24:05.192790Z"
    },
    "papermill": {
     "duration": 30.099962,
     "end_time": "2022-12-09T22:24:05.197625",
     "exception": false,
     "start_time": "2022-12-09T22:23:35.097663",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "#adding date columns for each attribute \n",
    "data$acceptance_date <-as.Date(data$acceptance_scan_timestamp)\n",
    "data$payment_date <-as.Date(data$payment_datetime)\n",
    "data$delivery_date <-as.Date(data$delivery_date)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "dba40576",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T22:24:05.223493Z",
     "iopub.status.busy": "2022-12-09T22:24:05.222034Z",
     "iopub.status.idle": "2022-12-09T22:24:05.237999Z",
     "shell.execute_reply": "2022-12-09T22:24:05.236473Z"
    },
    "papermill": {
     "duration": 0.030578,
     "end_time": "2022-12-09T22:24:05.240122",
     "exception": false,
     "start_time": "2022-12-09T22:24:05.209544",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Time difference of 5 days"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#adding columns for total days from time of order to delivery\n",
    "data$delivery_date[1]-data$payment_date[1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "1f6de286",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T22:24:05.265148Z",
     "iopub.status.busy": "2022-12-09T22:24:05.263665Z",
     "iopub.status.idle": "2022-12-09T22:24:05.275251Z",
     "shell.execute_reply": "2022-12-09T22:24:05.273573Z"
    },
    "papermill": {
     "duration": 0.026611,
     "end_time": "2022-12-09T22:24:05.277411",
     "exception": false,
     "start_time": "2022-12-09T22:24:05.250800",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "# data$acceptance_date <-as.Date(data$acceptance_scan_timestamp)\n",
    "# data$payment_date <-as.Date(data$payment_datetime)\n",
    "# data$delivery_date <-as.Date(data$delivery_date)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "ac76c658",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T22:24:05.302061Z",
     "iopub.status.busy": "2022-12-09T22:24:05.300521Z",
     "iopub.status.idle": "2022-12-09T22:24:17.197938Z",
     "shell.execute_reply": "2022-12-09T22:24:17.195676Z"
    },
    "papermill": {
     "duration": 11.913595,
     "end_time": "2022-12-09T22:24:17.201666",
     "exception": false,
     "start_time": "2022-12-09T22:24:05.288071",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "#calculating days to process order\n",
    "\n",
    "time_to_process= data.frame(data$acceptance_date-data$payment_date)\n",
    "# appending days_to_deliver to data table\n",
    "data <- data %>%\n",
    "  add_column(Add_Column = time_to_process$data.acceptance_date...data.payment_date)\n",
    "\n",
    "# renaming column\n",
    "names(data)[names(data) == \"Add_Column\"] = \"time_to_process\"\n",
    "# converting to numeric\n",
    "data$time_to_process <-as.numeric(as.character(data$time_to_process))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "eff6e9db",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T22:24:17.227178Z",
     "iopub.status.busy": "2022-12-09T22:24:17.225684Z",
     "iopub.status.idle": "2022-12-09T22:24:17.237486Z",
     "shell.execute_reply": "2022-12-09T22:24:17.235666Z"
    },
    "papermill": {
     "duration": 0.027944,
     "end_time": "2022-12-09T22:24:17.240685",
     "exception": false,
     "start_time": "2022-12-09T22:24:17.212741",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "# #calculating days from acceptance to delivery\n",
    "# time_to_process= data.frame(data$acceptance_date-data$payment_date)\n",
    "# # appending days_to_deliver to data table\n",
    "# data <- data %>%\n",
    "#   add_column(Add_Column = time_to_process$data.acceptance_date...data.payment_date)\n",
    "\n",
    "# # renaming column\n",
    "# names(data)[names(data) == \"Add_Column\"] = \"time_to_process\"\n",
    "# # converting to numeric\n",
    "# data$time_to_process <-as.numeric(as.character(data$time_to_process))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "764995eb",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T22:24:17.267443Z",
     "iopub.status.busy": "2022-12-09T22:24:17.265622Z",
     "iopub.status.idle": "2022-12-09T22:24:27.000241Z",
     "shell.execute_reply": "2022-12-09T22:24:26.998605Z"
    },
    "papermill": {
     "duration": 9.751073,
     "end_time": "2022-12-09T22:24:27.003351",
     "exception": false,
     "start_time": "2022-12-09T22:24:17.252278",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "#calculating days from acceptance to delivery\n",
    "data1= data.frame(data$delivery_date-data$acceptance_date)\n",
    "# appending days_to_deliver to data table\n",
    "data <- data %>%\n",
    "  add_column(Add_Column = data1$data.delivery_date...data.acceptance_date)\n",
    "\n",
    "# # renaming column\n",
    "names(data)[names(data) == \"Add_Column\"] = \"acceptance_to_delivery\"\n",
    "# # converting to numeric\n",
    "data$acceptance_to_delivery <-as.numeric(as.character(data$acceptance_to_delivery))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "e4f1f7e2",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T22:24:27.028039Z",
     "iopub.status.busy": "2022-12-09T22:24:27.026623Z",
     "iopub.status.idle": "2022-12-09T22:24:36.895247Z",
     "shell.execute_reply": "2022-12-09T22:24:36.893518Z"
    },
    "papermill": {
     "duration": 9.884402,
     "end_time": "2022-12-09T22:24:36.898335",
     "exception": false,
     "start_time": "2022-12-09T22:24:27.013933",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "#calculating days to delivery\n",
    "date= data.frame(data$delivery_date-data$payment_date)\n",
    "# appending days_to_deliver to data table\n",
    "data <- data %>%\n",
    "  add_column(Add_Column = date$data.delivery_date...data.payment_date)\n",
    "\n",
    "# renaming column\n",
    "names(data)[names(data) == \"Add_Column\"] = \"days_to_deliver\"\n",
    "# converting to numeric\n",
    "data$days_to_deliver <-as.numeric(as.character(data$days_to_deliver))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "47690230",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-12-09T22:24:36.924344Z",
     "iopub.status.busy": "2022-12-09T22:24:36.922918Z",
     "iopub.status.idle": "2022-12-09T22:24:36.933992Z",
     "shell.execute_reply": "2022-12-09T22:24:36.932510Z"
    },
    "papermill": {
     "duration": 0.027172,
     "end_time": "2022-12-09T22:24:36.936435",
     "exception": false,
     "start_time": "2022-12-09T22:24:36.909263",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "# library(caTools)\n",
    "\n",
    "# #make this example reproducible\n",
    "# set.seed(666)\n",
    "\n",
    "# #Use 70% of dataset as training set and remaining 30% as testing set\n",
    "# sample <- sample.split(train$days_to_deliver, SplitRatio = 0.7)\n",
    "# train_df  <- subset(train, sample == TRUE)\n",
    "# test_df   <- subset(train, sample == FALSE)"
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
   "duration": 702.877631,
   "end_time": "2022-12-09T22:24:37.774227",
   "environment_variables": {},
   "exception": null,
   "input_path": "__notebook__.ipynb",
   "output_path": "__notebook__.ipynb",
   "parameters": {},
   "start_time": "2022-12-09T22:12:54.896596",
   "version": "2.4.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
