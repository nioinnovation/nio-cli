import unittest
from unittest.mock import patch
from nio_cli.commands import Server


class TestCommandServer(unittest.TestCase):

    def test_server_run(self):
        """This will execute nio as a subprocess with executable name nio_run
        """
        with patch('nio_cli.commands.server.subprocess.Popen') as Popen:
            options = {}
            options['--daemon'] = False
            options['-d'] = False
            options['--ip'] = '127.0.0.1'
            options['--port'] = 8181
            options['--run'] = True
            Server(options).run()
            self.assertEqual(Popen.call_args[0][0], ['nio_run'])

    def test_server_full(self):
        """This will execute nio as a subprocess with executable name nio_full
        """
        with patch('nio_cli.commands.server.subprocess.Popen') as Popen:
            options = {}
            options['--daemon'] = False
            options['-d'] = False
            options['--ip'] = '127.0.0.1'
            options['--port'] = 8181
            options['--full'] = True
            Server(options).run()
            self.assertEqual(Popen.call_args[0][0], ['nio_full'])

    def test_server_default(self):
        """This will execute nio as a subprocess with executable name nio_run
        as default when no arguments are specified
        """
        with patch('nio_cli.commands.server.subprocess.Popen') as Popen:
            options = {}
            options['--daemon'] = False
            options['-d'] = False
            options['--ip'] = '127.0.0.1'
            options['--port'] = 8181
            Server(options).run()
            self.assertEqual(Popen.call_args[0][0], ['nio_run'])
