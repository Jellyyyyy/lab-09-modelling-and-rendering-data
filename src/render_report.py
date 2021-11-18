#####
# Setting environment variable. NOTE: This is not a production-safe practice.
# This is only acceptable because this is a lab.
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '//c/Users/yaoyu/musa509-0829-1d970995ed94.json'
#####

import geopandas as gpd
import pandas as pd
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

template_root = Path(__file__).resolve().parent / 'templates'
output_root = Path(__file__).resolve().parent.parent / 'output'

def main():
    # Download the map data.
    ...

    # Download the chart data.
    ...

    # Download the population density list data.
    ...

    # Render the data into the template.
    env = Environment(loader=FileSystemLoader(str(template_root)))
    template = env.get_template('index.html')
    output = template.render(
        # TEMPLATE DATA GOES HERE...
    )

    # Save the rendered output to a file in the "output" folder.
    with open(output_root / 'index.html', mode='w') as outfile:
        outfile.write(output)

if __name__ == '__main__':
    main()
