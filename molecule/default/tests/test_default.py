import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_chrony_conf_created(host):
    f1 = host.file('/etc/chrony/chrony.conf')
    f2 = host.file('/etc/chrony.conf')
    if f1.exists:
        assert f1.exists
        assert f1.contains("server")
    elif f2.exists:
        assert f2.exists
        assert f2.contains("server")
    else:
        assert False, f'{"chrony.conf file not found"}'


def test_chrony_pkg_installed(host):
    pkg = host.package("chrony")
    assert pkg.is_installed
