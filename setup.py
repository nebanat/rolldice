from setuptools import setup

setup(
    name='RollDice-CLI',
    version='1.0',
    packages=['cli', 'cli.commands'],
    include_package_data=True,
    install_requires=[
        'click',
    ],
    entry="""
        [console_scripts]
        rolldice=cli.cli:cli
    """,
)
