## Department-wide Sales Prediction and Holiday Markdown Effects

### Overview

This project focuses on predicting department-wide sales for each store for the upcoming year while also considering the impact of markdowns during holiday weeks. The goal is to provide valuable insights to assist in decision-making and offer recommended actions to maximize business impact.

![Screenshot (451)](https://github.com/Sukumar9944/Department-wide-Sales-Prediction-and-Holiday-Markdown-Effects/assets/132226144/e702677a-df77-43f1-8064-3799fa91d529)


### Table of Contents

1. [Introduction](#introduction)
2. [Data](#data)
3. [Methods](#methods)
4. [Results](#results)
5. [Recommendations](#recommendations)
6. [Usage](#usage)

---

### Introduction

In today's dynamic retail environment, accurately predicting sales and understanding the impact of promotions, especially during holiday weeks, is crucial for strategic planning. This project aims to address these challenges by developing a predictive model for department-wide sales and analyzing the effects of markdowns on holiday weeks.

---

### Data

The dataset used for this project includes historical sales data, markdown information, and holiday schedules for each store. The features used in the model include [Year, Store, Store_Type, Department, Temperature, Fuel_Price, CPI, Unemployment], and the target variable is the department-wide sales.

---

### Methods

#### Data Processing with PySpark and Databricks
The data processing and merging steps were efficiently handled using PySpark and Databricks. This allowed for scalable and distributed processing of large datasets, ensuring optimal performance. The key steps involved in data processing include:

1. Data Cleaning

2. Data Merging

#### Predictive Model

We employed Random forest regressor for the model, column transformer with one hot encoding and ordinal encoding to encode the categorical variables and GridSearch CV for Hyperparamter tuning and ML Flow to log the artifacts, hyperparamters and Evaluation metrics to build an accurate forecasting model. The model was trained on historical data, validated, and fine-tuned to ensure robust predictions.

#### Holiday Markdown Analysis

To understand the effects of markdowns during holiday weeks, we conducted Pearson's Correlation and Data Visualizations using Tablueau. This allowed us to identify patterns and correlations between markdowns and sales during holiday periods.

---

### Results

- The predictive model achieved a R2 score of 99% on Training data and 92% on Testing data.
- The analysis of holiday markdown effects revealed that the markdown has a Significant effect on Overall Sales. Detailed results can be found in
  https://public.tableau.com/views/EffectsOfMarkdown/Dashboard1?:language=en-US&:display_count=n&:origin=viz_share_link

---

### Recommendations

Based on the insights drawn from the model and holiday markdown analysis, the following actionable recommendations are provided:

1. **Prioritize Holiday Markdowns:** Focus on strategic markdowns during holiday weeks to maximize sales impact.
2. **Optimize Inventory:** Adjust inventory levels based on predicted sales to prevent overstock or stockouts.
3. **Focus on the Least Stores and Department which has very much low contribution on Overall Sales**
4. **To view more detailed insights : Go to this Link:**
   https://public.tableau.com/views/Insights-FinalProject/OverallSales?:language=en-US&:display_count=n&:origin=viz_share_link

---

### Usage

To use the predictive model and view the results, follow these steps:

1. Clone the repository.
2. Install the required dependencies (see requirements.txt).
3. Run app.py
