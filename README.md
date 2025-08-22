Jarvis AI Voice Assistant 🎙️🤖

A Python-based desktop voice assistant that can perform system operations, fetch live information, tell jokes, play YouTube videos, send emails/WhatsApp messages, and much more.
This assistant uses speech recognition, text-to-speech, and multiple APIs to interact with the user naturally.

✨ Features
🖥️ System Operations

Open Notepad, Discord, Calculator, Camera, Command Prompt directly by voice.

🌍 Online Features

Get IP Address.

Search Wikipedia and summarize results.

Play videos on YouTube.

Search on Google.

Fetch latest News Headlines (using NewsAPI).

Get Weather Report for your current city (via OpenWeather API).

Show Trending Movies (via TMDB API).

📩 Communication

Send WhatsApp messages instantly (via PyWhatKit).

Send Emails directly from voice commands.

🎭 Fun Utilities

Listen to random jokes (Dad Jokes API).

Receive random life advice (AdviceSlip API).

🗣️ Smart Interaction

Greets user according to the time of day.

Converts speech → text using Google Speech Recognition.

Converts text → speech using pyttsx3.

Contextual exit commands (“exit”, “stop”) with time-based goodbyes.

🛠️ Requirements

Python 3.7+

Required libraries:

pip install requests wikipedia pywhatkit pyttsx3 SpeechRecognition


APIs Needed (you must generate your own free API keys):

NewsAPI

OpenWeather

TMDB

📂 Project Structure
JarvisAI/
│── main.py                  # Main voice assistant code
│── utils.py                 # Opening text & helper phrases
│── functions/
│   ├── os_ops.py            # System operations (Notepad, CMD, etc.)
│   ├── online_ops.py        # Online features (news, weather, etc.)
│── requirements.txt         # Python dependencies
│── README.md                # Documentation

▶️ How to Run

Clone the repository or download the project files.

Install dependencies:

pip install -r requirements.txt


Run the assistant:

python main.py


Speak your command! 🎤 Example:

“Open Notepad”

“Search Wikipedia for Artificial Intelligence”

“Play Imagine Dragons on YouTube”

“Tell me a joke”

“What’s the weather in my city?”

⚠️ Notes

Make sure your microphone is enabled for speech recognition.

Replace the API Keys, Email, and Password in online_ops.py with your own valid credentials.

For sending emails, enable "Less secure app access" in your Gmail account or use an App Password.

WhatsApp messages require WhatsApp Web to be logged in on your default browser.

👨‍💻 Author

Developed by Naveed
🎓 Department of CSE 
📅 2025
