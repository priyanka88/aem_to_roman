# Convert Integer to Roman numeral
This app converts decimal numbers to roman numerals.

# Requirements

Python 3, pip 3, Docker daemon

# Local
## Installation and How to Run

Step 1: Clone this repository. Create a virtual environment if preferred.

    $ git clone <URL here>

Step 2: Install all necessary dependencies to run:

    $ pip install -r requirements.txt

Step 3: Run the application:

	$ python app.py

Step 4: Access this url in your browser: 

	http://0.0.0.0:8080/romannumeral?query=<integer>


# Docker Container
## Installation and How to Run

Step 1: Build the docker image.
    
    $ docker build  -t aem_to_roman .

Step 2: Run the docker container with desired Host port # and Container port = 8080

    $ docker run -t -p 5500:8080 aem_to_roman

# Docker Container on AWS with Container Insights in Cloudwatch
## Installation and How to Run

Step 1: Create a repository in ECR

    $ aws ecr create-repository --repository-name to-roman-repo

Step 2: Using the repoURI from the response above, login to docker

    $ aws ecr get-login-password | docker login --username AWS --password-stdin <account#>.dkr.ecr.us-west-2.amazonaws.com/toroman-repo

Step 3: Tag the current image with readable name

    $  docker tag to-roman <account#>.dkr.ecr.us-west-2.amazonaws.com/to-roman-repo

Step 4: Push the image to ECR

    $ docker push <account#>.dkr.ecr.us-west-2.amazonaws.com/to-roman-repo

Step 5: Create a task in ECS console > Task Definitions. add Container Definition with the image we just pushed to ECR.
    I have switched Container insights ON for the Cloudwatch to have container logs in a log group. 
    Log driver is `awslogs` under log group `/ecs/to-roman-task` for debugging errors or monitoring.

Step 6: Create ECS Cluster to run this Task with default VPC, default Subnet and Security group 
    to open the Host port, specified in Container Definition in the previous step.

Step 7: Go to Public IP generated Clusters > <cluster-name> > Tasks > Task Details > Network > Public IP, the app will be running there.

    $ <public IP>:8080/romannumeral?query=<integer>


## Production level extensions/modifications

1. Create IAM role to manage ECS container and possible new containers for metrics
2. Add SSL to the container to use HTTPS
3. Add Kibana dashboard to either Cloudwatch logs or ELK stack in the same cluster for visual dashboard
4. Add rate limit on the API GET method using `flask-limiter` or similar library
5. Add load balancer in front of container (application level)
6. Observe CPU utilization periodically to maximize compute percentage usage (in this case container)
7. Add SNS notifications on failure of API call frm Cloudwatch to decrease downtime and debug

