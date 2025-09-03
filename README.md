Personalized Financial Recommender

An interactive financial recommendation demo built with Streamlit, where users receive personalized asset suggestions based on transaction history, asset features, and risk profiles.

🧠 About the Project

This project demonstrates a hybrid recommendation system combining content-based filtering, collaborative filtering (SVD), and risk-adjusted recommendations. Users can:

🏦 Explore Recommendations: See top assets suggested for a selected user.

📊 Hybrid Scoring: Combines content similarity with collaborative filtering predictions.

⚖️ Risk Alignment: Adjusts scores according to user risk tolerance and asset volatility.

📈 Interactive UI: Easy-to-use Streamlit interface to select users and get recommendations.

🔧 Tech Stack

Frontend/UI: Streamlit

Languages: Python 3

Libraries & Tools:

pandas, numpy, scikit-learn

scikit-surprise (SVD for collaborative filtering)

Streamlit

📁 Folder Structure
Recommderfinancial/
├── streamlit_app.py          # Main Streamlit interface
├── requirements.txt          # Project dependencies
├── data/                     # Generated synthetic datasets
├── src/
│   ├── data_pipeline.py      # Data generation & loading
│   ├── features.py           # Asset feature engineering
│   ├── content_model.py      # Content-based user profiles & scoring
│   ├── cf_model.py           # Collaborative filtering (SVD)
│   ├── hybrid.py             # Hybrid scoring & risk adjustment
│   └── serve.py              # Main API for Streamlit app
└── README.md

🛠️ How to Run Locally

Clone the repository:

git clone https://github.com/hthakral14/Recommderfinancial.git
cd Recommderfinancial


Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows


Install dependencies:

pip install -r requirements.txt


Run the Streamlit app:

streamlit run streamlit_app.py


Select a User ID and click Get Recommendations to view top assets.

🚀 Features

Personalized recommendations for users

Hybrid scoring (content-based + collaborative filtering)

Risk-adjusted scores for safer investment suggestions

Interactive and lightweight Streamlit interface

Synthetic data generation for testing/demo purposes

🚀 Future Improvements

Integrate real financial datasets

Add time-series forecasting for asset returns

Optimize collaborative filtering for large-scale datasets

Include portfolio-based risk modeling

Deploy on Streamlit Cloud or Hugging Face Spaces

🤝 Contributing

Fork the repository

Create a new branch:

git checkout -b feature/YourFeature


Commit your changes:

git commit -m "Add YourFeature"


Push to your branch:

git push origin feature/YourFeature


Open a Pull Request

📄 License

This project is licensed under the MIT License.

👩‍💻 Author

Himanshi Thakral

GITHUB 
hthakral14
