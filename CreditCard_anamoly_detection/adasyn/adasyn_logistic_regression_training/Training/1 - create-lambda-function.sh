aws lambda create-function \
    --region us-east-1 \
    --function-name fraud-detection2-adasyn-logistic-training-testing_new \
    --role arn:aws:iam::676101537567:role/wcc-ds-iam-role-lambda-execution \
    --code ImageUri=676101537567.dkr.ecr.us-east-1.amazonaws.com/fraud-detection-testing:adasyn-logistic-training-testing\
    --package-type Image \
    --memory-size 10240 \
    --timeout 900 \