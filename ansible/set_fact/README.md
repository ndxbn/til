`set_fact` がグローバル変数を使っている気がしたので、その検証

[ホストごとに共有な facts](https://docs.ansible.com/ansible/latest/reference_appendices/glossary.html#term-facts) に `set` しているので、ホストごとのスコープになる。実質グローバル変数かなって感じ。

`ansible-playbook -vv -i local -c local site.yml` の実行結果は、以下の通り。

```
ansible-playbook 2.5.5
  config file = /etc/ansible/ansible.cfg
  configured module search path = [u'/home/vagrant/.ansible/plugins/modules', u'/usr/share/ansible/plugins/modules']
  ansible python module location = /usr/lib/python2.7/site-packages/ansible
  executable location = /usr/bin/ansible-playbook
  python version = 2.7.5 (default, Apr 11 2018, 07:36:10) [GCC 4.8.5 20150623 (Red Hat 4.8.5-28)]
Using /etc/ansible/ansible.cfg as config file
statically imported: /dev/shm/foo/roles/inner/tasks/assert.yml
statically imported: /dev/shm/foo/roles/inner/tasks/assert.yml

PLAYBOOK: site.yml ***********************************************************************************************************************************************************************************************************************************************************
1 plays in site.yml

PLAY [all] *******************************************************************************************************************************************************************************************************************************************************************

TASK [Gathering Facts] *******************************************************************************************************************************************************************************************************************************************************
task path: /dev/shm/foo/site.yml:1
ok: [localhost]
META: ran handlers

TASK [inner : assrtion] ******************************************************************************************************************************************************************************************************************************************************
task path: /dev/shm/foo/roles/inner/tasks/assert.yml:1
ok: [localhost] => {
    "changed": false, 
    "msg": "All assertions passed"
}

TASK [inner : systemd configuration] *****************************************************************************************************************************************************************************************************************************************
task path: /dev/shm/foo/roles/inner/tasks/main.yml:4
included: /dev/shm/foo/roles/inner/tasks/systemd.yml for localhost
included: /dev/shm/foo/roles/inner/tasks/systemd.yml for localhost

TASK [inner : const service_name] ********************************************************************************************************************************************************************************************************************************************
task path: /dev/shm/foo/roles/inner/tasks/systemd.yml:1
ok: [localhost] => {"ansible_facts": {"service_name": "redis_7001"}, "changed": false}

TASK [inner : debug print] ***************************************************************************************************************************************************************************************************************************************************
task path: /dev/shm/foo/roles/inner/tasks/systemd.yml:4
ok: [localhost] => {
    "msg": "service name is redis_7001, port num is 7001"
}

TASK [inner : const service_name] ********************************************************************************************************************************************************************************************************************************************
task path: /dev/shm/foo/roles/inner/tasks/systemd.yml:1
ok: [localhost] => {"ansible_facts": {"service_name": "redis_7002"}, "changed": false}

TASK [inner : debug print] ***************************************************************************************************************************************************************************************************************************************************
task path: /dev/shm/foo/roles/inner/tasks/systemd.yml:4
ok: [localhost] => {
    "msg": "service name is redis_7002, port num is 7002"
}

TASK [inner : assrtion] ******************************************************************************************************************************************************************************************************************************************************
task path: /dev/shm/foo/roles/inner/tasks/assert.yml:1
fatal: [localhost]: FAILED! => {
    "assertion": "service_name is undefined", 
    "changed": false, 
    "evaluated_to": false
}
...ignoring

TASK [assert : assrtion] *****************************************************************************************************************************************************************************************************************************************************
task path: /dev/shm/foo/roles/assert/tasks/main.yml:1
fatal: [localhost]: FAILED! => {
    "assertion": "service_name is undefined", 
    "changed": false, 
    "evaluated_to": false
}
...ignoring
META: ran handlers
META: ran handlers

PLAY RECAP *******************************************************************************************************************************************************************************************************************************************************************
localhost                  : ok=10   changed=0    unreachable=0    failed=0   
```
