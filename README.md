# 😂 Random Joke Generator

A fun, lightweight web app built with **Python Flask** that fetches and displays random jokes using the [Official Joke API](https://official-joke-api.appspot.com/jokes/random). The app demonstrates core Flask skills like routing, API consumption, and template rendering.

---

## 🚀 Features

- 🔄 Get a new random joke on every refresh
- 🧠 Uses a public REST API
- 💻 Built with Flask and Jinja2
- 🎨 Clean, responsive UI with custom CSS

---

## 📸 Screenshot

<img width="1433" alt="image" src="https://github.com/user-attachments/assets/77a42830-998c-4e19-ae03-fe790876e695" />


---

## 🛠️ Technologies Used

- Python 3
- Flask
- HTML & CSS
- Jinja2 (template engine)
- Official Joke API

---

## 📂 Project Structure

joke-generator/
├── app.py # Flask backend
├── templates/
│ └── index.html # HTML template
├── static/
│ └── style.css # Custom styling
└── README.md # This file

---

## 💻 Getting Started

### Prerequisites
- Python 3.x installed
- `pip` (Python package manager)

### Installation

```bash
# Clone the repo
git clone https://github.com/your-username/joke-generator.git
cd joke-generator

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install Flask
pip install flask

# Run the app
python app.py
