from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
@app.route('/about')
def home():
    return render_template('index.html')

app.run(debug=True)
print('end')