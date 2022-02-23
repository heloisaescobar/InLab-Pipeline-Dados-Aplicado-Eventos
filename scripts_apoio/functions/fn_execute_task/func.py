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
  wsid = "ocid1.disworkspace.oc1.iad.anuwcljt2ow634yazk7nvc7l6kkki7rcfusqrchlery3hsaxqywikp653npa"
  application="2214e4ca-f171-4b2b-8b42-f835802867c4"
  task="585139af-d0d4-4f08-9710-7b3049e7663e"
  connection="378977c5-ecd6-4d53-bdc4-adc6043955b5"
  bucketName="bucket-raw-data"
  namespace = "idcmuvumgvos"
  md = oci.data_integration.models.RegistryMetadata(aggregator_key=task)
  trkey = str(int(time.time()))
  cp={"bindings":{"PARAMETER_API":{"rootObjectValue":{"modelType":"ENRICHED_ENTITY","entity":{"modelType":"FILE_ENTITY","key":"dataref:"+connection+"/"+bucketName+"/FILE_ENTITY:"+objectName, "externalKey":"https://objectstorage.us-ashburn-1.oraclecloud.com/"+namespace+"/"+bucketName+"/"+objectName, "objectStatus" : 1},"dataFormat":{"formatAttribute":{"modelType":"CSV_FORMAT","encoding":"UTF-8","delimiter": ",","quoteCharacter": "\"","hasHeader": "true","timestampFormat": "yyyy-MM-dd HH:mm:ss.SSS","escapeCharacter": "\\"},"type":"CSV"}}}}}
  task = oci.data_integration.models.CreateTaskRunDetails(key=trkey, registry_metadata=md, config_provider=cp)
  tsk = dip.create_task_run(wsid,application, create_task_run_details=task)
  return tsk.data