import os, yaml


class GetData(object):
    """数据驱动"""
    def __init__(self):
        pass

    def get_yml_data(self, name):
        with open("./Data" + os.sep + name, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
