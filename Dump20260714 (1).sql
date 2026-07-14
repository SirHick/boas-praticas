CREATE DATABASE  IF NOT EXISTS `metalsul_industrial` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `metalsul_industrial`;
-- MySQL dump 10.13  Distrib 8.0.44, for Win64 (x86_64)
--
-- Host: localhost    Database: metalsul_industrial
-- ------------------------------------------------------
-- Server version	8.0.44

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `categoria_produto`
--

DROP TABLE IF EXISTS `categoria_produto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categoria_produto` (
  `id_categoria` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  `descricao` text,
  PRIMARY KEY (`id_categoria`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categoria_produto`
--

LOCK TABLES `categoria_produto` WRITE;
/*!40000 ALTER TABLE `categoria_produto` DISABLE KEYS */;
INSERT INTO `categoria_produto` VALUES (1,'Estruturas Metálicas','Peças estruturais industriais'),(2,'Parafusos','Fixadores metálicos industriais'),(3,'Componentes Hidráulicos','Componentes para sistemas hidráulicos'),(4,'Peças Automotivas','Componentes destinados ao setor automotivo');
/*!40000 ALTER TABLE `categoria_produto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `controle_qualidade`
--

DROP TABLE IF EXISTS `controle_qualidade`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `controle_qualidade` (
  `id_qualidade` int NOT NULL AUTO_INCREMENT,
  `data_inspecao` date NOT NULL,
  `resultado_inspecao` varchar(50) NOT NULL,
  `observacoes_tecnicas` text,
  `id_ordem` int NOT NULL,
  PRIMARY KEY (`id_qualidade`),
  KEY `fk_qualidade_ordem` (`id_ordem`),
  CONSTRAINT `fk_qualidade_ordem` FOREIGN KEY (`id_ordem`) REFERENCES `ordem_producao` (`id_ordem`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `controle_qualidade`
--

LOCK TABLES `controle_qualidade` WRITE;
/*!40000 ALTER TABLE `controle_qualidade` DISABLE KEYS */;
INSERT INTO `controle_qualidade` VALUES (1,'2026-05-01','Aprovado','Produto dentro das especificações',1),(2,'2026-05-01','Aprovado','Lote aprovado sem inconformidades',2),(3,'2026-05-02','Reprovado','Vazamento identificado no teste hidráulico',3),(4,'2026-05-02','Aprovado','Correção realizada e item aprovado',3),(5,'2026-05-03','Em análise','Aguardando medições finais',4),(6,'2026-05-04','Aprovado','Qualidade aprovada conforme padrão ISO',5),(7,'2026-05-04','Aprovado','Parafusos dentro da tolerância',6),(8,'2026-05-05','Reprovado','Estrutura apresentou desalinhamento',8);
/*!40000 ALTER TABLE `controle_qualidade` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fornecedor`
--

DROP TABLE IF EXISTS `fornecedor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fornecedor` (
  `id_fornecedor` int NOT NULL AUTO_INCREMENT,
  `razao_social` varchar(150) NOT NULL,
  `cnpj` char(14) NOT NULL,
  `telefone` varchar(20) DEFAULT NULL,
  `cidade` varchar(100) NOT NULL,
  PRIMARY KEY (`id_fornecedor`),
  UNIQUE KEY `cnpj` (`cnpj`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fornecedor`
--

LOCK TABLES `fornecedor` WRITE;
/*!40000 ALTER TABLE `fornecedor` DISABLE KEYS */;
INSERT INTO `fornecedor` VALUES (1,'Aço Forte LTDA','11111111000111','(47)99999-1111','Joinville'),(2,'Metal Prime Industrial','22222222000122','(47)99999-2222','Blumenau'),(3,'Hydra Components','33333333000133','(47)99999-3333','Jaraguá do Sul'),(4,'AutoParts Brasil','44444444000144','(47)99999-4444','Curitiba'),(5,'Fixadores União','55555555000155','(47)99999-5555','São Paulo');
/*!40000 ALTER TABLE `fornecedor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `funcionario`
--

DROP TABLE IF EXISTS `funcionario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `funcionario` (
  `id_funcionario` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(150) NOT NULL,
  `cpf` char(11) NOT NULL,
  `cargo` varchar(100) NOT NULL,
  `salario` decimal(10,2) NOT NULL,
  `data_admissao` date NOT NULL,
  `id_setor` int NOT NULL,
  PRIMARY KEY (`id_funcionario`),
  UNIQUE KEY `cpf` (`cpf`),
  KEY `fk_funcionario_setor` (`id_setor`),
  CONSTRAINT `fk_funcionario_setor` FOREIGN KEY (`id_setor`) REFERENCES `setor` (`id_setor`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `funcionario`
--

LOCK TABLES `funcionario` WRITE;
/*!40000 ALTER TABLE `funcionario` DISABLE KEYS */;
INSERT INTO `funcionario` VALUES (1,'Carlos Henrique','11111111111','Operador CNC',4500.00,'2021-03-10',1),(2,'Marcos Paulo','22222222222','Soldador Industrial',4200.00,'2020-07-15',2),(3,'Fernanda Lima','33333333333','Inspetora de Qualidade',5000.00,'2019-11-20',5),(4,'Juliana Alves','44444444444','Pintora Industrial',3900.00,'2022-01-05',3),(5,'Ricardo Souza','55555555555','Montador Mecânico',4100.00,'2021-09-12',4),(6,'Patricia Gomes','66666666666','Supervisora de Produção',7500.00,'2018-05-18',1),(7,'Lucas Martins','77777777777','Auxiliar de Produção',2800.00,'2023-02-01',4),(8,'Amanda Costa','88888888888','Analista de Qualidade',5200.00,'2020-12-09',5),(9,'e','123','t',12.00,'1997-12-12',2);
/*!40000 ALTER TABLE `funcionario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ordem_producao`
--

DROP TABLE IF EXISTS `ordem_producao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ordem_producao` (
  `id_ordem` int NOT NULL AUTO_INCREMENT,
  `data_producao` date NOT NULL,
  `quantidade_produzida` int NOT NULL,
  `status_producao` varchar(50) NOT NULL,
  `tempo_estimado` int NOT NULL,
  `tempo_real` int DEFAULT NULL,
  `id_produto` int NOT NULL,
  `id_funcionario` int NOT NULL,
  PRIMARY KEY (`id_ordem`),
  KEY `fk_ordem_produto` (`id_produto`),
  KEY `fk_ordem_funcionario` (`id_funcionario`),
  CONSTRAINT `fk_ordem_funcionario` FOREIGN KEY (`id_funcionario`) REFERENCES `funcionario` (`id_funcionario`),
  CONSTRAINT `fk_ordem_produto` FOREIGN KEY (`id_produto`) REFERENCES `produto` (`id_produto`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ordem_producao`
--

LOCK TABLES `ordem_producao` WRITE;
/*!40000 ALTER TABLE `ordem_producao` DISABLE KEYS */;
INSERT INTO `ordem_producao` VALUES (1,'2026-05-01',10,'Concluída',480,500,1,1),(2,'2026-05-01',2000,'Concluída',240,230,2,6),(3,'2026-05-02',15,'Concluída',360,390,3,1),(4,'2026-05-03',50,'Em andamento',300,NULL,4,5),(5,'2026-05-03',12,'Concluída',420,415,5,1),(6,'2026-05-04',1500,'Concluída',180,175,6,6),(7,'2026-05-04',25,'Pausada',240,NULL,7,5),(8,'2026-05-05',8,'Concluída',600,640,8,1);
/*!40000 ALTER TABLE `ordem_producao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produto`
--

DROP TABLE IF EXISTS `produto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `produto` (
  `id_produto` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(150) NOT NULL,
  `descricao` text,
  `preco_fabricacao` decimal(10,2) NOT NULL,
  `quantidade_estoque` int NOT NULL DEFAULT '0',
  `id_categoria` int NOT NULL,
  `id_fornecedor` int NOT NULL,
  PRIMARY KEY (`id_produto`),
  KEY `fk_produto_categoria` (`id_categoria`),
  KEY `fk_produto_fornecedor` (`id_fornecedor`),
  CONSTRAINT `fk_produto_categoria` FOREIGN KEY (`id_categoria`) REFERENCES `categoria_produto` (`id_categoria`),
  CONSTRAINT `fk_produto_fornecedor` FOREIGN KEY (`id_fornecedor`) REFERENCES `fornecedor` (`id_fornecedor`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produto`
--

LOCK TABLES `produto` WRITE;
/*!40000 ALTER TABLE `produto` DISABLE KEYS */;
INSERT INTO `produto` VALUES (1,'Chassi Industrial','Estrutura metálica para máquinas industriais',2500.00,15,1,1),(2,'Parafuso Sextavado M10','Parafuso industrial galvanizado',2.50,5000,2,5),(3,'Cilindro Hidráulico HX20','Cilindro hidráulico de alta pressão',850.00,40,3,3),(4,'Suporte Automotivo X','Peça automotiva reforçada',120.00,150,4,4),(5,'Base Metálica Industrial','Base estrutural para equipamentos',980.00,30,1,2),(6,'Parafuso Allen M8','Parafuso allen para montagem industrial',1.80,3500,2,5),(7,'Válvula Hidráulica V300','Válvula para sistemas hidráulicos',430.00,60,3,3),(8,'Estrutura Tubular ZX','Estrutura metálica tubular',1750.00,20,1,1);
/*!40000 ALTER TABLE `produto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `setor`
--

DROP TABLE IF EXISTS `setor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `setor` (
  `id_setor` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  `localizacao` varchar(150) NOT NULL,
  PRIMARY KEY (`id_setor`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `setor`
--

LOCK TABLES `setor` WRITE;
/*!40000 ALTER TABLE `setor` DISABLE KEYS */;
INSERT INTO `setor` VALUES (1,'Usinagem','Bloco A'),(2,'Soldagem','Bloco B'),(3,'Pintura','Bloco C'),(4,'Montagem','Bloco D'),(5,'Qualidade','Bloco E');
/*!40000 ALTER TABLE `setor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'metalsul_industrial'
--

--
-- Dumping routines for database 'metalsul_industrial'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-07-14 15:42:02
