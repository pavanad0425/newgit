import boto3
import json

def get_ec2_price(instance_type, region='us-east-1'):
    pricing_client = boto3.client('pricing')

    response = pricing_client.get_products(
        ServiceCode='AmazonEC2',
        Filters=[
            {'Type': 'TERM_MATCH', 'Field': 'location', 'Value': region},
            {'Type': 'TERM_MATCH', 'Field': 'instanceType', 'Value': instance_type}
        ]
    )

    prices = []
    for product in response['PriceList']:
        terms = json.loads(product)['terms']['OnDemand']
        for term in terms:
            price_dimensions = terms[term]['priceDimensions']
            for dimension in price_dimensions:
                price = price_dimensions[dimension]['pricePerUnit']['USD']
                prices.append(float(price))

    if prices:
        return sum(prices) / len(prices)
    else:
        return None

def get_s3_price(storage_type, region='us-east-1'):
    pricing_client = boto3.client('pricing')

    response = pricing_client.get_products(
        ServiceCode='AmazonS3',
        Filters=[
            {'Type': 'TERM_MATCH', 'Field': 'location', 'Value': region},
            {'Type': 'TERM_MATCH', 'Field': 'storageClass', 'Value': storage_type}
        ]
    )

    prices = []
    for product in response['PriceList']:
        terms = json.loads(product)['terms']['OnDemand']
        for term in terms:
            price_dimensions = terms[term]['priceDimensions']
            for dimension in price_dimensions:
                price = price_dimensions[dimension]['pricePerUnit']['USD']
                prices.append(float(price))

    if prices:
        return sum(prices) / len(prices)
    else:
        return None

def get_kms_price(region='us-east-1'):
    pricing_client = boto3.client('pricing')

    response = pricing_client.get_products(
        ServiceCode='AWSKeyManagementService',
        Filters=[
            {'Type': 'TERM_MATCH', 'Field': 'location', 'Value': region}
        ]
    )

    prices = []
    for product in response['PriceList']:
        terms = json.loads(product)['terms']['OnDemand']
        for term in terms:
            price_dimensions = terms[term]['priceDimensions']
            for dimension in price_dimensions:
                price = price_dimensions[dimension]['pricePerUnit']['USD']
                prices.append(float(price))

    if prices:
        return sum(prices) / len(prices)
    else:
        return None

# Example usage
ec2_instance_type = 't2.micro'
s3_storage_type = 'Standard'
region = 'us-east-1'

ec2_price = get_ec2_price(ec2_instance_type, region)
s3_price = get_s3_price(s3_storage_type, region)
kms_price = get_kms_price(region)

if ec2_price is not None:
    print(f"Estimated EC2 price for {ec2_instance_type} in {region}: ${ec2_price:.4f} per hour")
else:
    print(f"Price not available for EC2 instance {ec2_instance_type} in {region}")

if s3_price is not None:
    print(f"Estimated S3 price for storage type {s3_storage_type} in {region}: ${s3_price:.4f} per GB-month")
else:
    print(f"Price not available for S3 storage type {s3_storage_type} in {region}")

if kms_price is not None:
    print(f"Estimated KMS price in {region}: ${kms_price:.4f} per key operation")
else:
    print(f"Price not available for KMS in {region}")
