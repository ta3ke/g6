# -*- coding: utf-8 -*- #

import os
from typing import List, Any, Optional


def changeHtmlToJinja(path: str):
    for filename in os.listdir(path):
        filepath = path + os.sep + filename
        if os.path.isdir(filepath):
            changeHtmlToJinja(filepath)
        elif os.path.isfile(filepath):
            fname, ext = os.path.splitext(filepath)
            if ".html" == ext:
                print(filepath, "=>", fname + ".html.jinja")
                os.rename(filepath, fname + ".html.jinja")


if __name__ == "__main__":
    changeHtmlToJinja("./templates")
    changeHtmlToJinja("./admin/templates")
