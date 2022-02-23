import io
import requests
import os
import json
import logging
import sys
import time
import pandas as pd
from datetime import datetime, timedelta
import configparser

from fdk import response
import oci.object_storage


def get_api():
    endpoint = 'https://strangerthings-quotes.vercel.app/api/quotes/500'
    headers = {'content-type': "text/json; charset=utf-8"}
    # try connect endpoint
    response = requests.get(endpoint, headers=headers)
    if response.status_code != 200:
          raise Exception(response.status_code, response.text)
    jsonparsed = json.loads(response.text)
    response = pd.DataFrame(jsonparsed)

    return response.to_csv(encoding='utf-8')

def handler(ctx, data: io.BytesIO=None):
    vtime = time.strftime("%Y%m%d-%H%M%S")
    bucketName = 'bucket-raw-data'
    objectName = "stranger_api" + vtime + ".csv"
    content = get_api()
    resp = put_object(bucketName, objectName, content.encode(encoding = 'UTF-8', errors = 'strict'))
    return response.Response(
        ctx,
        response_data=json.dumps(resp),
        headers={"Content-Type": "application/json"}
    )

def put_object(bucketName, objectName, content):
    signer = oci.auth.signers.get_resource_principals_signer()
    client = oci.object_storage.ObjectStorageClient(config={}, signer=signer)
    namespace = client.get_namespace().data
    output=""
    try:
        object = client.put_object(namespace, bucketName, objectName, content)
        output = "Success: Put object '" + objectName + "' in bucket '" + bucketName + "'"
    except Exception as e:
        output = "Failed: " + str(e)
    return { "state": output }