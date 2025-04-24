from flask import Flask, request, render_template
from transformers import pipeline

app = Flask(__name__)
generator = pipeline("text-generation", model="gpt2", framework="pt")

@app.route("/", methods=["GET", "POST"])
def index():
    output_text = ""
    if request.method == "POST":
        user_prompt = request.form["prompt"]
        word_limit = request.form.get("length", "1000") 

        try:
            word_limit = int(word_limit)
        except ValueError:
            word_limit = 1000

        max_tokens = int(word_limit * 1.5)  
        result = generator(user_prompt, max_length=max_tokens, num_return_sequences=1)
        generated = result[0]["generated_text"]

        words = generated.split()
        if len(words) >= word_limit:
            output_text = " ".join(words[:word_limit])
        else:
            output_text = " ".join(words) + f"\n\n(Note: Only {len(words)} words were generated.)"

    return render_template("index.html", output=output_text)

if __name__ == "__main__":
    app.run(debug=True)
