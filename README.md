This project is an AI-powered Streamlit app for business-oriented SQL Q&A on e-commerce data using Google Gemini. The application automatically converts natural English business questions into SQLite queries and displays answers from real product data.

# Create the Conda Environment
conda create -p venv python==3.10 -y 

conda activate ./venv/

# Install Python Requirements
pip install -r requirements.txt

# Get Google API Key
Go to Google AI Studio(https://aistudio.google.com/app/apikey).

Generate your Gemini API key.

Create a .env file in the same folder as the code.

### Add the API key to your .env file:

GOOGLE_API_KEY="your-google-api-key-here"

# Start the Streamlit App
streamlit run app.py
