import argparse
import json
import logging
from dateutil.relativedelta import relativedelta
from typing import Dict , List

from duckdb    import IOException
from jinja2 import Template


from database_manager import (
    connect_to_database,
    close_database_connection,
    execute_query,



    
)