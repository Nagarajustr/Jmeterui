#!/bin/bash

 
GH_OWNER="Nagarajucts"
GH_REPOSITORY="Jmeterui"
GH_TOKEN="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"
GH_LABEL="docker_runner"
 
RUNNER_SUFFIX=$(cat /dev/urandom | tr -dc 'a-z0-9' | fold -w 5 | head -n 1)
RUNNER_NAME="dockerNodeDevOps-${RUNNER_SUFFIX}" --lables $GH_LABEL
 
REG_TOKEN=$(curl -sX POST -H "Accept: application/vnd.github.v3+json" -H "Authorization: token ${GH_TOKEN}" https://api.github.com/repos/${GH_OWNER}/${GH_REPOSITORY}/actions/runners/registration-token | jq .token --raw-output)
#REG_TOKEN=$REG_TOKEN
 
cd /home/docker/actions-runner
 
./config.sh --unattended --url https://github.com/${GH_OWNER}/${GH_REPOSITORY} --token ${REG_TOKEN} --name ${RUNNER_NAME} --lables $GH_LABEL
 
cleanup() {
    echo "Removing runner..."
    ./config.sh remove --unattended --token ${REG_TOKEN}
}
 
trap 'cleanup; exit 130' INT
trap 'cleanup; exit 143' TERM

./run.sh & wait $!
