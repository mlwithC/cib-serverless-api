# Serverless Message Application on AWS

## Overview

A serverless web application built on AWS that allows users to submit messages through a web interface. The application uses AWS Lambda, API Gateway, DynamoDB, and S3 Static Website Hosting. A GitHub Actions CI/CD pipeline automatically deploys frontend changes to S3.

## Architecture

```text
User
  ↓
S3 Static Website
  ↓
API Gateway
  ↓
AWS Lambda
  ↓
DynamoDB
```

## Features

* Submit messages through a web interface
* Store messages in DynamoDB
* Serverless backend using AWS Lambda
* REST API using API Gateway
* Static website hosting using Amazon S3
* Automated frontend deployment using GitHub Actions
* Fully cloud-native architecture

## AWS Services Used

### Amazon S3

* Static website hosting
* Frontend file storage
* Public website access

### Amazon API Gateway

* REST API endpoint creation
* Request routing to Lambda

### AWS Lambda

* Serverless backend processing
* Message validation and storage

### Amazon DynamoDB

* NoSQL database
* Stores submitted messages

### AWS IAM

* Permissions management
* Secure service access

## Project Structure

```text
cib-serverless-api/
│
├── .github/
│   └── workflows/
│       └── deploy.yml
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── lambda/
│   └── lambda_function.py
│
└── README.md
```

## CI/CD Pipeline

```text
Developer
   ↓
Git Push
   ↓
GitHub Actions
   ↓
AWS S3
   ↓
Updated Website
```

Whenever changes are pushed to the main branch, GitHub Actions automatically deploys the frontend files to the S3 bucket.

## Workflow

1. User enters a message on the website
2. Frontend sends a POST request to API Gateway
3. API Gateway invokes Lambda
4. Lambda processes the request
5. Message is stored in DynamoDB
6. Success response is returned to the user

## Screenshots (Added)

### Frontend Website

### API Gateway Route

### Lambda Function

### DynamoDB Table

### GitHub Actions Deployment

## Skills Demonstrated

* AWS Lambda
* Amazon API Gateway
* Amazon DynamoDB
* Amazon S3
* IAM Permissions
* Git & GitHub
* GitHub Actions
* CI/CD Pipelines
* Serverless Architecture
* REST APIs
* JavaScript
* Python
* Cloud Deployment

## Learning Outcomes

Through this project, I learned:

* How serverless applications work
* Building and deploying REST APIs
* Hosting static websites on AWS
* Connecting AWS services together
* Automating deployments using GitHub Actions
* Managing cloud resources securely
* Designing cloud-native architectures

## Future Improvements

* User authentication using Amazon Cognito
* Message retrieval functionality
* Input validation and error handling
* Monitoring with Amazon CloudWatch
* Infrastructure provisioning using Terraform


