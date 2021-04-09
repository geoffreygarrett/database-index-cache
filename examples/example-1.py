import sys
from dbci.utils import yaml2dict

sys.path.insert(0, "../")

if __name__ == "__main__":
    print(yaml2dict("index.yaml"))
