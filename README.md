# 🚦 Verkehrsunfälle Forecasting Application

This application forecasts the number of traffic accidents ("Verkehrsunfälle") for the city of Munich using time series forecasting (ARIMA). The model specifically predicts the number of alcohol-related accidents ("Alkoholunfälle") for any requested month.

---

## 📂 Dataset

The dataset used for this model is:

**"Monatszahlen Verkehrsunfälle"**  
Source: München Open Data Portal

Dataset includes:
- Accident category
- Type (insgesamt = total)
- Year
- Month
- Number of accidents

The dataset contains data until the end of 2021, but only data until 2020 is used to train the model (as per project requirement).

---

## ⚙️ Technology Stack

- Python 3.x
- Flask (for API)
- pandas (data processing)
- statsmodels (ARIMA model)
- scikit-learn (metrics, optional)
- matplotlib (optional visualization)
- gunicorn (for deployment)

---

## 📊 Why ARIMA?

ARIMA (AutoRegressive Integrated Moving Average) is chosen because:

- The dataset is time-series based (monthly data).
- ARIMA handles trend and seasonality effectively.
- It requires limited data preprocessing.
- Suitable for small-to-medium sized datasets.
- No need for external features (purely univariate model).

---

## 🔨 Project Workflow (Steps done in code)

Here are the exact steps that have been implemented in the code:

1️⃣ **Loading Dataset**  
- The CSV file `monatszahlen2505_verkehrsunfaelle_06_06_25.csv` is loaded using pandas.

2️⃣ **Renaming Columns**  
- Columns are renamed to simpler names:  
  `MONATSZAHL ➔ Category`, `AUSPRAEGUNG ➔ Type`, `JAHR ➔ Year`, `MONAT ➔ Month`, `WERT ➔ Value`

3️⃣ **Data Cleaning**  
- Rows where `Month` column equals `'Summe'` are filtered out.
- Month values are converted to integers.
- Only records until `Year <= 2020` are kept for model training.

4️⃣ **Filtering Data**  
- Only data where:
  - `Category = Alkoholunfälle`
  - `Type = insgesamt`
- These rows are selected for forecasting.

5️⃣ **Creating DateTime Index**  
- A datetime index (`ds`) is created by combining `Year` and `Month` columns.
- The dataframe is sorted and reindexed by date.

6️⃣ **Visualizing Historical Data**  
- A plot is generated (using matplotlib) to visualize historical accident counts.  
- 📸 The generated graph is attached in the repository as `Historical_Visualization.jpeg`.

7️⃣ **ARIMA Model Training**  
- An ARIMA model is created with order (1,1,1).
- The model is fitted using the training data.

8️⃣ **Generating Forecast**  
- The trained model is used to forecast for the next 60 months after Dec 2020.

9️⃣ **Flask API Creation**  
- A Flask app is built with the following endpoints:
  - `/` (GET): Simple health check.
  - `/forecast` (POST): Accepts JSON input `{"year": YYYY, "month": MM}` and returns the forecast.

10️⃣ **API Output**  
- The API returns:
```json
{
  "prediction": value
}

