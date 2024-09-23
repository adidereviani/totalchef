from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Ensure the secret key is set for session handling

# Default language is English
DEFAULT_LANGUAGE = 'he'

# Helper function to get the current language
def get_language():
    return session.get('language', DEFAULT_LANGUAGE)

# Route to switch languages
@app.route('/switch-language/<lang>')
def switch_language(lang):
    session['language'] = lang
    return redirect(request.referrer or url_for('home'))

# Homepage route with language support
@app.route('/')
def home():
    lang = get_language()
    return render_template(f'index_{lang}.html')

# Other routes
@app.route('/products')
def products():
    lang = get_language()
    return render_template(f'products_{lang}.html')

@app.route('/points-of-sale')
def points_of_sale():
    lang = get_language()
    return render_template(f'points_of_sale_{lang}.html')

@app.route('/contact')
def contact():
    lang = get_language()
    return render_template(f'contact_{lang}.html')

@app.route('/about')
def about():
    lang = get_language()
    return render_template(f'about_{lang}.html')

if __name__ == '__main__':
    app.run(debug=True)
