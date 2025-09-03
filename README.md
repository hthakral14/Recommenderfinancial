Personalized Financial Recommender

Atplotlib is a hybrid financial recommendation system built in Python and Streamlit. It combines content-based filtering, collaborative filtering (SVD), and risk-adjusted recommendations to provide personalized asset suggestions for users based on transaction history, asset features, and risk profiles.

🚀 Features

Synthetic Data Generation: Simulate users, assets, and transaction history.

Content-Based Filtering: Compute user profiles using asset features like sector, volatility, and past returns.

Collaborative Filtering (SVD): Predict ratings for user-asset pairs using SVD.

Hybrid Recommendations: Combine CF and content-based scores for better personalization.

Risk Alignment: Adjust recommendations based on user risk tolerance and asset volatility.

Interactive Streamlit Demo: Explore recommendations through a user-friendly interface.

🗂 Project Structure
Recommenderfinancial/
├── data/                   # Generated synthetic datasets
├── src/
│   ├── data_pipeline.py    # Data generation & loading
│   ├── features.py         # Asset feature engineering
│   ├── content_model.py    # Content-based scoring
│   ├── cf_model.py         # Collaborative filtering (SVD)
│   ├── hybrid.py           # Hybrid scoring and risk adjustment
│   └── serve.py            # Main API for Streamlit app
├── streamlit_app.py        # Streamlit front-end
├── requirements.txt        # Python dependencies
└── README.md

⚡ Installation

Clone the repository:

git clone https://github.com/hthakral14/Recommenderfinancial.git
cd Recommenderfinancial


Create a virtual environment:

python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows


Install dependencies:

pip install -r requirements.txt

🖥 Usage

Run the Streamlit app:

streamlit run streamlit_app.py


Select a User ID from the dropdown.

Click Get Recommendations.

View top asset recommendations with asset ID, ticker, sector, and score.

🔧 How It Works

Data Generation: Generates synthetic datasets for users, assets, and transactions.

Feature Engineering: One-hot encodes categorical features (sector, market_cap) and standardizes numeric features (volatility, past_return).

Content-Based Filtering: Builds user profiles weighted by past transactions and calculates cosine similarity with assets.

Collaborative Filtering: Trains an SVD model on user-asset ratings to predict missing ratings.

Hybrid Recommendations: Combines normalized CF and content-based scores using a weight alpha=0.6.

Risk Alignment: Adjusts scores based on user risk tolerance vs asset volatility.

Recommendation Output: Returns top-K recommended assets for a user with scores.

📦 Dependencies

Python 3.8+

pandas

numpy

scikit-learn

scikit-surprise

streamlit

Install all dependencies:

pip install pandas numpy scikit-learn scikit-surprise streamlit

📈 Future Improvements

Integrate real financial datasets

Add time-series forecasting for returns

Optimize CF predictions for large datasets

Enhance risk modeling with portfolio constraints

📄 License

MIT License © 2025
