from flask import Flask, render_template, request, jsonify
import secrets
import string

app = Flask(__name__)


def generate_password(length: int, non_alpha_chars: int) -> str:
    if length < 1:
        length = 8
    if non_alpha_chars < 0:
        non_alpha_chars = 0
    if non_alpha_chars > length:
        non_alpha_chars = length

    alpha_chars = string.ascii_letters + string.digits
    special_chars = string.punctuation

    alpha_count = length - non_alpha_chars

    password_chars = []
    for _ in range(alpha_count):
        password_chars.append(secrets.choice(alpha_chars))
    for _ in range(non_alpha_chars):
        password_chars.append(secrets.choice(special_chars))

    secrets.SystemRandom().shuffle(password_chars)

    return ''.join(password_chars)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    length = int(data.get('length', 12))
    non_alpha = int(data.get('nonAlpha', 2))
    password = generate_password(length, non_alpha)
    return jsonify({'password': password})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
