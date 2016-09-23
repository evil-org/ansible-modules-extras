#!/usr/bin/python
# Make coding more python3-ish
from __future__ import (absolute_import, division)
__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.urls import open_url


def fetch(url):
    stream = open_url(url)

    return stream.read()


def write(data, dest):
    raise NotImplementedError


def save_data(mod):
    data = fetch(mod.params["url"])

    if write(data, mod.params["dest"]):
        mod.exit_json(msg="Data saved", changed=True)
    else:
        mod.fail_json(msg="Data could not be saved")


def main():
    mod = AnsibleModule(
        argument_spec=dict(
            url=dict(required=True),
            dest=dict(required=False, default="/tmp/firstmod")
        )
    )

    save_data(mod)


if __name__ == '__main__':
    main()
