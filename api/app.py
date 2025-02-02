from flask import Flask, jsonify, request
from flask_cors import CORS  # Import the CORS module
import json
import os

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# Load the dictionary data
with open('Scraped Data/Dictionaries/tagalog_dictionary.json', 'r') as f:
    dictionary_data = json.load(f)

@app.route('/api/define', methods=['GET'])
def define_word():
    # Get the word parameter from the URL
    word = request.args.get('word')
    matches = []  # List to store all matches

    # Search for the word in the list of dictionaries
    for entry in dictionary_data:
        if entry["word"].lower() == word.lower():  # Case-insensitive match
            matches.append({"word": entry["word"], "definition": entry["definition"]})
    
    # If matches are found, return them
    if matches:
        return jsonify({"matches": matches})
    
    # If the word is not found
    return jsonify({"error": "Word not found"}), 404

if __name__ == '__main__':
    port = int(os.getenv('PORT', 10000))  # Default to port 10000 if PORT is not set
    app.run(host='0.0.0.0', port=port)
