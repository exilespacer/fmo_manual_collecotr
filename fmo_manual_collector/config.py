# director path of output
import os
DIR_HOME = os.path.dirname(__file__)
DIR_HOME = '.' if DIR_HOME=='' else DIR_HOME

DIR_FMO_MANUAL_DATA = f'{DIR_HOME}/data'

DIR_DATA_HTML = f'{DIR_FMO_MANUAL_DATA}/html'
if not os.path.exists(DIR_DATA_HTML):
    os.mkdir(DIR_DATA_HTML)

# for fmo html contents
DIR_DATA_FMO_HTML_CONTENTS = f'{DIR_FMO_MANUAL_DATA}/fmo_html_contents'
if not os.path.exists(DIR_DATA_FMO_HTML_CONTENTS):
    os.mkdir(DIR_DATA_FMO_HTML_CONTENTS)

# for fmo machine items
DIR_DATA_FMO_MACHINE_ITEMS = f'{DIR_FMO_MANUAL_DATA}/fmo_machine_items'
if not os.path.exists(DIR_DATA_FMO_MACHINE_ITEMS):
    os.mkdir(DIR_DATA_FMO_MACHINE_ITEMS)

# for fmo manual items
DIR_DATA_FMO_MANUAL_ITEMS = f'{DIR_FMO_MANUAL_DATA}/fmo_manual_items'
if not os.path.exists(DIR_DATA_FMO_MANUAL_ITEMS):
    os.mkdir(DIR_DATA_FMO_MANUAL_ITEMS)
