# House Price Prediction API

## 📌 What is this project?
This is a Flask-based API that predicts house prices using a pre-trained model. Given input features such as location, size, and number of rooms, the API returns an estimated house price.

## ⚙️ How to Use?

### 1️⃣ Installation
To set up the project, clone this repository and install dependencies:
```bash
# Clone the repo
git clone https://github.com/ashdev-7/house-price-api.git
cd house-price-api

# Install dependencies
pip install -r requirements.txt
```

### 2️⃣ Running the API
Run the Flask server with:
```bash
python server.py
```
By default, the API will be available at `http://127.0.0.1:5000/`.

### 3️⃣ Making Predictions
Send a POST request with house details to get the predicted price:
exmaple :
```bash
curl -X POST "http://127.0.0.1:5000/predict" -H "Content-Type: application/json" -d '{"sqft": 1500, "bedrooms": 3, "bathrooms": 2, "location": "New York"}'
```
Response:
```json
{
  "predicted_price": 350000
}
```

## 🤔 Why this project?
- Helps real estate agencies, buyers, and sellers get quick price estimates.
- Demonstrates how to build a simple yet functional ML-powered API with Flask.
- Provides a starting point for more advanced real estate prediction models.

---

