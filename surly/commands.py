import click
from click_shell import shell
from surly import Surly
from surly.relation import Relation


# @click.group()
@shell(prompt='surly >_ ', intro='Starting SURLY...')
def cli():
    pass


@cli.command()
@click.argument('filepath')
def read(filepath):
    """
    \b
    This command does nothing at the moment
    """
    pass


sur = Surly()
temp_relations = {}


@cli.command()
@click.argument('relation_name', nargs=1)
@click.argument('attribute_definitions', nargs=1)
def relation(relation_name, attribute_definitions):
    """
    
    Create a Relation
    
    """
    attr_defs = attribute_definitions.strip('()')
    sur.relation_command([relation_name, attr_defs])


@cli.command()
@click.argument('relation_name', nargs=1)
@click.argument('attribute_definitions', nargs=-1)
def insert(relation_name, attribute_definitions):
    """
    
    Insert Values into a Relation
    
    """
    click.echo('insert_command')
    sur.insert_command([relation_name, attribute_definitions])


@cli.command()
@click.argument('relation_name', nargs=1)
@click.option('--where', '-w', default='', help='WHERE=select condition.')
@click.option('--temp', default='', help='Temporary relation to represent selected values.')
def select(relation_name, where, temp):
    """
    
    Select Tuples from a Relation based on a specified condition.
    
    """

    if temp:
        temp_relations[temp] = Relation(temp)
        temp_relations[temp].records = sur.select_command(relation_name, condition=where)
        click.echo(temp_relations)
        return
    click.echo(sur.select_command(relation_name, condition=where))


@cli.command()
@click.option('--temp', default='', help='FROM=Name of temp relation.', nargs=1)
@click.option('--f', help='FROM=Name of relation to project from.', nargs=1)
@click.argument('attributes', nargs=-1)
def project(f, temp, attributes):
    """Project from a Relation"""
    sur.project_command(attributes, relname=f)


@cli.command()
@click.argument('rel1', nargs=1)
@click.argument('rel2', nargs=1)
@click.option('--temp', default='', help='FROM=Name of temp relation.', nargs=1)
@click.option('--where', '-w', default='', help='WHERE=select condition.', nargs=2)
def join(rel1, rel2, where, temp):
    """
    
    Join two relations based on condition
    
    """
    if temp:
        temp_relations[temp] = Relation(temp)
        temp_relations[temp].records = sur.join_command(rel1, rel2, condition=where)
        click.echo(temp_relations)
        return
    click.echo(sur.join_command(rel1, rel2, condition=where))
    # click.echo('join_command')


@cli.command()
@click.argument('relation_name', nargs=-1)
def print(relation_name):
    """
    
    Print a relation by name or use
    'print CATALOG' to view DB info
    
    """
    for name in relation_name:
        if name in temp_relations.keys():
            temp_relations[name].print_records()
        else:
            sur.print_command(name)


@cli.command()
@click.argument('name')
@click.option('--where', '-w', default='')
def delete(name, where):
    """
    
    Delete all data from a relation without deleting 
    the relation. If 'WHERE' is used, only deletes tuples
    that meet specified conditions.
    
    """
    sur.delete_command(name, condition=where)


@cli.command()
@click.argument('name')
def destroy(name):
    """
    
    Destroy a relation completely.
    
    """
    sur.destroy_command(name)
    click.echo('destroy_command')


@cli.command()
def quit():
    click.echo('quit_command')


if __name__ == '__main__':

    cli()
