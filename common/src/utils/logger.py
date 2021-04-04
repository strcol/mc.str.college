import datetime
import sys

try:
    import colorama
except ImportError:
    pass

LEVEL_ERROR = 1
LEVEL_WARNING = 2
LEVEL_INFO = 3
LEVEL_DEBUG = 4

use_colors = 'colorama' in sys.modules


class Logger:
    def __init__(self, enabled=True, level=LEVEL_DEBUG, file=None,
                 print_function=print):
        self.enabled = enabled
        self.level = level
        self.file = file
        self.print = print_function

        if use_colors:
            colorama.init()

    def _log_file(self, message):
        if not self.file:
            return
        with open(self.file, 'a', encoding='utf-8') as file:
            file.write(message + '\n')

    def info(self, message):
        if not self.enabled or self.level < LEVEL_INFO:
            return
        timestamp = datetime.datetime.now().isoformat()
        msg_nc = f'[{timestamp}] [INFO] {message}'
        if use_colors:
            msg = (f'{colorama.Fore.CYAN}[{timestamp}]{colorama.Fore.GREEN}'
                   f' [INFO] {colorama.Fore.WHITE}{message}'
                   f'{colorama.Style.RESET_ALL}')
        else:
            msg = msg_nc
        self._log_file(msg_nc)
        self.print(msg)

    def error(self, message):
        if not self.enabled or self.level < LEVEL_ERROR:
            return
        timestamp = datetime.datetime.now().isoformat()
        msg_nc = f'[{timestamp}] [ERROR] {message}'
        if use_colors:
            msg = (f'{colorama.Fore.CYAN}[{timestamp}]{colorama.Fore.RED}'
                   f' [ERROR] {colorama.Fore.WHITE}{message}'
                   f'{colorama.Style.RESET_ALL}')
        else:
            msg = msg_nc
        self._log_file(msg_nc)
        self.print(msg)

    def warning(self, message):
        if not self.enabled or self.level < LEVEL_WARNING:
            return
        timestamp = datetime.datetime.now().isoformat()
        msg_nc = f'[{timestamp}] [WARNING] {message}'
        if use_colors:
            msg = (f'{colorama.Fore.CYAN}[{timestamp}]{colorama.Fore.YELLOW}'
                   f' [WARNING] {colorama.Fore.WHITE}{message}'
                   f'{colorama.Style.RESET_ALL}')
        else:
            msg = msg_nc
        self._log_file(msg_nc)
        self.print(msg)

    def debug(self, message):
        if not self.enabled or self.level < LEVEL_DEBUG:
            return
        timestamp = datetime.datetime.now().isoformat()
        msg_nc = f'[{timestamp}] [DEBUG] {message}'
        if use_colors:
            msg = (f'{colorama.Fore.CYAN}[{timestamp}]{colorama.Fore.MAGENTA}'
                   f' [DEBUG] {colorama.Fore.WHITE}{message}'
                   f'{colorama.Style.RESET_ALL}')
        else:
            msg = msg_nc
        self._log_file(msg_nc)
        self.print(msg)
