# Redis clean all keys

## Possible ways

### Redis-cli client

I try via redis-cli, but redis cli client doesn't support ssl/tsl connection.
*   [posible solution](https://redislabs.com/blog/stunnel-secure-redis-ssl/)
*   [ssh-tunnel](https://help.compose.com/docs/redis-ssh-tunnels)

### Python

Simple and nice and easy of cause for me :-).

#### Links

*   [python documentation](https://redis-py.readthedocs.io/en/latest/)


## Step by step manual

*   clone [git _common repo](https://gitlab.innoble.io/platform/azure-ci/_common)
*   go to platform/knowledge-base/playbooks/mock_phase/redis and execute bash script redis_flush.sh
    *   Type redis cache name
    *   Type subscription

### prerequisites

*   az cli
*   docker
