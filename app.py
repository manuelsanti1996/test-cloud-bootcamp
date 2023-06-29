from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    a = 4
    print("Hello!", a)
    return render_template('test-0.html')

def test_1():
    print("test_1")
    return render_template('test-1.html')

if __name__ == "__main__":
    app.run(debug=True)
