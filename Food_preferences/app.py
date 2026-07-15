from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import requests
import json
import os


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "openai/gpt-oss-20b:free"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_food_recommendations", methods=["POST"])
def get_food_recommendations():
    try:
        user_data = request.get_json()
        ingredients = user_data['ingredients']
        preference = user_data['preference']
        style = user_data['style']
        age = user_data['age']

        prompt = (
            f"User has ingredients: {ingredients}. "
            f"They prefer {preference} food. "
            f"They want {style} style food, and their age is {age}. "
            "Recommend four food items with ingredients and steps to prepare. "
            "You no need to use ** in the generating text."
        )

        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
            # Optionally add Referer and X-Title headers if needed
        }
        data = {
            "model": MODEL,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }

        response = requests.post(OPENROUTER_API_URL, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        result = response.json()

        # Extract the generated text from the response
        food_items = result.get("choices", [{}])[0].get("message", {}).get("content", "")

        if food_items:
            print("FOOD: ", food_items)
            return jsonify({"foodItems": food_items})
        else:
            return jsonify({"error": "No recommendations generated"}), 500

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
