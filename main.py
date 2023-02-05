from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def generate_even_numbers():
    """Render a form to take n as input and generate n even numbers."""
    if request.method == 'POST':
        n = int(request.form.get('n'))
        even_numbers = [i for i in range(2, (n * 2) + 1, 2)]
        return render_template('even_numbers.html', numbers=even_numbers)
    return render_template('input_form.html')

if __name__ == '__main__':
    app.run(debug=True)
