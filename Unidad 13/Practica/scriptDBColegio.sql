USE [master]
GO
/****** Object:  Database [colegio]    Script Date: 3/11/2022 12:18:55 ******/
CREATE DATABASE [colegio]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'colegio', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS\MSSQL\DATA\colegio.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'colegio_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS\MSSQL\DATA\colegio_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT
GO
ALTER DATABASE [colegio] SET COMPATIBILITY_LEVEL = 150
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [colegio].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [colegio] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [colegio] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [colegio] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [colegio] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [colegio] SET ARITHABORT OFF 
GO
ALTER DATABASE [colegio] SET AUTO_CLOSE ON 
GO
ALTER DATABASE [colegio] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [colegio] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [colegio] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [colegio] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [colegio] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [colegio] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [colegio] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [colegio] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [colegio] SET  ENABLE_BROKER 
GO
ALTER DATABASE [colegio] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [colegio] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [colegio] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [colegio] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [colegio] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [colegio] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [colegio] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [colegio] SET RECOVERY SIMPLE 
GO
ALTER DATABASE [colegio] SET  MULTI_USER 
GO
ALTER DATABASE [colegio] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [colegio] SET DB_CHAINING OFF 
GO
ALTER DATABASE [colegio] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [colegio] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [colegio] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [colegio] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO
ALTER DATABASE [colegio] SET QUERY_STORE = OFF
GO
USE [colegio]
GO
/****** Object:  Table [dbo].[alumnos]    Script Date: 3/11/2022 12:18:55 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[alumnos](
	[legajo] [int] NOT NULL,
	[nombre] [varchar](45) NULL,
	[apellido] [varchar](45) NULL,
	[fecha_nacimiento] [date] NULL,
PRIMARY KEY CLUSTERED 
(
	[legajo] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[cursa]    Script Date: 3/11/2022 12:18:55 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[cursa](
	[legajo] [int] NULL,
	[codigo_materia] [int] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[materias]    Script Date: 3/11/2022 12:18:55 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[materias](
	[codigo] [int] NOT NULL,
	[descripcion] [varchar](45) NULL,
PRIMARY KEY CLUSTERED 
(
	[codigo] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
INSERT [dbo].[alumnos] ([legajo], [nombre], [apellido], [fecha_nacimiento]) VALUES (1001, N'Alejandro', N'Gomez', CAST(N'1990-11-20' AS Date))
INSERT [dbo].[alumnos] ([legajo], [nombre], [apellido], [fecha_nacimiento]) VALUES (1002, N'Marco', N'Gimenez', CAST(N'1995-10-20' AS Date))
INSERT [dbo].[alumnos] ([legajo], [nombre], [apellido], [fecha_nacimiento]) VALUES (1003, N'Alan', N'Belcastro', CAST(N'1993-09-24' AS Date))
INSERT [dbo].[alumnos] ([legajo], [nombre], [apellido], [fecha_nacimiento]) VALUES (1004, N'Miguel', N'Martinez', CAST(N'1998-02-10' AS Date))
INSERT [dbo].[alumnos] ([legajo], [nombre], [apellido], [fecha_nacimiento]) VALUES (1005, N'Patricio', N'Alvarez', CAST(N'1999-04-12' AS Date))
GO
INSERT [dbo].[cursa] ([legajo], [codigo_materia]) VALUES (1001, 2333)
INSERT [dbo].[cursa] ([legajo], [codigo_materia]) VALUES (1003, 3242)
INSERT [dbo].[cursa] ([legajo], [codigo_materia]) VALUES (1005, 1233)
INSERT [dbo].[cursa] ([legajo], [codigo_materia]) VALUES (1003, 2333)
INSERT [dbo].[cursa] ([legajo], [codigo_materia]) VALUES (1001, 1233)
GO
INSERT [dbo].[materias] ([codigo], [descripcion]) VALUES (1233, N'Sistemas')
INSERT [dbo].[materias] ([codigo], [descripcion]) VALUES (2230, N'Matematica')
INSERT [dbo].[materias] ([codigo], [descripcion]) VALUES (2333, N'Lengua')
INSERT [dbo].[materias] ([codigo], [descripcion]) VALUES (2355, N'Programacion')
INSERT [dbo].[materias] ([codigo], [descripcion]) VALUES (3242, N'Informatica')
GO
ALTER TABLE [dbo].[cursa]  WITH CHECK ADD FOREIGN KEY([codigo_materia])
REFERENCES [dbo].[materias] ([codigo])
GO
ALTER TABLE [dbo].[cursa]  WITH CHECK ADD FOREIGN KEY([legajo])
REFERENCES [dbo].[alumnos] ([legajo])
GO
USE [master]
GO
ALTER DATABASE [colegio] SET  READ_WRITE 
GO
