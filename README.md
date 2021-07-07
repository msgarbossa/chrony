# Ansible Role: chrony

Install and configure chrony time synchronization for Debian-based or RPM-based Linux distributions (Ubuntu/Debian, Redhat).  

## Requirements 

- systemd

## Supports

- Ubuntu
- Debian
- CentOS
- Redhat

## Role Variables

| Variable         | Choices/Defaults | Purpose/Description                                                                                  |
| ---------------- | ---------------- | ---------------------------------------------------------------------------------------------------- |
| chrony_servers</br> *string, list, dict* | **""** | Accepts multiple comma-delimited NTP servers (no spaces), list, or dictionary w/ overrides (see examples) |
| chrony_pools</br> *string, list, dict* | **""** | Accepts multiple comma-delimited NTP pools (no spaces), list, or dictionary w/ overrides (see examples) |
| chrony_default_opts</br> *list* | **[iburst]** | Options to append to each server entry in chrony.conf |
| chrony_config</br> *dict* | **driftfile: /var/lib/chrony/drift<br>makestep: 1.0 3<br>rtcsync: <br>logdir: /var/log/chrony** | Dictionary of key/value configurations |

## Role Dependencies

- none

## Example Playbook Tasks

Minimum facts will automatically be gathered if ansible_system is not defined

Specify one or more NTP servers as a comma-separated string (no spaces)

```yaml
  - name: Install and configure chrony
    include_role:
      name: chrony
    vars:
      chrony_servers: 10.10.1.1
```

Specify one or more NTP servers as a list

```yaml
  - name: Install and configure chrony
    include_role:
      name: chrony
    vars:
      chrony_servers:
        - 10.10.1.1
        - 10.10.1.2
```

Specify one or more NTP servers as a dictionary with optional overrides for chrony_default_opts on the first server

```yaml
  - name: Include role
    include_role:
      name: chrony
    vars:
      chrony_servers:
        10.10.1.1:
          - iburst
          - xleave
        10.10.1.2: []
```

The above results in the following configuration:

```bash
# cat /etc/chrony/chrony.conf 
server 10.10.1.1 iburst xleave
server 10.10.1.2 iburst
driftfile /var/lib/chrony/drift
makestep 1.0 3
rtcsync 
logdir /var/log/chrony
```

## References

Configuration file modeled after Facebook's Chef [fb_chrony cookbook](https://github.com/facebook/chef-cookbooks/tree/master/cookbooks/fb_chrony)

## License

MIT / BSD

## Source

https://github.com/msgarbossa/chrony
