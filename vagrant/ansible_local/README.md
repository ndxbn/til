https://www.vagrantup.com/docs/provisioning/ansible_local.html

`vagrant up`

```
C:\Users\ndxbn\Documents\repos\github.com\ndxbn\til\vagrant\ansible_local\local>vagrant rsync && vagrant provision
==> default: Rsyncing folder: /cygdrive/c/Users/ndxbn/Documents/repos/github.com/ndxbn/til/vagrant/ansible_local/ => /vagrant
==> default: Running provisioner: ansible_local...
Vagrant has automatically selected the compatibility mode '2.0'
according to the Ansible version installed (2.5.5).

Alternatively, the compatibility mode can be specified in your Vagrantfile:
https://www.vagrantup.com/docs/provisioning/ansible_common.html#compatibility_mode
    default: Running ansible-playbook...

PLAY [all] *********************************************************************

TASK [Gathering Facts] *********************************************************
ok: [localhost]

TASK [debug] *******************************************************************
ok: [localhost] => {
    "msg": "Hello world!"
}

PLAY RECAP *********************************************************************
localhost                  : ok=2    changed=0    unreachable=0    failed=0
```

## Requirements

- Oracle Virtual Box
- Vagrant
