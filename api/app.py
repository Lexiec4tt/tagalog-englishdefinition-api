from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

# Load the dictionary data
with open('Scraped Data/Dictionaries/tagalog_dictionary.json', 'r') as f:
    dictionary_data = json.load(f)

@app.route('/api/define', methods=['GET'])
def define_word():
    # Get the word parameter from the URL
    word = request.args.get('word')

    # Array of all matching words
    words = []

    # Search for the word in the list of dictionaries
    for entry in dictionary_data:
        if entry["word"].lower() == word.lower():  # Case-insensitive match
            jsonWord = jsonify({"word": entry["word"], "definition": entry["definition"]})
            words.append(jsonWord)
    
    # If the word is not found
    if not words:
        return jsonify({"error": "Word not found"}), 404
    
    # If there are word/s
    else:
        return jsonify({"words": words});
    

if __name__ == '__main__':
    port = int(os.getenv('PORT', 10000))  # Default to port 10000 if PORT is not set
    app.run(host='0.0.0.0', port=port)
