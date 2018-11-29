from azure.keyvault import KeyVaultClient, KeyVaultAuthentication
from azure_helper import crendetial as cr


def auth_callback(server, resource, scope):
    credentials = cr().get_dev_credential(
        resource="https://vault.azure.net"
    ).get_credentials()
    token = credentials.token
    return token['token_type'], token['access_token']


if __name__ == '__main__':
    client = KeyVaultClient(KeyVaultAuthentication(auth_callback))

    print(client)

    secret_bundle = client.get_secret(
        "https://abx-vault.vault.azure.net/",
        "azure-db-user--pwd",
        "0beb68502a5944258b0f5500deda6bee")

    print(secret_bundle.value)
