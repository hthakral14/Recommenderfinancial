Personalized Financial Recommender

A hybrid financial recommendation system demo built with Python and Streamlit, combining content-based filtering, collaborative filtering (SVD), and risk-adjusted recommendations. Generate personalized asset recommendations for users based on transaction history, asset characteristics, and risk profiles.

Features

User & Asset Simulation: Generates synthetic datasets of users, assets, and transactions.

Content-Based Filtering: Computes user profiles and asset similarity using asset features.

Collaborative Filtering (CF): Predicts user-asset ratings with SVD.

Hybrid Recommendations: Combines CF and content-based scores with risk alignment.

Interactive Demo: Built with Streamlit for easy exploration.

Installation

Clone the repository:

git clone https://github.com/yourusername/atplotlib.git
cd atplotlib


Create a virtual environment:

python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows


Install dependencies:

pip install -r requirements.txt

Usage

Run the Streamlit demo:

streamlit run streamlit_app.py


Select a user ID from the dropdown.

Click Get recommendations.

View top asset recommendations with asset_id, ticker, sector, and score.

Project Structure
atplotlib/
├── data/                   # Auto-generated synthetic datasets
├── src/
│   ├── data_pipeline.py    # Data generation and loading
│   ├── features.py         # Asset feature engineering
│   ├── content_model.py    # Content-based user profiles & scoring
│   ├── cf_model.py         # Collaborative filtering model (SVD)
│   ├── hybrid.py           # Hybrid scoring and risk adjustment
│   └── serve.py            # Main API for Streamlit app
├── streamlit_app.py        # Streamlit demo interface
├── requirements.txt        # Python dependencies
└── README.md

How it Works

Data Generation
Synthetic users, assets, and transaction history are generated if CSVs are not found.

Feature Engineering

One-hot encode categorical features: sector, market_cap

Standardize numeric features: volatility, past_return

Content-Based Filtering

Build user profiles as weighted averages of asset features based on transaction ratings or amounts

Compute cosine similarity between users and assets

Collaborative Filtering (SVD)

Train SVD model on user-asset ratings

Predict missing ratings

Hybrid Scoring

Normalize content and CF matrices

Combine scores with alpha weight (default 0.6)

Apply risk alignment: adjusts scores based on user risk tolerance vs asset volatility

Recommendation Output

Returns top-K recommended assets for a user with scores for ranking

Dependencies

Python 3.8+

pandas

numpy

scikit-learn

surprise

streamlit

Install all with:

pip install pandas numpy scikit-learn scikit-surprise streamlit

Example

Future Improvements

Real financial datasets integration

Add time-series forecasting for returns

Improve risk modeling with portfolio constraints

Optimize CF predictions for large datasets

License

MIT License © 2025