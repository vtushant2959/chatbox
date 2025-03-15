# Import necessary libraries
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Ensure necessary NLTK data is downloaded
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

# Create a new chatbot named "MyChatBot"
chatbot = ChatBot('MyChatBot')

# Create a trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot using the English corpus
trainer.train("chatterbot.corpus.english")

# Function to get a response from the chatbot
def get_response(user_input):
    return str(chatbot.get_response(user_input))

# Main function to run the chatbot
def run_chatbot():
    print("Welcome to MyChatBot! Type 'quit' to exit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "quit":
            print("Goodbye!")
            break
        
        print("Bot:", get_response(user_input))

# Run the chatbot
if __name__ == "__main__":
    run_chatbot()
