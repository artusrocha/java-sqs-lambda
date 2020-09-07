rm -rf build
rm packaged.yml
mkdir build
cp app/*.py build/
python -m venv build
pip install requests

aws cloudformation package \
    --template-file template.yml \
    --s3-bucket $BUILD_OUTPUT_BUCKET \
    --output-template-file packaged.yml &&

aws cloudformation deploy --template packaged.yml \
    --capabilities CAPABILITY_IAM --stack-name $1
