# Prompt Engineering Assistant

An AI-powered **Prompt Engineering Assistant** built with **Python** and **Google Gemini AI**. This application helps users create, improve, analyze, optimize, evaluate, and translate prompts for AI models through an easy-to-use command-line interface.

---

## Features

* ✨ Generate high-quality prompts
* 🚀 Improve existing prompts
* 📖 Explain prompts in detail
* ⚡ Optimize prompts for better AI responses
* 📊 Evaluate prompt quality
* 🌍 Translate prompts into different languages
* 💬 Chat with Google Gemini AI
* 💾 Save prompts for future use
* 📜 View prompt history
* 📤 Export prompt history

---

## Technologies Used

* Python 3.10+
* Google Gemini API
* google-genai
* python-dotenv
* colorama

---

## Project Structure

```
Prompt_Engineering_Assistant/
│── app.py                 # Main application
│── assistant.py           # Gemini AI functions
│── test.py                # Testing script
│── requirements.txt       # Project dependencies
│── prompt_history.txt     # Saved prompt history
│── .env.example           # Environment variable template
│── README.md              # Project documentation
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Sameera9640/Prompt_Engineering_Assistant.git
```

### 2. Navigate to the project folder

```bash
cd Prompt_Engineering_Assistant
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file in the project folder and add your Google Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## Running the Application

Windows

```bash
py -3.10 app.py
```

or

```bash
python app.py
```

---

## Sample Menu

```
=============================
 Prompt Engineering Assistant
=============================

1. Generate Prompt
2. Improve Prompt
3. Explain Prompt
4. Optimize Prompt
5. Evaluate Prompt
6. Translate Prompt
7. AI Chat
8. Save Prompt
9. View History
10. Export History
0. Exit
```

---

## Requirements

* Python 3.10 or later
* Google Gemini API Key
* Internet connection

---

## Future Improvements

* GUI using Tkinter or PyQt
* Web version using Flask or Streamlit
* Multiple AI model support
* User authentication
* Prompt templates
* Dark mode interface

---

## Author

**Sameera9640**

GitHub: https://github.com/Sameera9640

---

## License

This project is developed for learning and educational purposes.
