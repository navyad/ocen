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
  "productData": {
    "productId": "string",
    "productNetworkId": "string"
  },
  "loanApplicationIds": [
    "string"
  ],
  "consent": {
    "consentFetchType": "ONETIME",
    "vua": "string",
    "description": "string",
    "isAggregationEnabled": True,
    "consentAggregationId": "string",
    "consentHandle": "string",
    "consentStatus": "READY",
    "url": "string",
    "extensibleData": {}
  },
  "response": {
    "status": "SUCCESS",
    "responseDetail": "string"
  }
})




