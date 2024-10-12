# def Wxpusher_server():
#         import os
#         import requests

#         def sc_send(sendkey, title, desp='', options=None):
#             if options is None:
#                 options = {}
#             if sendkey.startswith('sctp'):
#                 url = f'https://{sendkey}.push.ft07.com/send'
#             else:
#                 url = f'https://sctapi.ftqq.com/{sendkey}.send'
#             params = {
#                 'title': title,
#                 'desp': desp,
#                 **options
#             }
#             headers = {
#                 'Content-Type': 'application/json;charset=utf-8'
#             }
#             response = requests.post(url, json=params, headers=headers)
#             result = response.json()
#             return result
#         print("before getkey")
#         #key = os.environ.get('SENDKEY')
#         print("after getkey")
#         table_content="123"
#         msg=f"<table style='border-collapse: collapse;'><tr style='background-color: #f2f2f2;'><th style='border: 1px solid #ccc; padding: 8px;'>🆔</th><th style='border: 1px solid #ccc; padding: 8px;'>用户名</th><th style='border: 1px solid #ccc; padding: 8px;'>总积分</th><th style='border: 1px solid #ccc; padding: 8px;'>今日积分</th></tr>{table_content}</table>"
#         ret = sc_send(key, 'pgsh', msg)
#         print(ret)
#         pass
# Wxpusher_server()