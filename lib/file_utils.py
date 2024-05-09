# -*- coding: utf-8 -*- #

import os


def changeHtmlFilesToJinja(root_path: str):
    """
    .html 템플릿 파일 -> .html.jinja로 변경

    Args:
        path (str): _description_
    """
    for filename in os.listdir(root_path):
        filepath = root_path + os.sep + filename
        if os.path.isdir(filepath):
            changeHtmlFilesToJinja(filepath)
        elif os.path.isfile(filepath):
            fname, ext = os.path.splitext(filepath)
            if ".html" == ext:
                print(filepath, "=>", fname + ".html.jinja")
                os.rename(filepath, fname + ".html.jinja")


if __name__ == "__main__":
    changeHtmlFilesToJinja("./templates")
    changeHtmlFilesToJinja("./admin/templates")
