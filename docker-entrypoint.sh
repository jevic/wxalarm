#!/bin/sh
set -e
Files=/alarm/alarm.py

if [ -z "$SECRET" -o -z "$CORPID" -o -z "$AGENTID" ];then
   echo -e "\033[31m请配置环境变量参数:   \033[m\n\
Example: -e CORPID=xxxx ....\n\
\n\
CORPID 	\t 企业 CorpID \n\
SECRET  \t 应用 Secret \n\
AGENTID \t 应用 AgentId"
else
    sed -i "s/Corpid=.*/Corpid = '$CORPID'/g" $Files
    echo "Corpid = $CORPID"
    sed -i "s/Secret=.*/Secret = '$SECRET'/g" $Files
    echo "Secret = $SECRET"
    sed -i "s/agentid=.*/agentid = $AGENTID/g" $Files
    echo "agentid = $AGENTID"
fi

exec "$@"
