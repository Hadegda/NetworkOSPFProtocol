from commands import *

_help_str = '''
This is a simulation "Open Shortest Path First protocol" work

Commands:
  `ping start_id finish_id`    transits way from router node to another throw shortest path, ids must be int
  `scheme schemeName`   adds couple of routers, schemeName must be one of 'ring', 'star' or  'bus'
  `help`    prints help information
  `exit`    correct program terminates 

'''

def form_Command(args):
    name = args[0]
    if name == 'scheme':
        scheme_names ={
            'ring': schemeRing,
            'star': schemeStar,
            'bus': schemeBus,
            'mesh': schemeMesh
        }

        if args[1] not in scheme_names.keys():
            print('Wrong command, print \"help\" for information')
            return Command()

        return scheme_names[args[1]]()

    if name == 'ping':
        return PingCommand(int(args[1]), int(args[2]))
    if name == 'help':
        print(_help_str)
        return Command()
    elif name == 'exit':
        return ExitCommand()


def parse_args(args: list):
    commands = {
        'scheme': 1,
        'ping': 2,
        'help': 0,
        'exit': 0
    }

    command = args[0]
    if command not in commands.keys():
        print('Wrong command, print \"help\" for information')
        return Command()

    Command_info = commands.get(command)
    if len(args) - 1 != Command_info:
        print('Wrong parameters number, print \"help\" for information')
        return Command()

    return form_Command(args)


def cmd_parse(str_Command: str):
    try:
        Command = parse_args(str_Command.strip('\n').split(' '))
        return Command

    except SystemExit:
        pass