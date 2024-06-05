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