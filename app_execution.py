import windows

from library._01_simple import app
# from library_html_inside_view import app
# from library_template_str_inside_view import app
# from library_template_outside_view import app
if __name__ == '__main__':
    app.debug = True
    host = windows.environ.get('IP', '0.0.0.0')
    port = int(windows.environ.get('PORT', 8080))
    app.run(host=host, port=port)
