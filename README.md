<div align="center">

# 🧠 LLMFuzzer - Fuzzing Framework for Large Language Models 🧠

![LLMFuzzer-shell](https://github.com/mnns/LLMFuzzer/assets/1796080/71b006df-706c-43f6-acd1-49646dbcb0e5)

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Stars](https://img.shields.io/github/stars/mnns/LLMFuzzer)
![Forks](https://img.shields.io/github/forks/mnns/LLMFuzzer)
![Issues](https://img.shields.io/github/issues/mnns/LLMFuzzer)

</div>

LLMFuzzer is the first open-source fuzzing framework specifically designed for Large Language Models (LLMs), especially for their integrations in applications via LLM APIs. 🚀💥

# 🎯 Who is this for?

If you're a security enthusiast, a pentester, or a cybersec researcher who loves to find and exploit vulnerabilities in AI systems, LLMFuzzer is the perfect tool for you. It's built to make your testing process streamlined and efficient. 🕵️‍♀️

![Untitled](https://github.com/mnns/LLMFuzzer/assets/1796080/a143897d-383c-4ed9-8b2f-65f4cdc5aa63)

# 🌟 Features

- Robust fuzzing for LLMs 🧪
- LLM API integration testing 🛠️
- Wide range of fuzzing strategies 🌀
- Modular architecture for easy extendability 📚

## 🚀 Get Started

1. Clone the repo
```bash
git clone https://github.com/mnns/LLMFuzzer.git
```

2. Navigate to the project directory
```bash
cd LLMFuzzer
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Edit **llmfuzzer.cfg** with your LLM API endpoint (LLMFuzzer -> Your Application -> LLM)
```bash
Connection: 
  Type: HTTP-API
  Url: "http://localhost:3000/chat" # Your LLM API
  Content: JSON
  Query-Attribute: "query" # Your JSON query attribute
  Output-Attribute: "answer" # Your JSON response attribute
  Headers: {'enwiki_session': '17ab96bd8ffbe8ca58a78657a918558'} # Add HTTP Headers if needed 
  Cookie: {'enwiki_session': '17ab96bd8ffbe8ca58a78657a918558'} # Add Cookies if needed
```

5. Run LLMFuzzer
```bash
python main.py
```

## 📚 Documentation
We are working on full documentation. It will cover detailed information about the architecture, different fuzzing strategies, examples, and how to extend the tool.

## 🤝 Contributing
We welcome all contributors who are passionate about improving LLMFuzzer. See our contributing guidelines for ways to get started. 🤗

## 💼 License
LLMFuzzer is licensed under the MIT License. See the LICENSE file for more details.

## 🎩 Acknowledgments
LLMFuzzer couldn't exist without the community. We appreciate all our contributors and supporters. Let's make AI safer together! 💖

