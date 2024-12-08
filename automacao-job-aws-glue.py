
def delete_objects_in_prefix(bucket_name, prefix):
    """
    Exclui todos os objetos dentro de um determinado prefixo em um bucket S3.
    
    Args:
    - bucket_name (str): O nome do bucket S3.
    - prefix (str): O prefixo do diretório onde os objetos estão localizados.
    """
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)

    object_keys = [obj.key for obj in bucket.objects.filter(Prefix=prefix)]
    
    try:
        response = bucket.delete_objects(
            Delete={'Objects': [{'Key': key} for key in object_keys]}
        )
        if 'Deleted' in response:
            print("Deleted objects:")
            for obj in response['Deleted']:
                print(f"- {obj['Key']}")
        if 'Errors' in response:
            print("Errors deleting objects:")
            for error in response['Errors']:
                print(f"- {error['Key']}: {error['Code']}")
    except Exception as e:
        print("Error:", e)

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Exemplo de uso
delete_objects_in_prefix("example-bucket", "example-prefix")
