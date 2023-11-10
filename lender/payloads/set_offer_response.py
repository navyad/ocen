import json


payload = json.dumps({
  "metadata": {
    "version": "string",
    "originatorOrgId": "string",
    "originatorParticipantId": "string",
    "timestamp": "string",
    "traceId": "string",
    "requestId": "string"
  },
  "response": {
    "status": "SUCCESS",
    "responseDetail": "string"
  },
  "productData": {
    "productId": "BNPL23",
    "productNetworkId": "NTX_BPNL"
  },
  "loanApplicationId": "string",
  "loanApplicationStatus": "CREATED",
  "extensibleData": {}
})
