# eBay Delivery Date Prediction

This repository contains code and data for predicting delivery dates for eBay shipments. The project aims to build a machine learning model to predict the delivery date of eBay shipments based on various attributes.

## Table of Contents

- [Introduction](#introduction)
- [Data Preprocessing](#data-preprocessing)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Feature Engineering](#feature-engineering)
- [Model Training](#model-training)
- [Model Evaluation](#model-evaluation)
- [Conclusion](#conclusion)

## Introduction

The goal of this project is to predict the delivery date of eBay shipments using machine learning techniques. The dataset contains information about various attributes such as seller ID, declared handling days, shipment method, shipping fee, item and buyer zip codes, category ID, item price, quantity, and more.

## Data Preprocessing

In this section, the raw data is loaded using R packages like `tidyverse` and `zipcodeR`. The dataset is cleaned by handling missing values, converting data types, and dropping irrelevant columns. Categorical columns are factorized for modeling purposes.

## Exploratory Data Analysis

This section explores the dataset's statistical summary, distributions, and relationships between variables using visualizations created with the `ggplot2` package. Insights are drawn from the data to better understand the relationships between attributes.

## Feature Engineering

New features are created based on the existing attributes, such as calculating the average estimate of delivery time and calculating the distance between item and buyer zip codes. Additional date-related columns are added to calculate time-related features.

## Model Training

Various machine learning models are trained on the preprocessed dataset, including XGBoost, glmnet, and rpart. The dataset is split into training and testing sets, and different models are evaluated for their predictive performance.

## Model Evaluation

The trained models are evaluated using evaluation metrics such as Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE). The model with the best performance is selected as the final model for delivery date prediction.

## Conclusion

The project successfully builds a machine learning model for predicting eBay delivery dates based on various attributes. The process involves data preprocessing, exploratory data analysis, feature engineering, model training, and evaluation. The model's performance is assessed using appropriate evaluation metrics, and the insights gained from this project can potentially improve delivery date predictions for eBay shipments.

For detailed implementation and code, refer to the provided R script files.

## Usage

1. Clone the repository: `git clone https://github.com/armana0007/eBay-delivery-prediction.git`
2. Install the required R packages using `install.packages()`.
3. Run the R scripts to reproduce the data preprocessing, exploratory analysis, and model training process.

