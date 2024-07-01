# google_kubernetes
instructions to deploy ml model on google_kubernetes

## Container
<P>A container is a type of software that packages up an application and all its dependencies so the application runs reliably from one computing environment to another.</P>
<P>Docker is a company that provides software (also called Docker) that allows users to build, run and manage containers. While Docker’s container are the most common, there are other less famous alternatives such as LXD and LXC that provides container solution.</P>

## Kubernetes
<P>Kubernetes is a powerful open-source system developed by Google back in 2014, for managing containerized applications. In simple words, Kubernetes is a system for running and coordinating containerized applications across a cluster of machines. It is a platform designed to completely manage the life cycle of containerized applications.</P>
<P>You need to start the right containers at the right time, figure out how they can talk to each other, handle storage considerations, and deal with failed containers or hardware. This is the problem Kubernetes is solving by allowing large numbers of containers to work together in harmony, reducing the operational burden.</P>

### Features
✔️ <b>Load Balancing:</b> Automatically distributes the load between containers.

✔️ <b>Scaling:</b> Automatically scale up or down by adding or removing containers when demand changes such as peak hours, weekends and holidays.

✔️ <b>Storage:</b> Keeps storage consistent with multiple instances of an application.

✔️ <b>Self-healing</b> Automatically restarts containers that fail and kills containers that don’t respond to your user-defined health check.

✔️ <b>Automated Rollouts</b> you can automate Kubernetes to create new containers for your deployment, remove existing containers and adopt all of their resources to the new container.

## Objective
To build and deploy a web application where the demographic and health information of a patient is entered into a web-based form which then outputs a predicted charge amount.

## Tasks
* Train and develop a machine learning pipeline for deployment.
* Build a web app using a Flask framework. It will use the trained ML pipeline to generate predictions  on new data points in real-time.
* Build a docker image and upload a container onto Google Container Registry (GCR).
* Create clusters and deploy the app on Google Kubernetes Engine.

## 10-steps to deploy a ML pipeline on Google Kubernetes Engine:
* Step 0 — Put your code in github
* Step 1 — Create a new project in GCP Console
* Step 2 — Import Project Code
    * Click the Activate Cloud Shell button at the top of the console window to open the Cloud Shell.
    * Execute the following code in Cloud Shell to clone the GitHub repository used in this tutorial.
        ```
        git clone https://github.com/AbhinavJhanwar/google_kubernetes.git
        cd google_kubernetes/product_ds
        ```
* Step 3 — Set Project ID Environment Variable
    * Execute the following code to set the PROJECT_ID environment variable. Make sure to provide project id same as in step 1.
        ```
        export PROJECT_ID=google-kubernetes-demo
        ```
* Step 4 — Build the docker image
    * Build the docker image of the application and tag it for uploading by executing the following code:
        ```
        # to build backend separately
        sudo docker build -t fastapi:v1 .
        # repeat this step in separate terminal to build frontend with below command
        sudo docker build -t streamlit:v1 .

        # build backend and frontend together
        sudo docker-compose build
        ```
    * check images using code- 
        ```
        sudo docker images
        ```
* Step 5 — Upload the container image
    * Authenticate to Container Registry (you need to run this only once):
        ```
        gcloud auth configure-docker
        ```
    * Execute the following code to upload the docker image to Google Container Registry:
        ```
        # sudo docker push <image-name>
        sudo docker push fastapi-backend:v1
        sudo docker push streamlit-frontend:v1
        ```
* Step 6 — Create Cluster
    * A cluster consists of a pool of Compute Engine VM instances, running Kubernetes.
    * Set your project ID and Compute Engine zone options for the gcloud tool:
        ```
        gcloud config set project $PROJECT_ID 
        gcloud config set compute/zone europe-west1-b
        ```
    * Create a cluster by executing the following code:
        ```
        gcloud container clusters create ds-cluster --num-nodes=2
        ```
* Step 7 — Deploy Application
   * To deploy and manage applications on a GKE cluster, you must communicate with the Kubernetes cluster management system. Execute the following command to deploy the application:
        ```
        kubectl create deployment ds-app-backend --image=fastapi-backend:v1
        kubectl create deployment ds-app-frontend --image=streamlit-frontend:v1
        ```
*  Step 8 — Expose your application to the internet
    * By default, the containers you run on GKE are not accessible from the internet because they do not have external IP addresses. Execute the following code to expose the application to the internet:
        ```
        kubectl expose deployment ds-app-backend --type=LoadBalancer --port 8000 --target-port 8000
        kubectl expose deployment ds-app-frontend --type=LoadBalancer --port 8501 --target-port 8501
        ```
* Step 9 — Check Service
    * Execute the following code to get the status of the service. EXTERNAL-IP is the web address you can use in browser to view the published app.
        ```
        kubectl get service
        ```
* Step 10 — See the app in action on http://34.71.77.61:8080


## References-
* https://towardsdatascience.com/deploy-machine-learning-model-on-google-kubernetes-engine-94daac85108b<br>