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
    "productId": "string",
    "productNetworkId": "string"
  },
  "loanApplicationId": "string",
  "loanApplicationStatus": "CREATED",
  "extensibleData": {}
})
