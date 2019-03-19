import windows

from library._01_simple import app
if __name__ == '__main__':
    app.debug = True
    host = windows.environ.get('IP', '0.0.0.0')
    port = int(windows.environ.get('PORT', 8080))
    app.run(host=host, port=port)
