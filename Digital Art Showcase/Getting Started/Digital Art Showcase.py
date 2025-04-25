from flask import Flask
app = Flask(__name__)

# Home route
@app.route("/")
@app.route("/home")
def home():
    return """
    <h1>Welcome to The Artist's Haven</h1>
    <p>Explore an inspiring collection of creative works from talented artists around the world.</p>
    """

# About route
@app.route("/about")
def about():
    return """
    <h1>About The Artist's Haven</h1>
    <p>This platform is dedicated to celebrating the diverse world of art, where artists can showcase their unique visions and creations.</p>
    """

# Gallery route
@app.route("/gallery")
def gallery():
    return """
    <h1>The Artist's Haven</h1>
    <p>Browse a curated collection of masterpieces, from traditional paintings to innovative digital expressions.</p>
    """

# Artists route
@app.route("/artists")
def artists():
    return """
    <h1>Meet the Artists</h1>
    <p>Discover the passionate creators behind the artwork, and delve into their stories and creative processes.</p>
    """

if __name__ == '__main__':
    app.run(debug=True)
