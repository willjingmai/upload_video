from qcloud_vod.vod_upload_client import VodUploadClient
from qcloud_vod.model import VodUploadRequest
from qcloud_cos import CosServiceError
import datetime
starttime = datetime.datetime.now()
client = VodUploadClient("SecretId", "SecretKey")
request = VodUploadRequest()
request.MediaFilePath = "video_porn.mp4"
request.CoverFilePath = "img_porn.jpg"
try:
    response = client.upload("ap-chongqing", request)
    print("success")
    endtime = datetime.datetime.now()
    print ("Uploading time is ",(endtime - starttime))
except CosServiceError as e:
    print("fail")
    e.get_origin_msg()  # 获取原始错误信息，格式为XML
    e.get_digest_msg()  # 获取处理过的错误信息，格式为dict
    e.get_status_code() # 获取 http 错误码（如4XX，5XX)
    e.get_error_code()  # 获取 COS 定义的错误码
    e.get_error_msg()   # 获取 COS 错误码的具体描述
    e.get_trace_id()    # 获取请求的 trace_id
    e.get_request_id()  # 获取请求的 request_id
    e.get_resource_location() # 获取 URL 地址
    endtime = datetime.datetime.now()
    print ("Uploading time is ",(endtime - starttime))