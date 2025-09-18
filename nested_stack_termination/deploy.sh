

aws cloudformation create-stack \
  --stack-name demo-nested-bad-prop \
  --template-body file://root.yaml \
  --parameters ParameterKey=NestedTemplateURL,ParameterValue=https://s3.us-east-1.amazonaws.com/www.printhelloworld.org/nested_template.yaml