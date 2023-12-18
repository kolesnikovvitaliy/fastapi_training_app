#!/bin/bash

CONFIGLOG_PATH='./config.log'

#wait for MSSQL server to start

export STATUS=1
i=0

while [[ $STATUS -ne 0 ]] && [[ $i -lt 60 ]]; do
	i=$i+1
	echo "*************************************************************************"
	echo "Waiting for SQL Server to start (it will fail until port is opened)..."
	/opt/mssql-tools/bin/sqlcmd -t 1 -S "$DB_HOST" -U "$MSSQL_START_USER" -P "$MSSQL_START_PASSWORD" -Q "select 1" >> /dev/null
	STATUS=$?
	sleep 1	
done

if [ $STATUS -ne 0 ]; then 
	echo "Error: MSSQL SERVER took more than 60 seconds to start up."
	exit 1
fi

echo "======= MSSQL SERVER STARTED ========" | tee -a $CONFIGLOG_PATH


file="/var/opt/mssql/data/${REAL_DB}.mdf"

if [ ! -f "$file" ]
then
	echo "*********** Attaching previously restored databases..." | tee -a $CONFIGLOG_PATH
	/opt/mssql-tools/bin/sqlcmd -S "$DB_HOST" -U "$MSSQL_START_USER" -P "$MSSQL_START_PASSWORD" -d master -i ./config/init-db.sql | tee -a $CONFIGLOG_PATH
	echo "*********** Preparing SQL Server instance features: Contained databases " | tee -a $CONFIGLOG_PATH
	/opt/mssql-tools/bin/sqlcmd -S "$DB_HOST" -U "$MSSQL_START_USER" -P "$MSSQL_START_PASSWORD" -d master -i ./config/setup.instance.sql | tee -a $CONFIGLOG_PATH
# else
# 	echo "*********** Restoring databases: WideWorldImporters, Adventureworks, tpcc ..." | tee -a $CONFIGLOG_PATH
# 	/opt/mssql-tools/bin/sqlcmd -S "$DB_HOST" -U "$MSSQL_START_USER" -P "$MSSQL_START_PASSWORD" -d master -i ./config/restore.sql | tee -a $CONFIGLOG_PAT
	
fi
echo "======= MSSQL CONFIG COMPLETE =======" | tee -a $CONFIGLOG_PATH