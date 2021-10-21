This Maven code structure was created using the maven-archetype-quickstart archetype via the following command:

**mvn archetype:generate -DgroupId=com.example.helloworld -DartifactId=dropwizard-helloworld -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false**

The code in this repository roughly follows the Dropwizard example code on-line.

Dropwizard is an example of an embedded container application server. In traditonal Application Server contexts, you start your server and deploy your compiled application into it. In an embedded container context, you embed a lightweight container, in this case Jetty with your application.

Dropwizard is a lightweight framework that uses Jetty for HTTP, Jersey for REST and Jackson for JSON. It is everything you need to deploy a simple REST-based Web Service.

**A quick overview of the code:**

Configuration Class - HelloWorldConfiguration is a subclass of Configuration which specifies environment-specific parameters. These parameters are housed in a YAML configuaration file called hello-world.yaml. Jackson does the magic to map contents from the yaml file back and forth into the Java world. Application Class - HelloWorldApplication is a sublcass of Application (the core of the Dropwizard application) and is parametrized with HelloWorldConfiguaration. Representation Class - in short, a JSON representation needs to conform to RFC 1149 which specifies that things should look like the following. Saying provides the representation of this response. { "id": 1, "content": "Hi!" }

Dropwizard applications are typically built as fat jars using the maven-shade plug-in. This is essentially a self-contained jar - app code + dependency code - that can be dropped somewhere and run. This type of logic will produce a dependency-reduced pom so, if and when, the app and pom are published, this will provide a different view of how to build vs how to consume this application. Some other magic happens here like stripping digital signatures, collating service manifest data and setting the MainClass to be run when the application is started via java -jar.

To build the application, type:

mvn package To run the application, type:

**java -jar target/dropwizard-helloworld-1.0-SNAPSHOT.jar server hello-world.yml**

To query some sayings, try accessing:

http://localhost:8080/hello-world

or

http://localhost:8080/hello-world?name=Successful+Dropwizard+User

and at the Admin Interface at http://localhost:8081/
