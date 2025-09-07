import google.generativeai as genai
import os
from typing import List

# Configure with API key
API_KEY = "AIzaSyDSij09Q6KeBy3Xk5ytR0VRqFG4JQfNUOM"  # Consider using environment variables instead

def initialize_chatbot():
    print("Initializing chatbot...")
    try:
        genai.configure(api_key=API_KEY)
        
        # List available models
        models = genai.list_models()
        model_names = [model.name for model in models]
        print(f"Available models: {model_names}")
        
        # Use a valid model name from the available models
        # Note: The model name should be the full name as returned by the API
        model = genai.GenerativeModel('gemini-1.5-pro')  # Use a valid model name
        chat = model.start_chat(history=[])
        return chat
    except Exception as e:
        print(f"Error during initialization: {e}")
        return None

def run_chatbot():
    chat = initialize_chatbot()
    
    if not chat:
        print("Failed to initialize chatbot. Exiting.")
        return
    
    print("\nChatbot initialized. Type 'exit' or 'quit' to end the conversation.")
    print()
    
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit"]:
                print("Goodbye!")
                break
            
            if not user_input.strip():
                continue
                
            response = chat.send_message(user_input)
            print(f"\nBot: {response.text}\n")
            
        except Exception as e:
            print(f"\nError during conversation: {e}")
            print("Trying to restart the chat session...")
            chat = initialize_chatbot()
            if not chat:
                print("Failed to reinitialize chatbot. Exiting.")
                break

if __name__ == "__main__":
    run_chatbot()