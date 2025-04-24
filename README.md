# Random Text Generator Web App

A simple web application that uses the GPT-2 language model to generate text based on user prompts. Built with Flask and Hugging Face Transformers.

## 🚀 Features

- Prompt-based text generation
- User-defined response length
- Modern, responsive UI with loading indicator
- Built using GPT-2 via Hugging Face Transformers

## 🛠 Tech Stack

- Backend: Flask
- Frontend: HTML, CSS (custom)
- Model: GPT-2 (via `transformers` library)

## 📁 Project Structure

├── app.py # Flask application ├── templates/ │ └── index.html # Main frontend template ├── static/ │ └── style.css # Styling for the frontend └── README.md # Project documentation

bash
Copy
Edit

## ▶️ How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/random-text-generator.git
   cd random-text-generator
Create a virtual environment (optional but recommended)

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
Install dependencies

bash
Copy
Edit
pip install flask transformers
Run the app

bash
Copy
Edit
python app.py
Open your browser and visit: http://127.0.0.1:5000

📸 Screenshot

📌 Notes
The app uses GPT-2 with a dynamic token limit based on the word count.

A word count higher than model capabilities may result in trimmed output.

🧠 Future Improvements
Add support for multiple model options (e.g., GPT-2 XL, GPT-Neo)

Implement streaming responses

Allow text download/share option
