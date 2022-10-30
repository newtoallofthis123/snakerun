class Term:
    def run(self):
        from flask import render_template, Flask, jsonify, request
        app = Flask(__name__)

        @app.route('/', methods=['GET'])
        def home():
            return render_template('term.html')

        @app.route('/exec', methods=['GET', 'POST'])
        def exec():
            import os
            stream = os.popen(request.values.get("cmd"))
            output = str(stream.read()).replace(
                "\n", "<br>").replace(" ", "&nbsp")
            return jsonify(output)

        import webbrowser
        webbrowser.open(f'http://localhost:5000/')
        app.run(debug=False)


print("Hello World")
