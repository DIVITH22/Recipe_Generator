from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import requests
import os
import traceback

app = Flask(__name__)
CORS(app)

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Use a reliable free model
MODEL = "openai/gpt-oss-20b:free"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get_food_recommendations", methods=["POST"])
def get_food_recommendations():
    try:

        # Check API Key
        if not OPENROUTER_API_KEY:
            return jsonify({"error": "OPENROUTER_API_KEY not found"}), 500

        user_data = request.get_json()

        ingredients = user_data.get("ingredients", "")
        preference = user_data.get("preference", "")
        style = user_data.get("style", "")
        age = user_data.get("age", "")

        prompt = f"""
User has these ingredients:
{ingredients}

Preference:
{preference}

Food Style:
{style}

Age:
{age}

Recommend exactly four recipes.

For each recipe include:

1. Recipe Name
2. Ingredients
3. Preparation Steps

Do not use markdown.
Do not use **.
"""

        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": MODEL,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }

        response = requests.post(
            OPENROUTER_API_URL,
            headers=headers,
            json=payload,
            timeout=90
        )

        print(response.status_code)
        print(response.text)

        response.raise_for_status()

        result = response.json()

        food_items = result["choices"][0]["message"]["content"]

        return jsonify({
            "foodItems": food_items
        })

    except Exception:
        traceback.print_exc()
        return jsonify({
            "error": "Server Error"
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
print("=== NEW VERSION DEPLOYED ===")
print(response.status_code)
print(response.text)
