# -*- coding: utf-8 -*-

import click
import time

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
def main(args=None):
    """Console script for pywatch4test"""
    unittest_dir = "tests"
    package_name = "simple_calculator"
    startswith_test = True

    click.echo("Running... pywath4test")

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
