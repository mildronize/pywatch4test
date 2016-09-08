# -*- coding: utf-8 -*-

import click
import time
import os

from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

from pywatch4test.pywatch4test import PathProcessor


class ModifiedHandler(PatternMatchingEventHandler):
    patterns = ["*.py"]

    def __init__(self, path_processor):
        super().__init__()
        self.path_processor = path_processor

    def on_created(self, event):
        self.path_processor.when_file_changed(event.src_path)

    #  def on_any_event(self, event):
        #  pass

    def on_modified(self, event):
        self.path_processor.when_file_changed(event.src_path)


@click.command()
@click.option('--unittest-dir', '-d', default="tests", help='Where is tests \
directory?')
@click.option('--package-name', '-p', default="", help='Your package name')
@click.option('--endswith-test', '-s', is_flag=True, help='Naming styles, if \
enable this flag, pattern is `*_test`')
def main(unittest_dir, package_name, endswith_test):
    """Console script for pywatch4test"""
    #  unittest_dir = "tests"
    #  package_name = "simple_calculator"
    startswith_test = not endswith_test

    click.echo("Running...  pywath4test")
    click.echo("")
    click.echo("Watching... *.py at {}".format(os.getcwd()))
    click.echo("Test Directory: {}/{}".format(os.getcwd(), unittest_dir))
    click.echo("-"*20)

    event_handler = ModifiedHandler(
            PathProcessor(unittest_dir, package_name, startswith_test))
    observer = Observer()
    observer.schedule(event_handler, '.', recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()
