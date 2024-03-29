class Md:
    def __init__(self, name):
        self.name = name

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
                    "# This is a boiler plate code generated by snakerun\nStart Typing Below")
                return "# This is a boiler plate code generated by snakerun\n#Start Typing Below"

        @app.route('/', methods=['GET'])
        def home():
            return "<h1 style='font-family: consolas, monospace; font-size: 84px; text-align: center;'>🐍 SNAKE RUN <br><br> There is nothing to see here!</h1>"

        @app.route('/save', methods=['POST'])
        def save():
            name = request.form.get('name')
            content = request.form.get('text')
            with open(name, 'w') as file:
                file.write(content)
                return f"<h1 style='font-family: consolas, monospace; font-size: 84px; text-align: center;'>🐍 SNAKE RUN <br><br> Saved file {self.name}!</h1>"

        @app.route(f'/{self.name}', methods=['GET', 'POST'])
        def main():
            import os
            return render_template('md.html', filename=self.name, filename_adv=f'{os.getcwd()}\{self.name}', content=read(f'{os.getcwd()}\{self.name}'))
        
        import webbrowser
        webbrowser.open(f'http://localhost:5000/{self.name}')
        app.run(debug=False)