# 🏠 House Price Prediction App

A user-friendly Streamlit web app for predicting house prices using machine learning. Enter house features or upload a CSV for batch predictions. Built with scikit-learn, pandas, and Streamlit.

---

## 🌐 Deployment

You can deploy this app for free on [Render](https://render.com/) or [Streamlit Community Cloud](https://streamlit.io/cloud) by connecting your GitHub repo and following their deployment instructions.

- **Access the live app here:** [https://house-price-streamlit-app.onrender.com](https://house-price-streamlit-app.onrender.com)

## 🚀 Features

- **Single Prediction:** Enter house details in the sidebar to get an instant price estimate.
- **Batch Prediction:** Upload a CSV file with multiple houses for bulk predictions and download the results.
- **Interactive Visualizations:** View distribution of predicted prices for batch uploads.
- **Easy to Deploy:** Ready for Render or Streamlit Community Cloud.

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/)
- [scikit-learn](https://scikit-learn.org/)
- [pandas](https://pandas.pydata.org/)
- [numpy](https://numpy.org/)
- [matplotlib](https://matplotlib.org/)
- [joblib](https://joblib.readthedocs.io/)

---

## ⚡ Quick Start

1. **Clone the repository**
git clone https://github.com/AnshMahajan-grep/house-price-streamlit-app.git
cd house-price-streamlit-app


2. **Install dependencies**
pip install -r requirements.txt

3. **Run the app**
streamlit run app.py


4. **Open in your browser:**  
The app will open automatically. If not, go to [http://localhost:8501](http://localhost:8501).

---

## 📑 Usage

- **Single Prediction:**  
Fill in the house details in the sidebar and click "Predict Single House Price".

- **Batch Prediction:**  
Upload a CSV file with the required columns (see below for an example), and download the results with predicted prices.

### Example CSV Format

bedrooms,bathrooms,sqft_living,sqft_lot,floors,waterfront,view,condition,sqft_above,sqft_basement,house_age,has_been_renovated

3,2,1800,5000,1,0,0,3,1500,300,20,0

4,3,2500,7000,2,1,1,4,2000,500,10,1


---

## 📝 Model Training

- The model was trained on the [Kaggle House Prices dataset](https://www.kaggle.com/).
- All preprocessing and feature engineering steps are included in the pipeline (`models/pipeline.pkl`).

---

## 🌐 Deployment

You can deploy this app for free on [Render](https://render.com/) or [Streamlit Community Cloud](https://streamlit.io/cloud) by connecting your GitHub repo and following their deployment instructions.

---

## 🤝 Contributing

Pull requests and suggestions are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

This project is open source and available under the MIT LICENSE.

---

## 🙋‍♂️ Author

- [Your Name](https://github.com/AnshMahajan-grep)

---
