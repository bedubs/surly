import click
from click_shell import shell
from surly import Surly


# @click.group()
@shell(prompt='surly >_ ', intro='Starting SURLY...')
def cli():
    pass


@cli.command()
@click.argument('filepath')
def read(filepath):
    """Takes a file as an argument"""
    pass


sur = Surly()


@cli.command()
@click.argument('relation_name', nargs=1)
@click.argument('attribute_definitions', nargs=1)
def relation(relation_name, attribute_definitions):
    """Create a Relation"""
    # click.echo('Relation Name: {}\nAttribute Definitions: {}'.format(relation_name, attribute_definitions))
    attr_defs = attribute_definitions.strip('()')
    # click.echo(attr_defs.split(', '))
    sur.relation_command([relation_name, attr_defs])


@cli.command()
@click.argument('relation_name', nargs=1)
@click.argument('attribute_definitions', nargs=-1)
def insert(relation_name, attribute_definitions):
    """Insert Values into a Relation"""
    click.echo('insert_command')
    sur.insert_command([relation_name, attribute_definitions])
    # click.echo('Relation Name: {}\nAttribute Definitions: {}'.format(relation_name, attribute_definitions))


@cli.command()
@click.argument('relation_name', nargs=1)
@click.option('--where', '-w', help='WHERE=select condition.')
def select(relation_name, where):
    """Select Tuples from a Relation based on a specified condition."""
    click.echo('Relation: {}'.format(relation_name))
    click.echo('WHERE: {}'.format(where))
    click.echo('select_command')
    # sur.select_command(relation_name, where)


@cli.command()
@click.option('--temp', help='FROM=Name of temp relation.', nargs=1)
@click.option('--f', help='FROM=Name of relation to project from.', nargs=1)
@click.argument('attributes', nargs=-1)
def project(f, temp, attributes):
    """Project from a Relation"""
    sur.project_command(attributes, relname=f, temp=temp)


@cli.command()
@click.argument('relation_a', nargs=1)
@click.argument('relation_b', nargs=1)
@click.option('--temp', '-t', help='FROM=Name of temp relation.', nargs=1)
@click.option('--where', '-w', help='WHERE=select condition.', nargs=1)
def join(relation_a, relation_b, temp, where):
    """Join two relations based on condition"""
    sur.join_command(relation_a, relation_b, where, temp=temp)
    click.echo('join_command')


@cli.command()
@click.argument('name', nargs=-1)
def print(name):
    sur.print_command(name)


@cli.command()
@click.argument('name')
@click.option('--where', '-w')
def delete(name, where):
    """Delete all data from a relation without deleting 
    the relation. If 'WHERE' is used, only deletes tuples
    that meet specified conditions."""
    sur.delete_command(name, condition=where)


@cli.command()
@click.argument('name')
def destroy(name):
    """Destroy a relation completely."""
    sur.destroy_command(name)
    click.echo('destroy_command')


@cli.command()
def quit():
    click.echo('quit_command')


if __name__ == '__main__':

    cli()
