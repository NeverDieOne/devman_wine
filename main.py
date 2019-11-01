from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from utils import get_age, drink_parse


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html'])
)
template = env.get_template('template.html')


rendered_page = template.render(
    time=get_age(),
    drinks=drink_parse('wine')
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)


server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
