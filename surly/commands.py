import click
from click_shell import shell
from surly import Surly
import readin


# @click.group()
@shell(prompt='surly >_ ', intro='Starting SURLY...')
def cli():
    pass


@cli.command()
@click.argument('filepath')
def read(filepath):
    """Takes a file as an argument"""
    readin.read_file(filepath)


sur = Surly()


@cli.command()
@click.argument('relation_name', nargs=1)
@click.argument('attribute_definitions', nargs=1)
def relation(relation_name, attribute_definitions):
    """Create a Relation"""
    click.echo('Relation Name: {}\nAttribute Definitions: {}'.format(relation_name, attribute_definitions))
    attr_defs = attribute_definitions.strip('()')
    click.echo(attr_defs.split(', '))


@cli.command()
@click.argument('relation_name', nargs=1)
@click.argument('attribute_definitions', nargs=-1)
def insert(relation_name, attribute_definitions):
    """Insert Values into a Relation"""
    click.echo('insert_command')
    click.echo('Relation Name: {}\nAttribute Definitions: {}'.format(relation_name, attribute_definitions))


@cli.command()
@click.argument('relation_name', nargs=1)
@click.option('--where', '-w', help='WHERE=select condition.')
def select(relation_name, where):
    """Select Tuples from a Relation based on a specified condition."""
    click.echo('Relation: {}'.format(relation_name))
    click.echo('WHERE: {}'.format(where))
    click.echo('select_command')


@cli.command()
@click.option('--f', help='FROM=Name of relation to project from.', nargs=1)
@click.argument('attributes', nargs=-1)
def project(f, attributes):
    """Project from a Relation"""
    click.echo('Attributes: {}'.format(attributes))
    click.echo('FROM: {}'.format(f))
    click.echo('project_command')


@cli.command()
def join():
    click.echo('join_command')


@cli.command()
@click.argument('name', nargs=-1)
def print(name):
    click.echo('PRINT {}'.format(name))
    sur.print_command(name)


@cli.command()
def delete():
    click.echo('delete_command')


@cli.command()
def destroy():
    click.echo('destroy_command')


@cli.command()
def quit():
    click.echo('quit_command')


if __name__ == '__main__':

    cli()
