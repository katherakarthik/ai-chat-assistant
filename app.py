
from flask import Flask, render_template, request, jsonify
from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Get token from environment variable (SECURE!)
API_TOKEN = os.getenv('HUGGINGFACE_TOKEN')

if not API_TOKEN:
    raise ValueError("⚠️  HUGGINGFACE_TOKEN not found! Create a .env file with your token.")

# Initialize the Inference Client
client = InferenceClient(token=API_TOKEN)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/test")
def test_endpoint():
    """Test the inference client"""
    try:
        print("=" * 60)
        print("TESTING INFERENCE CLIENT")
        print("=" * 60)
        
        messages = [{"role": "user", "content": "Say hello!"}]
        
        response = client.chat_completion(
            messages=messages,
            model="meta-llama/Llama-3.2-1B-Instruct",
            max_tokens=50
        )
        
        result = response.choices[0].message.content
        
        print(f"Success! Response: {result}")
        print("=" * 60)
        
        return jsonify({
            "success": True,
            "response": result
        })
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({
            "success": False,
            "error": str(e)
        })

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json.get("message", "")
    
    print("\n" + "=" * 60)
    print(f"USER: {user_input}")
    print("=" * 60)
    
    models_to_try = [
        "meta-llama/Llama-3.2-1B-Instruct",
        "meta-llama/Llama-3.2-3B-Instruct",
        "Qwen/Qwen2.5-0.5B-Instruct",
        "HuggingFaceH4/zephyr-7b-beta",
    ]
    
    for model_name in models_to_try:
        try:
            print(f"\nTrying: {model_name}")
            
            messages = [
                {"role": "system", "content": "You are a helpful and friendly chatbot. Keep responses concise and conversational."},
                {"role": "user", "content": user_input}
            ]
            
            response = client.chat_completion(
                messages=messages,
                model=model_name,
                max_tokens=150,
                temperature=0.7,
                stream=False
            )
            
            answer = response.choices[0].message.content.strip()
            
            print(f"✅ Success with {model_name}")
            print(f"Response: {answer}")
            print("=" * 60 + "\n")
            
            return jsonify({"reply": answer})
            
        except Exception as e:
            error_msg = str(e)
            print(f"❌ Failed with {model_name}: {error_msg[:100]}")
            
            if "loading" in error_msg.lower() or "503" in error_msg:
                continue
            elif "429" in error_msg or "rate" in error_msg.lower():
                continue
            else:
                continue
    
    print("❌ All models failed!")
    print("=" * 60 + "\n")
    
    return jsonify({
        "reply": "I'm having trouble connecting right now. Please try again in a moment!"
    })

@app.route("/health")
def health():
    """Check if the client is working"""
    try:
        user_info = client.whoami()
        
        return jsonify({
            "status": "✅ Connected",
            "username": user_info.get("name", "Unknown"),
            "type": user_info.get("type", "Unknown")
        })
    except Exception as e:
        return jsonify({
            "status": "❌ Error",
            "error": str(e)
        })

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("🚀 AI CHATBOT - SECURE VERSION")
    print("=" * 60)
    print(f"✓ Token loaded from environment")
    print("✓ Main page:   http://127.0.0.1:5000")
    print("✓ Test page:   http://127.0.0.1:5000/test")
    print("✓ Health:      http://127.0.0.1:5000/health")
    print("=" * 60 + "\n")
    app.run(debug=True)