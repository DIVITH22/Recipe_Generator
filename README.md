🍽️ AI-Powered Food Preference Chatbot

📌 Overview

The AI-Powered Food Preference Chatbot is a web-based application that provides personalized food recommendations based on user preferences. Users can interact with the chatbot by entering available ingredients, dietary preferences, preferred cuisine style, and age. The system then utilizes Artificial Intelligence to generate customized recipes along with preparation instructions.

This project demonstrates the integration of Frontend Development, Backend Development, API Integration, and AI-powered recommendation systems to deliver an interactive user experience.

---

✨ Features

* Interactive chatbot-based user interface
* Collects ingredient availability and dietary preferences
* Supports both Vegetarian and Non-Vegetarian food recommendations
* Generates four personalized recipes
* Provides ingredients and step-by-step cooking instructions
* Real-time AI-powered recommendation generation
* Responsive design for desktop and mobile devices

---

🛠️ Technologies Used

Frontend

* HTML5
* CSS3
* JavaScript

Backend

* Python
* Flask
* Flask-CORS

AI Integration

* OpenRouter API
* GPT-OSS 20B Model

---

📂 Project Structure

```text
Food-Preference-Chatbot/
│
├── app.py
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── script.js
├── README.md
└── requirements.txt
```

---

⚙️ Installation & Setup

Clone the Repository

```bash
git clone <repository-url>
cd Food-Preference-Chatbot
```

Install Required Packages

```bash
pip install flask flask-cors requests
```

Run the Application

```bash
python app.py
```

Open in Browser

```text
http://127.0.0.1:5000
```

---

🚀 How It Works

1. User enters available ingredients.
2. User selects Veg or Non-Veg preference.
3. User chooses a preferred cuisine style.
4. User provides age information.
5. Frontend sends the collected data to the Flask backend.
6. The backend communicates with the AI model through the OpenRouter API.
7. The AI generates four personalized food recommendations with ingredients and preparation steps.
8. Results are displayed in the chatbot interface.

---

🎯 Future Enhancements

* User Authentication System
* Recipe History Management
* Nutritional Value Analysis
* Multi-Language Support
* Voice-Based Interaction
* AI-Generated Recipe Images
* Recipe Rating and Feedback System

---

👨‍💻 Author

Divith S
B.E Computer Science Engineering
Kongunadu College of Engineering and Technology

---

📜 License

This project is developed for educational and learning purposes.
