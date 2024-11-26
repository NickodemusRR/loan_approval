# ML Zoomcamp 2024 Capstone Project 1 - Loan Approval

A midterm project from [ml-zoomcamp](!http://mlzoomcamp.com/) 2024. 

During this midterm we have learned 
1. Machine Learning Model: Classification and Regression. 
2. Deployment in an web application using Flask
3. Containerization using Docker

This project served to showcase what we have learning up to the moment.

This project using the [Loan Approval Classification](!https://www.kaggle.com/datasets/taweilo/loan-approval-classification-data/data) dataset which can be downloaded from [kaggle](!https://www.kaggle.com/datasets/taweilo/loan-approval-classification-data/data).

This dataset has two target variables that can be use to create machine learning model:
1. Loan Status -> "0": "rejected; "1": approved can be used to train classification model.
2. Credit Score can be used to train regression model.

We used this dataset to train a classification model for this midterm project. Based on the feature given, the model will predict whether the loan application is approved or rejected.

Conda is used as virtual environment and the depedencies needed was provided in [requirement.txt](!./requirements.txt) file.
```bash
conda create --name ml-zoomcamp
conda activate ml-zoomcamp
pip install -r requirements.txt
```

We used Docker container and build an image from the [Dockerfile](!./Dockerfile)
```bash
docker build -t midterm-project1 .
```

Run the docker image using this command:
```bash
docker run -it --rm -p 9696:9696 midterm-project1
```

Flags explanations:
* `--name`: give the name to the created conda environment
* `-r`: installing pip packages listed in the requirements.txt file
* `-t`: specifying tag name
* `-it`: allowing access to the terminal inside Docker image
* `--rm`: removing the image from the system after we have exited the image
* `-p`: mapping the port `9696` in our machine to the port `9696` inside Docker image  
