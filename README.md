# 🧹 AWS Glue Job: Limpeza de Database Antes de População

Este repositório contém o script desenvolvido para otimizar o processo de alimentação de um database gerenciado pela AWS Glue. O objetivo principal é fazer com que o job do AWS Glue realize uma limpeza no bucket S3 associado ao database antes de inserir os arquivos atualizados para evitar duplicações na atualização diaria do database e automatizar um processo anteriormente manual.

## 🛠️ **Motivação do Projeto**
Originalmente, os jobs do Glue apenas adicionavam os arquivos ao database, resultando em duplicações e ineficiência no processamento dos dados visto que para evitar as duplicatas era necessaria uma limpeza manual no bucket. Este script resolve esse problema ao:
1. Identificar os arquivos no diretorio definido no bucket S3.
2. Excluir os arquivos antigos do bucket.
3. Permitir que o processo de alimentação ocorra de forma limpa, organizada e automatica.

## 🚀 **Como Funciona**
O script utiliza a integração entre **AWS Glue**, **S3** e **Python**, realizando as seguintes etapas:
1. Configura o ambiente do AWS Glue (Spark e GlueContext).
2. Exclui todos os arquivos dentro de um diretorio específico no bucket S3 antes de iniciar o processo de população.
3. Executa a carga de dados atualizados, garantindo que o database mantenha informações consistentes e sem duplicação.

## 📋 **Pré-requisitos**
- **AWS Glue** configurado na sua conta AWS.
- Permissões adequadas para o bucket S3.
- Linguagem **Python** e dependências do AWS Glue (`boto3`, `awsglue`).

## 🔧 **Estrutura do Código**
- **`delete_objects_in_prefix`**:
  Uma função que limpa o prefixo especificado no bucket S3.
- **Configuração do Glue Job**:
  Configurações necessárias para rodar o job com suporte a Spark e GlueContext.
- **Execução do Job**:
  O job é inicializado e os dados atualizados são povoados no database após a limpeza.

## 💡 **Como Usar**
1. Substitua `bucket_name` e `prefix` no script pelos valores correspondentes ao seu ambiente.
2. Atualize o script do job no AWS Glue.
3. Execute o job no AWS Glue.

## 📜 **Licença**
Este projeto está licenciado sob os termos da [Licença MIT](LICENSE.txt).
