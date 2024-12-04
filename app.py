from flask import Flask, request, jsonify
from transformers import T5Tokenizer, TFAutoModelForSeq2SeqLM
from bs4 import BeautifulSoup

app = Flask(__name__)

model = TFAutoModelForSeq2SeqLM.from_pretrained("./CodiLeapML/summarization")
tokenizer = T5Tokenizer.from_pretrained("./CodiLeapML/summarization")

def clean_html(raw_html):
    """Membersihkan HTML menjadi teks."""
    if isinstance(raw_html, str) and "<" in raw_html and ">" in raw_html:
        soup = BeautifulSoup(raw_html, "html.parser")
        return soup.get_text(separator=" ")
    return raw_html

@app.route('/summarize', methods=['POST'])
def summarize():
    try:
        data = request.get_json()
        input_text = data.get("text", "")

        if not input_text:
            return jsonify({"error": "No text provided"}), 400

        cleaned_text = clean_html(input_text)

        input_ids = tokenizer.encode(cleaned_text, return_tensors='tf')
        summary_ids = model.generate(
            input_ids,
            max_length=500,
            min_length=300,
            num_beams=4,
            repetition_penalty=2.0,
            length_penalty=0.8,
            early_stopping=False,
            no_repeat_ngram_size=3,
            use_cache=True
        )

        summary_text = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return jsonify({"summary": summary_text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
