# Import the necessary libraries
import flask
import jinja2  # Import Jinja2 for template rendering
import morse_code

# Create a Flask app
app = flask.Flask(__name__)

# Define a route to handle the user's request
@app.route("/")
def index():
    # Get the user's message from the query parameter 'message'
    message = flask.request.args.get("message", "")

    # Convert the message to Morse code
    morse_message = morse_code.convert_message_to_morse(message)

    # Render the template with the generated Morse code
    template = jinja2.Environment(loader=jinja2.PackageLoader(__name__, "templates")).get_template("index.html")
    return template.render(morse_code=morse_message)

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
  
