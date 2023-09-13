# ansible_B6.5.1

To run playbook create_user.yml you need to use command ansible-playbook create_user.yml --ask-vault-password

To run playbook install_postfix.yml you need to use command:

ansible-playbook install_postfix.yml --tags "init postfix" or ansible-playbook install_postfix.yml --tags "drop postfix" depending on the required task.
