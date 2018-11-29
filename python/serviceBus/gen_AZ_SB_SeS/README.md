# Prod

## Service bus

### Topic

> #### Environment
>
> ##### Topic definition
>
> | Environment name                        | description                                                                                                          | example value | Mandatory | Default value |
> | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ------------- | --------- | ------------- |
> | topic_name                              | Servicebus topic name                                                                                                | pay-events    | Y         |               |
> | message_time_to_live                    | Time to live duration at ISO 8601                                                                                    | P30D          | N         | P14D          |
> | duplicate_detection_history_time_window | SO 8601 time format for structure that defines the duration of the duplicate detection history.                      | 0:0:10        | N         | 0:10:00       |
> | enable_batched_operations               | Allow server-side batched operations.                                                                                | true          | N         | true          |
> | enable_duplicate_detection              | A boolean value indicating if this topic requires duplicate detection.                                               | true          | N         | true          |
> | enable_express                          | A boolean value indicating if this topic requires duplicate detection.                                               | true          | N         | true          |
> | enable_partitioning                     | A boolean value that indicates whether the topic/queue to be partitioned across multiple message brokers is enabled. | false         | N         | false         |
> | max_size                                | Maximum size of topic in megabytes, which is the size of the memory allocated for the topic.                         | 1024          | N         | 1024          |
> | Access_policies                               | List of access policy rights.   | \["send"\]         | N         | \[\]          |
>
>
>
>
>-   SB_SUBSCRIPTION_SMS_CATCHER="sms-catcher"

```yaml
{
    "a": "b"
}
```

### Create topic



# SB serviceBus

## Solution overview and deployed resources

This template deploys an servicebus.

## Azure Resources Provisioning

```bash
# log in to Azure
az login

# check the active subscription
az account show
# when needed switch to specific subscription
az account set --subscription HCI_ABX

# create a resource group
az group create \
--name abx-pv-sb-dev-rg \
--location westeurope \
--verbose

# create ACR itself
az group deployment create \
--resource-group abx-pv-sb-dev-rg \
--name abx-pv-sb-dev-deployment \
--template-file abx-pv-sb-dev-templates-gen.json \
--parameters @abx-pv-sb-dev-parameters.json \
--verbose
```
