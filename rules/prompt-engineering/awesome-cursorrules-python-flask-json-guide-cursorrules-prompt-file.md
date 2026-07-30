---
name: awesome-cursorrules-python-flask-json-guide-cursorrules-prompt-f
description: "Cursor rules for Python Flask development with JSON guide."
category: prompt-engineering
source_repo: PatrickJS/awesome-cursorrules
source_path: "rules/python-flask-json-guide-cursorrules-prompt-file.mdc"
source_url: https://github.com/PatrickJS/awesome-cursorrules/blob/HEAD/rules/python-flask-json-guide-cursorrules-prompt-file.mdc
---

This project is heavily reliant on our custom Drawscape Factorio python module.

Here is code examples of how to use the module:

```python
from drawscape_factorio import create as createFactorio
from drawscape_factorio import importFUE5

with open('/path/to/exported-entities.json', 'r') as file:
    json_data = json.load(file)
    data = importFUE5(json_data)
    result = createFactorio(data, {
        'theme_name': 'default',
        'color_scheme': 'main',
        'show_layers': ['assets', 'belts', 'walls', 'rails', 'electrical', 'spaceship']
    })

with open(output_file_name, 'w') as f:
    f.write(result['svg_string'])

---

**Source:** [`PatrickJS/awesome-cursorrules`](https://github.com/PatrickJS/awesome-cursorrules) → `rules/python-flask-json-guide-cursorrules-prompt-file.mdc`
