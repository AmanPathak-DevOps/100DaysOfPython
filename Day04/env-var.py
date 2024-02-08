import os

print(os.getenv('TF_VAR_AWS_REGION'))
print(os.getenv('PATH'))

endpoint = os.getenv('TF_VAR_ENDPOINT')
print(endpoint)