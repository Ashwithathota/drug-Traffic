# 🕵️‍♀️ Software Solutions to Identify Users Behind Telegram, WhatsApp, and Instagram Based Drug Trafficking

## 🔍 Overview

This project presents a software-based investigative solution designed to detect and identify individuals involved in drug trafficking activities on popular messaging and social media platforms—**Telegram, WhatsApp, and Instagram**. It utilizes **Natural Language Processing (NLP)**, **Machine Learning**, and a custom **flagging and alert system** to analyze suspicious chats and behavior patterns.

---

## 🚀 Features

- 🔐 **User Authentication** for Admin and Law Enforcement.
- 💬 **Message Input and Chat Interface** for uploading suspicious conversations.
- 🧠 **NLP & Machine Learning Module** for analyzing drug-related keywords and patterns.
- 🚨 **Flagging & Alert System** that detects suspicious messages in real time.
- 🛠 **Admin Review & Action Module** to inspect flagged chats and generate reports.
- 🗄 **SQLite Database Management** for storing user data, messages, alerts, and actions.

---

## 🧰 Technologies Used

- **Frontend**: HTML, CSS, Bootstrap  
- **Backend**: Django (Python), Machine Learning Models (Scikit-learn, NLTK/spaCy)  
- **Database**: SQLite3  
- **Tools**: Python, Django Admin, Regex, NLP, Matplotlib/Seaborn (for analysis & graphs)

---

## 🧪 System Modules

1. **User Authentication Module** – Login/registration for admin/investigators.
2. **Chat Input Interface** – Upload or simulate chat content.
3. **NLP & ML Engine** – Processes chat content to extract entities, keywords, and suspicious terms.
4. **Flagging System** – Identifies and flags users/groups based on set rules and ML predictions.
5. **Admin Dashboard** – View flagged users, download reports, mark actions taken.
6. **Database Module** – Securely stores users, messages, flagged records, actions, and logs.

---

## ⚙️ Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/drug-trafficking-monitoring.git
   cd drug-trafficking-monitoring
**2. Create Virtual Environment**
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
**3.Install Requirements**
   pip install -r requirements.txt
**4.Run Migrations**
  python manage.py makemigrations
  python manage.py migrate
**5.Start Server**
  python manage.py runserver
  
📁 **Folder Structure**
/drug-trafficking-monitoring
│
├── manage.py
├── db.sqlite3
├── requirements.txt
├── /templates
├── /static
├── /media
├── /ml_model         # Trained ML models, vectorizers, NLP scripts
├── /core             # Django App (views, models, urls, etc.)
└── README.md

🎯**Project Objectives**
CO1: Detect users involved in illegal drug-related activity via messaging analysis.

CO2: Analyze communication patterns and group networks using NLP.

CO3: Apply ML for pattern recognition in message behavior.

CO4: Alert authorities with detailed flagged reports.

CO5: Ensure ethical compliance and privacy consideration.

🧾**Project Outcomes**
PO1: High-accuracy identification of suspicious behavior.

PO2: Visualization of social group interactions.

PO3: Dashboard to streamline investigations.

PO4: Exportable reports for legal use.

PO5: Framework for global law enforcement collaboration.

👨‍⚖️ **Disclaimer**
This software is developed strictly for academic and law enforcement research purposes. Any misuse for surveillance without legal authorization is strictly discouraged.

📬**Contact**
Thota Ashwitha
📧 thotaashwitha03@gmail.com





