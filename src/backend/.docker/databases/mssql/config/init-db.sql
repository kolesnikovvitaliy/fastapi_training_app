IF NOT EXISTS (SELECT * FROM sys.sql_logins WHERE name = '$(DB_USER)')
BEGIN
    CREATE LOGIN [$(DB_USER)] WITH PASSWORD = '$(DB_PASSWORD)', CHECK_POLICY = OFF;
    CREATE USER [$(DB_USER)] FOR LOGIN [$(DB_USER)] WITH DEFAULT_SCHEMA=[dbo];
    ALTER SERVER ROLE [sysadmin] ADD MEMBER [$(DB_USER)];
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

USE [$(REAL_DB)]
GO
