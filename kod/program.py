import click
# @click.command()
# @click.option('-i')
# @click.option('-n')
# def run(i,n):
#     print(f'Witaj {i} {n} w radosnym świecie Pythona!')
#
# run()

# @click.command()
# @click.option('-i',required=True)
# @click.option('-n', required=True)
# def run(i,n):
#     print(f'Witaj {i} {n} w radosnym świecie Pythona!')
#
# run()

@click.command()
@click.option('-i',prompt=True)
@click.option('-n', prompt=True)
def run(i,n):
    print(f'Witaj {i} {n} w radosnym świecie Pythona!')

run()