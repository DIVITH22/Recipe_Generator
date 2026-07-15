from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import requests
import os
import traceback

app = Flask(__name__)
CORS(app)

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Change this if you want to use another model
MODEL = "openai/gpt-oss-20b:free"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get_food_recommendations", methods=["POST"])
def get_food_recommendations():

    if not OPENROUTER_API_KEY:
        return jsonify({"error": "OPENROUTER_API_KEY not found"}), 500

    try:

        user_data = request.get_json(force=True)

        prompt = f"""
User has these ingredients:
{user_data.get('ingredients','')}

Preference:
{user_data.get('preference','')}

Food Style:
{user_data.get('style','')}

Age:
{user_data.get('age','')}

Recommend exactly 4 recipes.

For each recipe provide:

Recipe Name
Ingredients
Preparation Steps

Do not use markdown.
Do not use **.
"""

        payload = {
            "model": MODEL,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }

        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        }

        response = requests.post(
            OPENROUTER_API_URL,
            headers=headers,
            json=payload,
            timeout=60
        )

        print("STATUS :", response.status_code)
        print("BODY :", response.text)

        response.raise_for_status()

        data = response.json()

        if "choices" not in data:
            return jsonify({"error": data}), 500

        food_items = data["choices"][0]["message"]["content"]

        return jsonify({
            "foodItems": food_items
        })

    except requests.exceptions.Timeout:
        return jsonify({
            "error": "OpenRouter request timed out."
        }), 500

    except requests.exceptions.HTTPError:
        print(response.text)
        return jsonify({
            "error": response.text
        }), 500

    except Exception:
        traceback.print_exc()
        return jsonify({
            "error": "Internal Server Error"
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
