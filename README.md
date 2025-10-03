I. Title: IMDB Movie Review Sentiment Analysis

II. Description: This project classifies movie review sentiment (positive or negative) using a supervised machine learning approach. The model achieves a final accuracy of 87.91% and is deployed as a web application.

III. Live Demo: The live application is hosted on Streamlit Community Cloud and can be accessed here - https://movie-review-analysis-kphnknzpirpregvcr2ndae.streamlit.app/ 

IV. Technical Stack:
  
    1.Language : Python

    2.Libraries used : pandas, scikit-learn, joblib, streamlit, re
  
    3.Tools used : Google Colab, Git, GitHub, Streamlit Community Cloud


V. Project Pipeline

    1.Data Preprocessing: The raw text data was cleaned by changing its 
        case, removing special characters, and filtering common stop words.
  
    2.Feature Engineering: The cleaned text was converted into a 
        numerical format using TF-IDF Vectorization to be used by the model.
  
    3.Model Training: A Logistic Regression model was trained on the 
        vectorized data. Its performance was optimized using Grid Search, which identified the best hyperparameters to 
        improve accuracy.
  
    4.Model Deployment: The trained model and vectorizer were saved and then deployed
        as a web application using Streamlit.


VI. Local Setup

    1. Clone:  git clone https://github.com/Suhas-Tatte/movie-review-analysis.git

    2.Install Dependencies:  pip install -r requirements.txt

    3.Run the Application:  streamlit run app.py

    
VII. Potential Improvements:
    
    1. Use more advanced models like BERT or LSTM.
    
    2. Expand the dataset for more robust training.
    
    3. Add features like sentiment visualization or more complex UI.
