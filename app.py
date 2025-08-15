from flask import Flask, render_template




app = Flask(__name__)




@app.route('/')
def home():
    return render_template('main.html')




@app.route('/candle')
def candle():
    return render_template('candle.html')




@app.route('/LoveMe')
def LoveMe():
    return render_template('LoveMe.html')




@app.route('/dinner')
def dinner():
    return render_template('dinner.html')




@app.route('/Happy')
def Happy():
    return render_template('Happy.html')




@app.route('/noodle')
def noodle():
    return render_template('noodle.html')




@app.route('/plz')
def plz():
    return render_template('plz.html')




@app.route('/present')
def present():
    return render_template('present.html')





@app.route('/propose')
def propose():
    return render_template('propose.html')





@app.route('/reject')
def reject():
    return render_template('reject.html')





@app.route('/success')
def success():
    return render_template('success.html')




@app.route('/thanks')
def thanks():
    return render_template('thanks.html')





if __name__ == '__main__':
    app.run(debug=True)
