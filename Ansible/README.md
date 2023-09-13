# Ansible
An example of running a Docker installation:

    ansible-playbook -i inventory.txt -l app playbook.yml

An example of running a Postgresql installation:

    ansible-playbook -i inventory.txt -l database playbook.yml
