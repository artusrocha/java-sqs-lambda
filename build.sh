#!/bin/bash 

rm -rf build
mkdir -p build/package

cp app/*.py build/package/
#python -m venv build
pip install -r requirements.txt -t build/package

aws --profile teste \
    cloudformation package \
    --template-file template.yml \
    --s3-bucket $BUILD_OUTPUT_BUCKET \
    --output-template-file build/packaged.yml &&

aws --profile teste \
    cloudformation deploy \
    --template build/packaged.yml \
    --capabilities CAPABILITY_IAM --stack-name $1
