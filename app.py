from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flashing messages

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        #instead of processing form data, just print it for now
        first_name = request.form.get('first-name')
        last_name = request.form.get('last-name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        print(f"Contact form submission: {first_name} {last_name}, {email}: {message}")
        
        
        return redirect(url_for('about'))

@app.route('/become-a-partner')
def become_partner():
    return render_template('become_partner.html')

@app.route('/partners')
def partners():
    return render_template('partners.html')

@app.route('/student-resources')
def student_resources():
    return render_template('student_resources.html')

if __name__ == '__main__':
    app.run(debug=True) 