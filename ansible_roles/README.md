# ansible_roles
To start the installation of nginx and php-fpm on different hosts, use the command:

ansible-playbook playbook.yml --ask-vault-password -e "host=IP_ADDRESS_PHP-FPM_SERVER" -i inventory.txt
