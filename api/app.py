from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Load the dictionary data
with open('Scraped Data/Dictionaries/tagalog_dictionary.json', 'r') as f:
    dictionary_data = json.load(f)

@app.route('/api/define', methods=['GET'])
def define_word():
    # Get the word parameter from the URL
    word = request.args.get('word')

    # Search for the word in the list of dictionaries
    for entry in dictionary_data:
        if entry["word"].lower() == word.lower():  # Case-insensitive match
            return jsonify({"word": entry["word"], "definition": entry["definition"]})
    
    # If the word is not found
    return jsonify({"error": "Word not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)