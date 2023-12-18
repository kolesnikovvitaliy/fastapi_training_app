RESTORE DATABASE [$(REAL_DB)] FROM  DISK = N'/var/opt/mssql/backup/$(REAL_DB).bak' WITH  
FILE = 1,  MOVE N'$(REAL_DB)' TO N'/var/opt/mssql/data/$(REAL_DB).mdf',  
MOVE N'$(REAL_DB)_log' TO N'/var/opt/mssql/data/$(REAL_DB).ldf',  
REPLACE, NOUNLOAD,  STATS = 5;