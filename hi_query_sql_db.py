#!/usr/bin/env python

import click
from dblib.querydb import querydb

#build a click group
@click.group()
def cli():
    """A simple CLI to query a SQL from Walmart database to search weekly sales that includes holidays or non-hoildays"""

#build a click command
@cli.command()
@click.option("--holiday", default="1", help="Please type 0 for non-holidays, 1 for holidays to check weekly sales.")
def cli_query(holiday):
    """Execute a SQL query from Walmart database to search weekly sales that includes holidays or non-hoildays"""
    querydb(holiday)
  
  #run the CLI
if __name__ == "__main__":
    cli()

