import click
from surly import Surly


@click.group()
def cli():
    pass


sur = Surly()


@cli.command()
@click.argument('relation_name', nargs=1)
@click.argument('attribute_definitions', nargs=1)
def relation_command(relation_name, attribute_definitions):
    """Create a Relation"""
    click.echo('Relation Name: {}\nAttribute Definitions: {}'.format(relation_name, attribute_definitions))
    attr_defs = attribute_definitions.strip('()')
    click.echo(attr_defs.split(', '))


@cli.command()
@click.argument('relation_name', nargs=1)
@click.argument('attribute_definitions', nargs=-1)
def insert_command(relation_name, attribute_definitions):
    """Insert Values into a Relation"""
    print('insert_command')
    click.echo('Relation Name: {}\nAttribute Definitions: {}'.format(relation_name, attribute_definitions))


@cli.command()
@click.option('--f', help='FROM=Name of relation to select from.', nargs=1)
@click.argument('attributes', nargs=-1)
def select_command(f, attributes):
    """Select Tuples from a Relation"""
    click.echo('Attributes: {}'.format(attributes))
    click.echo('FROM: {}'.format(f))
    print('select_command')


@cli.command()
@click.option('--f', help='FROM=Name of relation to project from.', nargs=1)
@click.argument('attributes', nargs=-1)
def project_command(f, attributes):
    """Project from a Relation"""
    click.echo('Attributes: {}'.format(attributes))
    click.echo('FROM: {}'.format(f))
    click.echo('project_command')


@cli.command()
def join_command():
    print('join_command')


@cli.command()
@click.argument('name', nargs=-1)
def print_command(name):
    click.echo('PRINT {}'.format(name))
    sur.print_catalog()


@cli.command()
def delete_command():
    print('delete_command')


@cli.command()
def destroy_command():
    print('destroy_command')


@cli.command()
def quit_command():
    print('quit_command')


if __name__ == '__main__':

    cli()
