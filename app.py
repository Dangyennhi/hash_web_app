from flask import Flask, render_template, request
import hashlib

app = Flask(__name__)

def sha256_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

def sha512_hash(text):
    return hashlib.sha512(text.encode()).hexdigest()

@app.route('/', methods=['GET', 'POST'])
def index():
    result = {}
    if request.method == 'POST':
        original = request.form.get('original', '')
        modified = request.form.get('modified', '')

        result['sha256_original'] = sha256_hash(original)
        result['sha512_original'] = sha512_hash(original)

        result['sha256_modified'] = sha256_hash(modified)
        result['sha512_modified'] = sha512_hash(modified)

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)