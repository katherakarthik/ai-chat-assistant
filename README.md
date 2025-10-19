# 🤖 AI Chat Assistant

A modern, Twitter/X-inspired AI chatbot powered by Hugging Face's Inference API. Built with Flask and featuring a sleek dark-themed UI.

![AI Chat Assistant](https://img.shields.io/badge/AI-Chatbot-blue)
![Python](https://img.shields.io/badge/Python-3.8+-green)
![Flask](https://img.shields.io/badge/Flask-3.0+-red)
![Hugging Face](https://img.shields.io/badge/HuggingFace-API-yellow)

## ✨ Features

- 🎨 **Twitter/X-inspired UI** - Modern, clean, and responsive design
- 💬 **Real-time Chat** - Instant responses from AI models
- 🤖 **Multiple AI Models** - Automatic fallback between models for reliability
- ⚡ **Fast & Lightweight** - Optimized for quick responses
- 🔒 **Secure** - Environment variable protection for API keys
- 📱 **Responsive** - Works on desktop, tablet, and mobile

## 🚀 Demo

![Chat Interface](screenshot.png)
*Screenshot of the chat interface*

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **AI API**: Hugging Face Inference API
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Models Used**:
  - Llama 3.2 1B Instruct
  - Llama 3.2 3B Instruct
  - Qwen 2.5 0.5B Instruct
  - Zephyr 7B Beta

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- A Hugging Face account and API token

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/ai-chat-assistant.git
   cd ai-chat-assistant
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the root directory:
   ```env
   HUGGINGFACE_TOKEN=your_token_here
   ```

   To get your Hugging Face token:
   - Go to [Hugging Face Settings](https://huggingface.co/settings/tokens)
   - Create a new token with "Inference API" permissions
   - Copy and paste it into your `.env` file

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   
   Navigate to `http://127.0.0.1:5000`

## 📁 Project Structure

```
ai-chat-assistant/
├── app.py                 # Main Flask application
├── templates/
│   └── index.html        # Chat interface
├── static/
│   └── (CSS if separate)
├── .env                  # Environment variables (not in repo!)
├── .gitignore           # Git ignore file
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## 🔧 Configuration

### Change AI Models

Edit the `models_to_try` list in `app.py`:

```python
models_to_try = [
    "meta-llama/Llama-3.2-1B-Instruct",
    "your-preferred-model-here",
]
```

### Customize UI

Modify the CSS in `templates/index.html` to change colors, fonts, and layout.

## 🌟 Features in Detail

### Typing Indicator
Shows animated dots when AI is generating a response

### Auto-retry Logic
Automatically tries alternative models if one fails

### Dark Theme
Eye-friendly dark mode inspired by Twitter/X

### Message History
Keeps track of conversation during the session

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## ⚠️ Important Notes

- **Never commit your `.env` file** - It contains your API token!
- **Free tier limits** - Hugging Face free accounts have rate limits
- **Model availability** - Some models may take time to load on first request

## 🐛 Troubleshooting

### "Invalid credentials" error
- Check that your `.env` file exists and contains a valid token
- Ensure your token has "Inference API" permissions

### "Model loading" message
- First request may take 20-60 seconds to load the model
- Try again after a moment

### Rate limit errors
- Free accounts have limited requests per hour
- Consider upgrading to Hugging Face PRO for higher limits

## 📧 Contact

karthik - karthikkattera8688@gmail.com

Project Link: [https://github.com/katherakarthik/ai-chat-assistant](https://github.com/YOUR_USERNAME/ai-chat-assistant)

## 🙏 Acknowledgments

- [Hugging Face](https://huggingface.co/) for the Inference API
- [Flask](https://flask.palletsprojects.com/) for the web framework
- Twitter/X for UI inspiration

---

Made with ❤️ by Kathera Karthik
