Attached the screen shot of Utilization from Grafana

Steps to follow:
****************
From GIT bash:

ssh -i <your pub key> <oci_user>@<public IP of that instance> -L 3000:localhost:3000

sudo yum install https://dl.grafana.com/oss/release/grafana-5.4.21.x86_64.rpm

sudo grafana-cli plugins install oci-datasource

sudo chmod 555 ./grafana/plugins/oci-datasource/dist/oci-plug_linux

sudo systemctl start grafana-server

http://localhost:3000/
  
  
