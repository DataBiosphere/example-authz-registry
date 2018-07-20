import os

import yaml


def lint():
    with open('user.yaml', 'r') as f:
        data = yaml.load(f)
    # pyyaml auto sort
    with open('user.yaml', 'w') as f:
        yaml.dump(data, f)


if __name__ == '__main__':
    lint()
