from not_flask import NotFlask

if __name__ == '__main__':
    app = NotFlask()

    @app.route('/')
    def index():
        return 'Hello World'

    print(app.serve('/'))