import os
from jinja2 import Template

os.chdir('/Users/pav/Documents/worka/gitRepo/pv_repo/python/jinja')

if __name__ == '__main__':
    with open('template.json') as f:
        template = Template(f.read())

    print(template.render(myValue='Ahoj', dalsi=' Ada to skoro umi!'))
    print(template.render({'myValue': 'Ahoj', 'dalsi': ' Ada to skoro umi!'}))
