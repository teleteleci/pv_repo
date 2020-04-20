FROM ubuntu:18.04
USER root

ARG bootstrap_playbook=ccep-controller.yml

COPY roles /tmp/roles/
COPY ${bootstrap_playbook} /tmp/

ENV ANSIBLE_LATEST_VERSION=2.9.2

RUN apt-get update && \
apt-get -y install python3-pip && \
apt-get -y install python3-apt && \
apt -y install vim && \
apt -y install curl && \
# Insure ansible is installed with pip3 so that it uses the python3 interpreter
pip3 install ansible==${ANSIBLE_LATEST_VERSION} && \
ansible-playbook /tmp/${bootstrap_playbook} && \
apt-get clean && \
rm -rf /tmp/roles && \
rm /tmp/${bootstrap_playbook}
