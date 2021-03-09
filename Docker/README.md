# ScoutGaming

This folder consists of Dockerfile, python script, and requirements.txt

### To build a Docker image run the next command:

```docker build -t <image_name> .```

### To run Docker container and set ENV variables run next command and enter necessary values
As was requested sensitive data we use ENV variables

```docker run -d -e "API_KEY=<api_key_value>" -e "PAGE_ID=<page_id_value>" -e "METRIC_ID=<metric_id_value>" <image_name>```
