import boto3
'''

export AWS_ACCESS_KEY_ID="ASIATGJHPQP4ZIYZCPNB"

export AWS_SECRET_ACCESS_KEY="IP2qkxvervTKfR2X9YgZbzBLl0gKrd/fAkaK6ASJ"

export AWS_SESSION_TOKEN="IQoJb3JpZ2luX2VjEDQaCXVzLWVhc3QtMSJIMEYCIQCeqQn1O09CDoedvKz9zP1mQOZDpVVlxpFeydn/xpic0AIhAJXn6w/Ku3bX3ZrqXVMvI/D0ejW3VABaGHDfmtTrNsEnKp0DCLz//////////wEQBBoMMjE5NjYzMDA4NzYxIgwqMDKWF6l5fla5zaUq8QJGLDEiztI/e9kp3m3fL48scJiTSbXpefHPHXy8KoZpxHmNpwyvvVgn4haMJC1izXuur9MPjdglax0NvQfSvHhzYbvIPpW5dqAbpIkTqgpFGEguM2b8I12JV38WT+U47HZ0f7lWFg8HYFaT+v79qpBKKIyAeoONqwEgSvWKoeuIEX7dYeoCCcA5ckcP+gzOKBz5blllN+N1E1FKURsiBu8kMHiBUfw/L4rIDiIxOkBVnpbBOYL7TL5PjAYPxFNIDMvJddGoIkW9i6p+DXm9uMJGgETlyI/0GihJPli8MN9X+s4uD7FZ1Iqq1N1tGKPEplAB2TBxK6jRocRoikZLpvaMxmHBtQWiPtuUkMLAQmDf+2in6g4eBQg3h2ix1eknK/1LWb6sVT39MQZz+FiO0FFySaGgNFAT408E6qY8eV1OGmaKK+wzf0jR7fy5c9Uz33c7v6rGN26lZhS/lqMfdzVntg8/VDS+l2PA2u5FVfYbbBIwqNK6iwY6pQHQNo9uwC+eV8vntz7yErIIe2fnWldEOBxarXzcElSkwgkdyYoOgWUww51DBACRdhJMG213CkaGH11Tw8Qr8O2U82C1cSZ1tcjSgZD/exF5Da9jo5vNGusTqMq/91Ay0lTRJTDFUMKMeqLGvTcp3oEa5sQBsSr2P+oybvgj2H2JVM4Vm6++X71zLsl0fYUSLDqSGSUc0/zPv21SilOv0XIbzsTCvuc="

'''

idp = boto3.client('cognito-idp',region_name='us-east-1')

# idp = boto3.client('cognito-idp', 
#                       aws_access_key_id='ASIATGJHPQP4ZIYZCPNB',
#                       aws_secret_access_key='IP2qkxvervTKfR2X9YgZbzBLl0gKrd/fAkaK6ASJ',
#                       region_name='us-east-1'
#                       )

def remove_user_from_group(
    user_pool_id: str,
    group_name: str,
    username: str
) -> dict:
    """
    Removes the user from group

    Args:
        user_pool_id (str): The UserPool id.
        group_name (str): The group name.
        username (str): The username to remove from the group.

    Returns:
        [type]: dict
    """

    respone = idp.admin_remove_user_from_group(
        UserPoolId=user_pool_id,
        Username=username,
        GroupName=group_name
    )
    print(respone)
    print(type(respone))

# UserPoolId='uat-user-pool'
UserPoolId='us-east-1_7nWvxejUP'
GroupName='ak-test'
Username='680169b3-9a3e-4a42-8d3a-a1add7f705bc'

remove_user_from_group(UserPoolId, GroupName, Username)