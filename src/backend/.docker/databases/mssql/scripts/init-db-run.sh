#!/bin/bash

CONFIGLOG_PATH='./config.log'

# wait for MSSQL server to start
export STATUS=1
i=0

while [[ $STATUS -ne 0 ]] && [[ $i -lt 60 ]]; do
	i=$i+1
	echo "*************************************************************************"
	echo "Waiting for SQL Server to start (it will fail until port is opened)..."
	/opt/mssql-tools/bin/sqlcmd -t 1 -S $DB_HOST -U sa -P $MSSQL_SA_PASSWORD -Q "select 1" >> /dev/null
	STATUS=$?
	sleep 1	
done

if [ $STATUS -ne 0 ]; then 
	echo "Error: MSSQL SERVER took more than 60 seconds to start up."
	exit 1
fi



echo "*********** Preparing SQL Server instance features: Contained databases " | tee -a $CONFIGLOG_PATH
/opt/mssql-tools/bin/sqlcmd -S $DB_HOST -U sa -P $MSSQL_SA_PASSWORD -d master -i ./config/init-db.sql | tee -a $CONFIGLOG_PATH
/opt/mssql-tools/bin/sqlcmd -S $DB_HOST -U $DB_USER -P $DB_PASSWORD -d $REAL_DB -i ./config/setup.instance.sql | tee -a $CONFIGLOG_PATH

echo "======= MSSQL SERVER STARTED ========" | tee -a $CONFIGLOG_PATH