/****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP (1000) [company_id]
      ,[company_name]
      ,[timezone]
  FROM [LydiaHelp].[dbo].[companies]