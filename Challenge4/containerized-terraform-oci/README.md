Build and run the docker image
*******************************
##docker build -t oracle_farook/terraform-oci:3.96.0 .
docker build -t <<The docker file>>

docker run \
  --interactive --tty --rm \
  --volume "$PWD":/data \
  oracle_farook/terraform-oci:3.96.0 "$@"

$terraform init
$terraform plan
$ alias terraform-oci="docker run --interactive --tty --rm --volume "$PWD":/data oracle_farook/terraform-oci:3.96.0 terraform"
