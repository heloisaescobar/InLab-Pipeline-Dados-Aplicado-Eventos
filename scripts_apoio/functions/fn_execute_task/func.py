import io
import json
import time
from fdk import response
import oci
from oci.data_integration.data_integration_client import DataIntegrationClient
def handler(ctx, data: io.BytesIO=None):
  signer = oci.auth.signers.get_resource_principals_signer()
  body = json.loads(data.getvalue())
  resource_name = body["data"]["resourceName"]
  resp = do(signer,resource_name)
  return response.Response(
    ctx, response_data=resp,
    headers={"Content-Type": "application/json"}
  )
def do(signer, objectName):
  dip = DataIntegrationClient(config={}, signer=signer)
  wsid = "<Adicionar_disworkspace>"
  application="<Sua_Application>"
  task="<Sua_Taks>"
  connection="<ETAG-Bucket>"
  bucketName="<Nome_Bucket>"
  namespace = "<NameSpace>"
  md = oci.data_integration.models.RegistryMetadata(aggregator_key=task)
  trkey = str(int(time.time()))
  cp={"bindings":{"PARAMETER_API":{"rootObjectValue":{"modelType":"ENRICHED_ENTITY","entity":{"modelType":"FILE_ENTITY","key":"dataref:"+connection+"/"+bucketName+"/FILE_ENTITY:"+objectName, "externalKey":"https://objectstorage.us-ashburn-1.oraclecloud.com/"+namespace+"/"+bucketName+"/"+objectName, "objectStatus" : 1},"dataFormat":{"formatAttribute":{"modelType":"CSV_FORMAT","encoding":"UTF-8","delimiter": ",","quoteCharacter": "\"","hasHeader": "true","timestampFormat": "yyyy-MM-dd HH:mm:ss.SSS","escapeCharacter": "\\"},"type":"CSV"}}}}}
  task = oci.data_integration.models.CreateTaskRunDetails(key=trkey, registry_metadata=md, config_provider=cp)
  tsk = dip.create_task_run(wsid,application, create_task_run_details=task)
  return tsk.data
