sudo apt install apache2-utils

htpasswd -c auth user1

kubectl create configmap nginx --from-file=nginx.conf

kubectl  create secret generic basic-auth --from-file=auth

kubectl apply -f ./first-pod.yaml
