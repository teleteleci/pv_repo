class crendetial():

    __key = None
    __client = None

    def __init__(self, tenant_id=None, client=None, key=None, resource=None):
        self.tenant_id = tenant_id
        self.__client = client
        self.__key = key
        self.resource = resource

    @classmethod
    def get_dev_credential(self, resource=None):
        TENANT_ID = '5675d321-19d1-4c95-9684-2c28ac8f80a4'
        # Your Service Principal App ID
        CLIENT = '21d897cd-cfce-4cb3-bc95-7ddad3b6a818'
        # Your Service Principal Password
        KEY = '13e6372f-f910-4645-b001-12a575a5fb75'

        c = crendetial(
            tenant_id=TENANT_ID,
            client=CLIENT,
            key=KEY,
            resource=resource
        )
        return c

    def get_credentials(self):
        from azure.common.credentials import ServicePrincipalCredentials
        credentials = None

        credentials = ServicePrincipalCredentials(
            client_id=self.__client,
            secret=self.__key,
            tenant=self.tenant_id,
            resource=self.resource
        )

        return credentials

    def debug(self):
        print('resource {}'.format(self.resource))
        print('tenant_id {}'.format(self.tenant_id))
        print('client {}'.format(self.__client))
        print('key {}'.format(self.__key))
