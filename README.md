1.
   # 🔗 Innovaxel URL Shortener

A simple Flask-based URL shortening service built with MongoDB.  
This app allows users to create, update, rretrive, delete, and view statistics of shortened URLs with a web UI.

---

## 🚀 Features

- Shorten any URL into a custom code
- Track number of times the short URL was accessed
- Update or delete existing shortened URLs
- Retrive long url based on short URL
- Frontend included for easier interaction

---

## 🛠️ Tech Stack

- **Backend:** Flask (Python)
- **Database:** MongoDB
- **Frontend:** HTML (Jinja2 Template)
- **Extras:** Flask-CORS, Flask-PyMongo

---

## ⚙️ Setup Instructions

~bash
1. **Clone the repo:**
   ```bash
   git clone https://github.com/your-username/hammad-innovaxel-shahbaz.git
   cd hammad-innovaxel-shahbaz
   git checkout dev

~bash
2. **Create Virtual Environment**
   python -m venv venv
   source venv/bin/activate

~bash 
4. **Install dependencies**
   pip install -r requirements.txt


5. Start MongoDB (ensure it’s running on mongodb://localhost:27017)

~bash
6. **Run the app**
    python app.py


7. **Open in browser**
    http://localhost:5000 





**Project Structure**
hammad-innovaxel-shahbaz/
│
├── app.py               # Flask backend
├── templates/
│   └── index.html       # UI frontend
├── static/
│   └── style.css        # css for attractive visualization
├── requirements.txt     # Python packages
└── README.md            # Project info

