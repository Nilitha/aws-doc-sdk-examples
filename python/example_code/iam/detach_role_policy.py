# Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

import boto3


# Create IAM client
iam = boto3.client('iam')

# Detach a role policy
iam.detach_role_policy(
    PolicyArn='arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess',
    RoleName='AmazonDynamoDBFullAccess'
)
 

# snippet-comment:[These are tags for the AWS doc team's sample catalog. Do not remove.]
# snippet-sourcedescription:[detach_role_policy.py demonstrates how to detach a role policy.]
# snippet-keyword:[Python]
# snippet-sourcesyntax:[python]
# snippet-sourcesyntax:[python]
# snippet-keyword:[AWS SDK for Python (Boto3)]
# snippet-keyword:[Code Sample]
# snippet-keyword:[AWS Identity and Access Management (IAM)]
# snippet-service:[iam]
# snippet-sourcetype:[full-example]
# snippet-sourcedate:[]
# snippet-sourceauthor:[jschwarzwalder (AWS)]

