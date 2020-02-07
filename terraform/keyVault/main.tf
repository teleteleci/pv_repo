variable "environment" {
    type = object(
        {
            subscription = string
            envPrefix = string
            tenantId = string
        }
    )
}

variable "rg" {
    type = object(
        {
            domain = string
            location = string
            tags = map(any)
        }
    )
}

variable "privileges" {
    type = object(
        {
            azure_aad_object_id = string
            keyvault = object(
                {
                    comments = string
                    principalId = string
                    permissions = object(
                        {
                            key_permissions = list(any)
                            secret_permissions = list(any)
                        }
                    )
                }
            )
        }
    )
}

provider "azurerm" {
    version = "=1.37.0"
}

# Create a resource group if it doesn’t exist
resource "azurerm_resource_group" "resource_group" {
    name = "${var.environment.envPrefix}-${var.rg.domain}-kv-rg"
    location = "${var.rg.location}"

    tags = "${var.rg.tags}"
}

resource "azurerm_key_vault" "example" {
    name                        = "${var.environment.envPrefix}-${var.rg.domain}-kv"
    location                    = "${var.rg.location}"
    resource_group_name         = "${var.environment.envPrefix}-${var.rg.domain}-kv-rg"
    enabled_for_disk_encryption = true
    tenant_id                   = "${var.environment.tenantId}"
    sku_name = "standard"

    access_policy {
        tenant_id = "${var.environment.tenantId}"
        object_id = "${var.privileges.azure_aad_object_id}"

        key_permissions = "${var.privileges.keyvault.permissions.key_permissions}"

        secret_permissions = "${var.privileges.keyvault.permissions.secret_permissions}"

        storage_permissions = [
            "get",
        ]
    }
    tags = "${var.rg.tags}"
}
