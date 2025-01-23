from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>مرحبًا بك في موقعي البسيط</h1><p>هذا نص يعرض باستخدام Flask</p>'

if __name__ == '__main__':
    app.run(debug=True)
