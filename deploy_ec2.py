import argparse
import boto3
import yaml
import sys

## LOAD CLOUDFORMATION TEMPLATE

def load_template(file_path):
    with open(file_path, 'r') as file:
        return file.read()

CLOUDFORMATION_TEMPLATE = load_template('EC2LaunchTemplate.yaml')

## DEPLOY THE STACK 
def deploy_stack(base_name):
    # Convert YAML template to JSON for CloudFormation
    cloudformation = boto3.client('cloudformation')
    stack_name = f"{base_name}"

    # Load the template
    template = CLOUDFORMATION_TEMPLATE
    try:
        # Create CloudFormation stack
        response = cloudformation.create_stack(
            StackName=stack_name,
            TemplateBody=template,
            Parameters=[
                {"ParameterKey": "BaseName", "ParameterValue": base_name},
            ],
            Capabilities=['CAPABILITY_NAMED_IAM'],
        )
        print(f"Stack creation initiated: {response['StackId']}")
    except Exception as e:
        print(f"Error creating stack: {e}")

## MAIN FUNCTION 
def main():
    parser = argparse.ArgumentParser(description="Deploy an EC2 instance with CloudFormation")
    parser.add_argument("-n", "--name", type=str, required=True, help="Base name for the created artifacts")

    args = parser.parse_args()

    base_name = args.name

    # Deploy stack with provided parameters
    deploy_stack(base_name)

if __name__ == "__main__":
    main()
