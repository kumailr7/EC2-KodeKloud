# EC2-KodeKloud

This project provides an automated way to create an EC2 instance on AWS using a CloudFormation template, orchestrated by a Python script. The script leverages `boto3` and `argparse` for AWS automation and command-line argument parsing.

## Prerequisites

- **Python Environment**: Make sure you have Python 3.x installed.
- **Required Python Packages**:
  - `boto3`
  - `argparse`
- **SSH Key Pair**:
  - Generate a public and private SSH key pair.
  - Import the public key into the AWS console (KodeKloud AWS Playground or your AWS account).
- **AWS Credentials**: Configure your AWS credentials (e.g., using `aws configure` or environment variables).

## Setup Instructions

1. **Clone the Repository**
    ```bash
    git clone https://github.com/kumailr7/EC2-KodeKloud.git
    cd EC2-KodeKloud
    ```

2. **Install Python Dependencies**
    ```bash
    pip install boto3 argparse
    ```

3. **Prepare SSH Key Pair**
    - Generate an SSH key pair (if you don’t have one):
      ```bash
      ssh-keygen -t rsa -b 2048 -f my-key
      ```
    - Import the public key (`my-key.pub`) into the AWS Console under EC2 > Key Pairs.

4. **Configure AWS Credentials**
    ```bash
    aws configure
    ```
    Or set the following environment variables:
    ```bash
    export AWS_ACCESS_KEY_ID=your_access_key
    export AWS_SECRET_ACCESS_KEY=your_secret_key
    export AWS_DEFAULT_REGION=your_region
    ```

## Usage

1. **Edit the CloudFormation Template**
    - Update the template file as needed (see sample in the repo or provide your own).

2. **Run the Python Script**
    ```bash
    python your_script.py --stack-name my-ec2-stack --template-file ec2_template.yaml --key-name my-key
    ```
    - Replace `your_script.py` with your actual script name.
    - Replace `my-key` with your imported AWS EC2 key pair name.

3. **Script Arguments**
    - `--stack-name`: The name for the CloudFormation stack.
    - `--template-file`: Path to your CloudFormation template YAML/JSON file.
    - `--key-name`: The EC2 Key Pair name to use.

## Notes

- Ensure your AWS user has permissions to create EC2 instances and CloudFormation stacks.
- The AWS region and account should match those used in the KodeKloud AWS Playground.
- For more details, customize or check the provided Python/CloudFormation templates.
