# 🎙️ Speech to Image Display System

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)

An interactive web application that listens to voice/speech input, processes spoken keywords or phrases, and dynamically retrieves and displays corresponding visual imagery from a curated database.

---

## 📌 Features

* 🎤 **Voice Input Processing**: Captures live speech input via the browser or microphone.
* 🖼️ **Dynamic Image Display**: Maps spoken words/phrases to corresponding visual assets in real time.
* 🗄️ **Database Integration**: Managed data handling via `database.py` for keyword-image mapping.
* 🌐 **Web Interface**: Clean, responsive frontend built with Flask templates and static assets.

---

## 📁 Project Structure

```text
speechtoimage/
│
├── static/
│   └── images/          # Image assets mapped to voice keywords
├── templates/
│   └── index.html       # Web UI templates
├── app.py               # Main Flask application / routing backend
├── database.py          # Database setup and query handlers
└── test.html            # UI/Feature testing template
```

🛠️ Tech Stack
​ Backend: Python, Flask
​ Database: SQLite / Python DB API
​ Frontend: HTML5, CSS3, JavaScript (Web Speech API)
​ Image Assets: Static image storage

​🚀 Getting Started

​1. Prerequisites

​  Make sure you have Python 3.8+ installed on your system.

​2. Clone the Repository

  git clone [https://github.com/Klakshitha/speechtoimage.git](https://github.com/Klakshitha/speechtoimage.git)
  cd speechtoimage

  
3. Install Dependencies
   
   pip install flask
  
  Add any additional packages if used, e.g., SpeechRecognition, PyAudio)

​4. Run the Application

  python app.py
  
  
5. Open in Browser
   
​  Visit the following local address in your web browser:

  [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

  
🎯 How It Works

1.​Click the microphone button on the web interface.

2.​Speak a keyword or phrase clearly into the microphone.

3.​The system processes the voice input, queries the database, and renders the corresponding image on the screen.
