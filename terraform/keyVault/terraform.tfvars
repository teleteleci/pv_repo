environment = {
    subscription = "ABX_DEV"
    envPrefix = "abdedv"
    tenantId = "1dbf4329-befc-4477-8668-8ec245c081bd"
}

rg = {
    domain = "pvtest"
    location = "West Europe"
    tags = {
        subscription = "xxx"
        note = "Delete anytime"
    }
}

privileges = {
    azure_aad_object_id = "be66ed76-1d61-43d4-873e-322a29ada4db"
    keyvault = {
        comments = "DEV_ADMINS"
        principalId = "be66ed76-1d61-43d4-873e-322a29ada4db"
        permissions = {
            key_permissions: [
                "get",
                "list",
                "update",
                "create",
                "import",
                "delete",
                "recover",
                "backup",
                "restore",
                "verify"
            ]
            secret_permissions: [
                "get",
                "list",
                "set",
                "delete",
                "recover",
                "backup",
                "restore"
            ]
        }
    }
}
