from flask import Flask, render_template, request, jsonify

# Create Flask app
app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return render_template("index.html")


# Command route
@app.route("/command", methods=["POST"])
def command():

    data = request.json
    text = data["command"].lower()

    image = ""

    if "cat" in text:
        image = "cat.jpg"

    elif "car" in text:
        image = "car.jpg"

    elif "tree" in text:
        image = "tree.jpg"

    elif "monkey" in text:
        image = "monkey.jpg"

    elif "lion" in text:
        image = "lion.jpg"

    elif "tiger" in text:
        image = "tiger.jpg"

    elif "mouse" in text:
        image = "mouse.jpg"

    elif "computer" in text:
        image = "computer.jpg"

    elif "elephant" in text:
        image = "elephant.jpg"

    elif "earphone" in text:
        image = "earphone.jpg"

    elif "python" in text:
        image = "python.jpg"

    return jsonify({"image": image})


# Run the application
if __name__ == "__main__":
    app.run(debug=True)