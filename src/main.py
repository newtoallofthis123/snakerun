from base64 import decode


def read(filename):
    import os
    with open(f'{os.getcwd()}\{filename}', 'r', encoding="utf8") as file:
        file_contents = file.read()
        import json
        file_mapper = json.loads(open(
            f'{os.path.realpath(__file__).replace("main.py", "")}data.json', 'r').read())["file_stuff"]
        file_ext = file_mapper["." + str(filename).split('.')[1]]
        from rich.console import Console
        from rich.syntax import Syntax
        console = Console()
        syntax = Syntax(file_contents, file_ext)
        console.print(f":eyes:Showing contents of file: {filename}")
        console.print(syntax)


def write(filename):
    from write import Write
    import os
    from rich.console import Console
    console = Console()
    import json
    file_mapper = json.loads(
        open(f'{os.path.realpath(__file__).replace("main.py", "")}data.json', 'r').read())["file_stuff"]
    file_ext = file_mapper["." + str(filename).split('.')[1]]
    write = Write(f'{filename}', file_ext)
    Console().print(f'Running Server for editing {filename}')
    write.up()


def editor(language):
    from write import Editor
    from rich.console import Console
    console = Console()
    editor = Editor(language)
    Console().print(f'Running Server for editing in {language}')
    editor.up()


def term():
    from term import Term
    term = Term()
    term.run()


def run(filename):
    from rich.console import Console

    def runfile(filename):
        from sys import platform
        import os
        filename = f'{os.getcwd()}\{filename}'
        if platform == "linux" or platform == "linux2":
            os.system(f'python3 {filename}')
        elif platform == "darwin":
            os.system(f'python3 {filename}')
        elif platform == "win32":
            try:
                os.system(f'python {filename}')
            except:
                os.system(f'python3 {filename}')
    import threading
    try:
        threads = list()
        Console().print("Starting Terminal Console", style='red')
        Console().print(f"Showing output for file {filename}", style='green')
        print("_____________________________________")
        thread = threading.Thread(target=runfile, args=(filename,))
        threads.append(thread)
        thread.start()

        for port, thread_1 in enumerate(threads):
            thread_1.join()
    except:
        print('Something went wrong')


def copy(filename):
    import pyperclip
    from rich.console import Console
    import os
    filename = f'{os.getcwd()}\{filename}'
    with open(filename, "r") as file:
        file_content = file.read()
        pyperclip.copy(str(file_content))
        Console().print(f"Copied file {filename}", style='green')


def delete(filename):
    import os
    from rich.console import Console
    try:
        filename = f'{os.getcwd()}\{filename}'
        os.remove(filename)
        Console().print(f'Deleted File {filename}', style='green')
    except:
        Console().print(f'Unable to delete file {filename}', style='red')


if __name__ == '__main__':
    import fire
    fire.Fire()
