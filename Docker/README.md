# ScoutGaming

This folder consists of Dockerfile, python script, and requirements.txt

### To build a Docker image run the next command:

```docker build -t <image_name> .```

### To run Standalone Docker container and set ENV variables run next command and enter necessary values
As was requested sensitive data we use ENV variables

```docker run -d -e "API_KEY=<api_key_value>" -e "PAGE_ID=<page_id_value>" -e "METRIC_ID=<metric_id_value>" <image_name>```

### To run script using K8s Deployment service follow next steps:
- build Docker image for K8s deployment
  
  ```docker build -t <your-image-name> .```

- push the image to registry: local or other
  
  ```docker push <your-image-name>```

- edit container image in deployment.yaml spec on 'your-image-name'
  
  ```spec.template.spec.containers[].image```

- run K8s service:
  
    ```kubectl create -f deployment.yaml```

### Memory limits
I've tested the script for memory usage as a standalone Docker container and as Kubernetes deployment on my local machine using Docker and Minikube.
In both situations, memory usage has never been over 20Mb per one container. 
Based on this experience I set the requested memory per one pod 25Mb and limited memory - 32Mb. 
In case when the pod requested more than a limited memory pod will be killed and redeployed a new pod with default limits.
Also, each situation is special and need to consider K8s resources and customer requests