# payment/services/momo.py
# import requests
# import uuid
# from django.conf import settings
# def get_access_token():
#     url = f"{settings.MTN_MOMO['base_url']}/disbursement/token/"
#     headers = {
#         "Ocp-Apim-Subscription-Key": settings.MTN_MOMO['subscription_key'],
#         "Authorization": f"Basic {settings.MTN_MOMO['api_key']}",
#     }
#     res = requests.post(url, headers=headers)
#     res.raise_for_status()
#     return res.json()["access_token"]
# def disburse_money_to_farmer(amount, farmer_mobile, external_id, reason):
#     token = get_access_token()
#     transaction_id = str(uuid.uuid4())
#     url = f"{settings.MTN_MOMO['base_url']}/disbursement/v1_0/transfer"
#     headers = {
#         "Authorization": f"Bearer {token}",
#         "X-Target-Environment": settings.MTN_MOMO['target_environment'],
#         "Ocp-Apim-Subscription-Key": settings.MTN_MOMO['subscription_key'],
#         "X-Reference-Id": transaction_id,
#         "Content-Type": "application/json"
#     }
#     payload = {
#         "amount": str(amount),
#         "currency": "EUR",
#         "externalId": str(external_id),
#         "payee": {
#             "partyIdType": "MSISDN",
#             "partyId": farmer_mobile
#         },
#         "payerMessage": reason,
#         "payeeNote": reason
#     }
#     response = requests.post(url, headers=headers, json=payload)
#     if response.status_code == 202:
#         return {"success": True, "transaction_id": transaction_id}
#     return {"success": False, "error": response.text}