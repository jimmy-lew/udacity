from typing import List
import math


class Window:
    """
    Class for creating a window in the terminal

    Attributes:
        width (int): Width of the window
    """

    def __init__(self, width: int):
        self.width = width
        pass

    def print(self, content: str, width: int = None, new_line: bool = True):
        """
        Print a line of text in the window

        Args:
            content (str): Content to print
            width (int): Width of the window
            new_line (bool): Whether to print a new line after the content

        """

        applied_width = self.width if width is None else width
        end = '\n' if new_line else ''
        if len(content) <= applied_width - 2:
            print(f'│ {content.center(applied_width - 2)} │', end=end)
        else:
            while len(content) > applied_width - 2:
                print(f'│ {content[:applied_width - 2]} │', end=end)
                content = content[applied_width - 2:]

    def create(self, content: List[str]):
        """
        Create a window with the given content

        Args:
            content (List[str]): Content to display in the window

        """

        print(f'╭{"─" * self.width}╮')
        for line in content:
            self.print(line)
        print(f'╰{"─" * self.width}╯')

    def create_stacked(self, content: List[List[str]]):
        """
        Create a window with the given content stacked horizontally

        Args:
            content (List[List[str]]): Content to display in the window

        """

        filtered_content = [filled_list for filled_list in content if len(filled_list) > 0]
        no_windows = len(filtered_content)
        width = int(self.width / no_windows) - (1 + math.floor(no_windows / 5))
        for i in range(no_windows):
            print(f'╭{"─" * width}╮', end='')
        print()
        for i in range(max([len(x) for x in filtered_content])):
            for j in range(no_windows):
                try:
                    self.print(filtered_content[j][i], width, False)
                except IndexError:
                    print(f'│ {" " * width} │', end='')
            print()
        for i in range(no_windows):
            print(f'╰{"─" * width}╯', end='')
        print()


if __name__ == '__main__':
    window = Window(80)
    window.create_stacked([
        ['Hello', 'World'],
        ['Hello', 'World'],
    ])
