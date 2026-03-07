🌱 Crop Recommendation System

A Flask-based web application that recommends suitable crops and fertilizers based on soil type, weather conditions, and market demand.
The system also supports multiple languages (English, Hindi, Telugu) to make it accessible for farmers from different regions.

🚀 Features

🌾 Crop recommendations based on:

Soil type

Weather conditions

Market demand

🧪 Fertilizer suggestions for recommended crops

🌍 Multi-language support:

English

Hindi

Telugu

🖥 Simple and user-friendly web interface

⚡ Fast rule-based recommendation system

🛠 Tech Stack

Backend: Python, Flask

Frontend: HTML, CSS, Jinja2 Templates

Language Support: Dictionary-based translation system

📂 Project Structure
Crop-Recommendation-System
│
├── App.py                # Flask backend logic
├── templates
│   ├── index.html        # Input form for crop recommendation
│   └── result.html       # Displays recommended crops and fertilizers
│
└── README.md

index.html contains the form where users select soil type, weather, and market demand. 

index

result.html displays the recommended crops and fertilizers after processing the inputs. 

Result

App.py handles the Flask server, recommendation logic, and language translations. 

App
