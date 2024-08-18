import click
from deppy.analyzer import analyze_dependencies
from deppy.report import generate_report


@click.group()
def cli():
    """Deppy: Dependency Analyzer for Python."""
    pass


@cli.command()
@click.option(
    '-r', '--requirements',
    type=click.Path(),
    help='Path to requirements.txt'
)
def analyze(requirements):
    """Analyze dependencies."""
    analyze_dependencies(requirements)


@cli.command()
@click.option(
    '-o', '--output',
    type=click.Path(),
    help='Output file for the report'
)
def report(output):
    """Generate a dependency report."""
    generate_report(output)


if __name__ == "__main__":
    cli()
