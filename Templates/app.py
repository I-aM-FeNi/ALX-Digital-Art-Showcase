from flask import Flask, render_template, url_for

app = Flask(__name__)

# Dummy data for artists' posts, tailored to your Web App vision
posts = [
    {
        'artist_name': 'Luna Vortex',
        'title': 'Abstract Dreams',
        'content': 'Exploring the vivid landscapes of the subconscious mind.',
        'date_posted': 'September 24, 2024'
    },
    {
        'artist_name': 'Orion Starlight',
        'title': 'Cosmic Wonders',
        'content': 'A deep dive into the mysteries of space through digital art.',
        'date_posted': 'September 22, 2024'
    },
    {
        'artist_name': 'Aether Mirage',
        'title': 'Illusions of Light',
        'content': 'Playing with light and shadows to craft surreal environments.',
        'date_posted': 'September 20, 2024'
    }
]

# Home route, following the tutorial's structure
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

# About route, simple as in the tutorial
@app.route("/about")
def about():
    return render_template('about.html', title='About')

# Main entry point, as in the tutorial
if __name__ == '__main__':
    app.run(debug=True)
