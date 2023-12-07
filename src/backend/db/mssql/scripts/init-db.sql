USE [master];
GO

IF NOT EXISTS (SELECT * FROM sys.sql_logins WHERE name = '$(NEW_USER)')
BEGIN
    CREATE LOGIN [$(NEW_USER)] WITH PASSWORD = '$(NEW_USER_PASSWORD)', CHECK_POLICY = OFF;
    CREATE USER [$(NEW_USER)] FOR LOGIN [$(NEW_USER)] WITH DEFAULT_SCHEMA=[dbo];
    ALTER SERVER ROLE [sysadmin] ADD MEMBER [$(NEW_USER)];
END
GO

IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = '$(TEST_DB)')
BEGIN
    CREATE DATABASE [$(TEST_DB)]
END
GO

USE [$(TEST_DB)]
GO

IF NOT EXISTS (SELECT 1 FROM sys.tables WHERE name = 'test')
BEGIN
    CREATE TABLE test (
        Id INT NOT NULL IDENTITY,
        Name TEXT NOT NULL,
        Description TEXT NOT NULL,
        PRIMARY KEY (Id)
    );
    INSERT INTO [test] (Name, Description)
    VALUES 
    ('T-Shirt Blue', 'Its blue'),
    ('T-Shirt Black', 'Its black'); 
END

IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = '$(REAL_DB)')
BEGIN
    CREATE DATABASE [$(REAL_DB)]
END
GO

USE [master]
GO

GRANT ALL ON [$(REAL_DB)] TO [$(NEW_USER)];
GO
GRANT ALL ON [$(TEST_DB)] TO [$(NEW_USER)];
GO

USE [$(REAL_DB)]
GO
-- EXECUTE AS USER = '$(NEW_USER)';  
-- GO