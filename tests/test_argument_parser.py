import pytest
from thefrick.argument_parser import Parser
from thefrick.const import ARGUMENT_PLACEHOLDER


def _args(**override):
    args = {'alias': None, 'command': [], 'yes': False,
            'help': False, 'version': False, 'debug': False,
            'force_command': None, 'repeat': False,
            'enable_experimental_instant_mode': False,
            'shell_logger': None}
    args.update(override)
    return args


@pytest.mark.parametrize('argv, result', [
    (['thefrick'], _args()),
    (['thefrick', '-a'], _args(alias='frick')),
    (['thefrick', '--alias', '--enable-experimental-instant-mode'],
     _args(alias='frick', enable_experimental_instant_mode=True)),
    (['thefrick', '-a', 'fix'], _args(alias='fix')),
    (['thefrick', 'git', 'branch', ARGUMENT_PLACEHOLDER, '-y'],
     _args(command=['git', 'branch'], yes=True)),
    (['thefrick', 'git', 'branch', '-a', ARGUMENT_PLACEHOLDER, '-y'],
     _args(command=['git', 'branch', '-a'], yes=True)),
    (['thefrick', ARGUMENT_PLACEHOLDER, '-v'], _args(version=True)),
    (['thefrick', ARGUMENT_PLACEHOLDER, '--help'], _args(help=True)),
    (['thefrick', 'git', 'branch', '-a', ARGUMENT_PLACEHOLDER, '-y', '-d'],
     _args(command=['git', 'branch', '-a'], yes=True, debug=True)),
    (['thefrick', 'git', 'branch', '-a', ARGUMENT_PLACEHOLDER, '-r', '-d'],
     _args(command=['git', 'branch', '-a'], repeat=True, debug=True)),
    (['thefrick', '-l', '/tmp/log'], _args(shell_logger='/tmp/log')),
    (['thefrick', '--shell-logger', '/tmp/log'],
     _args(shell_logger='/tmp/log'))])
def test_parse(argv, result):
    assert vars(Parser().parse(argv)) == result
