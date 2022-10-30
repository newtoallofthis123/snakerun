class Write:
    def __init__(self, name, language):
        import os
        self.name = name
        self.language = language

    def up(self):
        from flask import render_template, Flask, request
        app = Flask(__name__)

        def read(filename):
            try:
                file = open(filename, 'r')
                file_contents = file.read()
                file.close()
                return file_contents
            except:
                file = open(filename, 'w')
                file.write(
                    "#This is a boiler plate code generated by snakerun\nStart Typing Below")
                return "#This is a boiler plate code generated by snakerun\n#Start Typing Below"

        @app.route('/', methods=['GET'])
        def home():
            return "<h1 style='font-family: consolas, monospace; font-size: 84px; text-align: center;'>🐍 SNAKE RUN <br><br> There is nothing to see here!</h1>"

        @app.route('/save', methods=['POST'])
        def save():
            name = request.form.get('name')
            content = request.form.get('content')
            with open(name, 'w') as file:
                file.write(content)
                return f"<h1 style='font-family: consolas, monospace; font-size: 84px; text-align: center;'>🐍 SNAKE RUN <br><br> Saved file {self.name}!</h1>"

        @app.route(f'/{self.name}', methods=['GET', 'POST'])
        def main():
            import os
            return render_template('home.html', filename=self.name, filename_adv=f'{os.getcwd()}\{self.name}', language=self.language, content=read(f'{os.getcwd()}\{self.name}'))

        import webbrowser
        webbrowser.open(f'http://localhost:5000/{self.name}')
        app.run(debug=False)


class Editor:
    def __init__(self, language):
        self.language = language

    def up(self):
        from flask import render_template, Flask, request
        app = Flask(__name__)

        @app.route('/', methods=['GET'])
        def home():
            return render_template("editor.html", language=self.language)

        @app.route('/save', methods=['POST'])
        def save():
            name = request.form.get('name')
            content = request.form.get('content')
            with open(name, 'w') as file:
                file.write(content)
                return f"<h1 style='font-family: consolas, monospace; font-size: 84px; text-align: center;'>🐍 SNAKE RUN <br><br> Saved file {name}!</h1>"

        import webbrowser
        webbrowser.open(f'http://localhost:5000')
        app.run(debug=False)