import os
from jinja2 import Template

# constant
dblist = ["cbs", "app", "crm", "hst"]

os.chdir('/Users/pav/Documents/worka/gitRepo/pv_repo/python/jinja')

if __name__ == '__main__':
    with open('grRow.json') as f:
        template = Template(f.read())

    print(template.render(elements=dblist))
