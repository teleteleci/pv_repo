from azure.servicebus import ServiceBusService as sb

from azure.common.credentials import ServicePrincipalCredentials

# Tenant ID for your Azure Subscription
TENANT_ID = '5675d321-19d1-4c95-9684-2c28ac8f80a4'

# Your Service Principal App ID
CLIENT = 'f9d91d93-d1f3-4117-b8ee-db04ad0497cf'

# Your Service Principal Password
KEY = 'Vsu4'

credentials = ServicePrincipalCredentials(
    client_id = CLIENT,
    secret = KEY,
    tenant = TENANT_ID
)
