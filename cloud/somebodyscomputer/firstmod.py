#!/usr/bin/python
# Make coding more python3-ish
from __future__ import (absolute_import, division)
__metaclass__ = type

from urllib2 import URLError

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.urls import open_url


class FetchError(Exception):
    pass


class WriteError(Exception):
    pass


def fetch(url):
    try:
        stream = open_url(url)
        return stream.read()
    except URLError:
        raise FetchError("Data could not be fetched")


def write(data, dest):
    try:
        with open(dest, "w") as dest:
            dest.write(data)
    except IOError:
        raise WriteError("Data could not be written")


def save_data(mod):
    try:
        data = fetch(mod.params["url"])
        write(data, mod.params["dest"])
        mod.exit_json(msg="Data saved", changed=True)
    except (FetchError, WriteError) as err:
        mod.fail_json(msg="%s" % err)


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
