# Log-Classification
Log-Classification is a Python project that classifies log messages using multiple approaches, including Regular Expression (Regex), BERT-based processing, and Large Language Models (LLMs). This repository provides an easy-to-use CLI/API setup for classifying logs with high flexibility and accuracy.

🚀 Features

✔ Hybrid log classification using multiple models
✔ Regex-based pattern matching for simple logs
✔ BERT embeddings for semantic classification
✔ LLM-based processing for complex or ambiguous logs
✔ FastAPI server available for REST API classification

📁 Project Structure
📦 Log-Classification
├── classify.py             # Classification logic/entry point  
├── main.py                 # Main execution script  
├── processor_regex.py      # Regex classification module  
├── processor_bert.py       # BERT classifier module  
├── processor_llm.py        # LLM classification module  
├── server.py               # FastAPI server  
├── .env                    # Environment variables  
├── requirements.txt        # Dependencies  
└── README.md               # Project documentation

🛠️ Installation

Clone the repository

git clone https://github.com/codewithdev0805/Log-Classification.git
cd Log-Classification


Install dependencies

pip install -r requirements.txt


Setup environment variables

Create a .env file at the project root for any keys needed (e.g., LLM API keys).
Example:

OPENAI_API_KEY=your_api_key_here

💡 Usage
🔹 Run Log Classification (CLI)
python main.py --input "Your log message here"


This will print the predicted log class and scores.

🔹 Use FastAPI Server

Start the server:

python server.py


Open in browser or use with tools like Postman / curl:

POST http://localhost:8000/classify
Body: { "log": "User login failed from IP 192.168.1.1" }


Response:

{ "classification": "AUTH_FAILURE", "confidence": 0.87 }

📌 Classification Process

Regex Processor
Matches predefined patterns for structured logs.

BERT Processor
Uses sentence embeddings + classifier model for semantic patterns.

LLM Processor
Utilizes Large Language Models when patterns are complex or data is sparse.

🧠 How It Works

The project runs classification in a pipeline:

Try regex matching

If no match, use BERT classifier

Else fallback to LLM classification

This hybrid approach balances performance with accuracy and flexibility.

🧪 Examples

Input:

Error 503 – Service Unavailable from server X


Output:

{
  "log": "Error 503 – Service Unavailable",
  "classification": "Server_Error",
  "confidence": 0.93
}

💡 Contributing

Contributions are welcome! To contribute:

Fork the repo

Create your feature branch

Commit and push

Open a Pull Request

📝 License

This project is open source and available under the MIT License.
