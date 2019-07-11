# aws-serverless
Getting started on developing a serverless architecture in AWS (Lambda, API gateway, DynamoDB, etc.) 

## Getting Started
### Commands

Installing aws command line tool:
```
python -m pip install --upgrade awscli
```

Installing sam command line tool (1 of the following):
```
python -m pip install --upgrade aws-sam-cli
```

Setting up IAM access keys locally:
```
aws configure
```

## AWS S3
### Commands

Copy a directory containing a lambda function to AWS S3
```
aws s3 sync lambdas s3://jadams-demo-lambdas
```

Zip a lambda function directory, copy to s3
```
zip -r9 ../zipped/pyhello.zip pyhello
aws s3 cp pyhello.zip s3://jadams-demo-lambdas
```

## AWS Lambda
### Commands

Create a lambda function
```
aws lambda create-function --function-name pyhello --runtime python3.7 --role arn:aws:iam::282236276875:role/lambda-role --handler pyhello.hello_func --code S3Bucket=jadams-demo-lambdas,S3Key=pyhello.zip
```

Update lambda function code or configuration
```
aws lambda update-function-code --function-name pyhello --s3-bucket jadams-demo-lambdas --s3-key pyhello.zip
```

locally invoke an aws lambda function, piping stdout to base64 decoding
```
aws lambda invoke --function-name pyhello --log-type Tail --output text output.txt | cut -f 2 | base64 -D
```

## AWS Serverless Application Model (SAM)
### Commands

```
sam init --runtime python3.7 # initiate a sam application
cd sam-app # change directory
sam local start-api # start local application server
sam package --output-template-file packaged.yaml --s3-bucket jadams-demo-lambdas # package the directory and send the lambda function to the s3 bucket
sam deploy --template-file packaged.yaml --stack-name sam-app --capabilities CAPABILITY_IAM --region us-east-2 # deploy the sam application
```

## Links
[AWS Lambda Tutorial](https://aws.amazon.com/getting-started/tutorials/run-serverless-code)

[AWS SAM (Serverless Application Model) Client](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install-mac.html)

[AWS Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)

[AWS Lambda Command Line User Guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html)

[AWS IAM Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html)

[AWS SAM Developer Guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-quick-start.html)