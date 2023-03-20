from flask import Flask , render_template_string
app = Flask(__name__)

@app.route('/')
def score_server():
    try:
        with open('Scores.txt', 'r') as f:
            score = f.read().strip()
            return render_template_string('''                <html>
                <head>
                <title>Scores Game</title>
                </head>
                <body>
                <h1>The score is <div id="Score">{score}</div></h1>
                </body>
                </html>''',score=score)


    except Exception as e:
        return f'''
            <html>
            <head>
            <title>Scores Game</title>
            </head>
            <body>
            <h1><div id="score" style="color:red">{e}</div></h1>
            </body>
            </html>
        '''

#if __name__ == '__main__':
app.run()
