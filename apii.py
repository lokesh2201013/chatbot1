from flask import Flask, request, render_template, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = "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"

@app.route('/')
def home():
    return render_template('api.html')

@app.route('/api', methods=['POST'])
def process_message():
    try:
        data = request.get_json()
        user_message = data['message']

        # You can use OpenAI API to generate a response based on the user's message
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=user_message,
            max_tokens=50
        )

        # Extract the generated response
        ai_response = response.choices[0].text

        return jsonify({"message": ai_response})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
