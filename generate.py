import glob
import yaml
import models
from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

for path in glob.glob('data/services/*/service.yaml'):
    
    file = open(path, 'rb')
    data = yaml.safe_load(file)

    service = models.Service()
    service.name = data["name"]
    service.description = data["description"]

    service_template = env.get_template('service.html')
    print(service_template.render(service=service))