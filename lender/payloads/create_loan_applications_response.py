payload = {
  "metadata": {
    "version": "test",
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
  "loanApplications": [
    {
      "createdDate": "2023-10-29",
      "loanApplicationId": "string",
      "loanApplicationStatus": "CREATED",
      "pledgedDocuments": [
        {
          "source": "GSTN",
          "sourceIdentifier": "string",
          "format": "JSON",
          "reference": "string",
          "type": "GST_PROFILE",
          "isDataInline": True,
          "data": "string"
        }
      ],
      "borrower": {
        "primaryId": "string",
        "primaryIdType": "PAN",
        "additionalIdentifiers": [
          {
            "key": "string",
            "value": "string",
            "url": "string",
            "extensibleData": {}
          }
        ],
        "name": "string",
        "category": "ORGANIZATION",
        "contactDetails": [
          {
            "type": "PRIMARY",
            "desctiption": "string",
            "phone": "string",
            "email": "string",
            "address": {
              "hba": "string",
              "srl": "string",
              "landmark": "string",
              "als": "string",
              "vtc": "string",
              "pinCode": "string",
              "po": "string",
              "district": "string",
              "state": "string",
              "country": "string",
              "url": "string",
              "latitude": "string",
              "longitude": "string",
              "extensibleData": {}
            },
            "url": "string",
            "extensibleData": {}
          }
        ],
        "documents": [
          {
            "source": "GSTN",
            "sourceIdentifier": "string",
            "format": "JSON",
            "reference": "string",
            "type": "GST_PROFILE",
            "isDataInline": True,
            "data": "string"
          }
        ],
        "url": "string",
        "extensibleData": {},
        "aaIdentifier": "user@aa"
      },
      "guarantors": [
        {
          "primaryId": "string",
          "primaryIdType": "PAN",
          "description": "string",
          "additionalIdentifiers": [
            {
              "key": "string",
              "value": "string",
              "url": "string",
              "extensibleData": {}
            }
          ],
          "name": "string",
          "relationshipWithBorrower": "string",
          "category": "ORGANIZATION",
          "contactDetails": [
            {
              "type": "PRIMARY",
              "desctiption": "string",
              "phone": "string",
              "email": "string",
              "address": {
                "hba": "string",
                "srl": "string",
                "landmark": "string",
                "als": "string",
                "vtc": "string",
                "pinCode": "string",
                "po": "string",
                "district": "string",
                "state": "string",
                "country": "string",
                "url": "string",
                "latitude": "string",
                "longitude": "string",
                "extensibleData": {}
              },
              "url": "string",
              "extensibleData": {}
            }
          ],
          "documents": [
            {
              "source": "GSTN",
              "sourceIdentifier": "string",
              "format": "JSON",
              "reference": "string",
              "type": "GST_PROFILE",
              "isDataInline": True,
              "data": "string"
            }
          ],
          "url": "string",
          "extensibleData": {}
        }
      ],
      "applicants": [
        {
          "primaryId": "string",
          "primaryIdType": "PAN",
          "additionalIdentifiers": [
            {
              "key": "string",
              "value": "string",
              "url": "string",
              "extensibleData": {}
            }
          ],
          "name": "string",
          "category": "ORGANIZATION",
          "relationshipWithBorrower": "string",
          "contactDetails": [
            {
              "type": "PRIMARY",
              "desctiption": "string",
              "phone": "string",
              "email": "string",
              "address": {
                "hba": "string",
                "srl": "string",
                "landmark": "string",
                "als": "string",
                "vtc": "string",
                "pinCode": "string",
                "po": "string",
                "district": "string",
                "state": "string",
                "country": "string",
                "url": "string",
                "latitude": "string",
                "longitude": "string",
                "extensibleData": {}
              },
              "url": "string",
              "extensibleData": {}
            }
          ],
          "documents": [
            {
              "source": "GSTN",
              "sourceIdentifier": "string",
              "format": "JSON",
              "reference": "string",
              "type": "GST_PROFILE",
              "isDataInline": True,
              "data": "string"
            }
          ],
          "url": "string",
          "extensibleData": {}
        }
      ],
      "terms": {
        "requestedAmount": 0,
        "currency": "string",
        "sanctionedAmount": 0,
        "netDisbursedAmount": 0,
        "interestType": "FIXED",
        "interestRate": 0,
        "annualPercentageRate": 0,
        "coolingOffPeriod": {
          "duration": 0,
          "unit": "MONTH"
        },
        "totalRepayableAmount": 0,
        "interestAmount": 0,
        "description": "string",
        "tenure": {
          "duration": 0,
          "unit": "MONTH"
        },
        "legalAgreement": {
          "type": "TEXT",
          "data": "string"
        },
        "documents": [
          {
            "source": "GSTN",
            "sourceIdentifier": "string",
            "format": "JSON",
            "reference": "string",
            "type": "GST_PROFILE",
            "isDataInline": True,
            "data": "string"
          }
        ],
        "charges": {
          "prepayment": {
            "chargeType": "FIXED_AMOUNT",
            "data": {
              "rate": 0,
              "amount": 0,
              "applicableParameter": "TOTAL_LOAN_AMOUNT",
              "description": "string",
              "url": "string"
            },
            "url": "string",
            "extensibleData": {}
          },
          "bounce": {
            "chargeType": "FIXED_AMOUNT",
            "data": {
              "rate": 0,
              "amount": 0,
              "applicableParameter": "TOTAL_LOAN_AMOUNT",
              "description": "string",
              "url": "string"
            },
            "url": "string",
            "extensibleData": {}
          },
          "latePayment": {
            "chargeType": "FIXED_AMOUNT",
            "data": {
              "rate": 0,
              "amount": 0,
              "applicableParameter": "TOTAL_LOAN_AMOUNT",
              "description": "string",
              "url": "string"
            },
            "url": "string",
            "extensibleData": {}
          },
          "processing": {
            "chargeType": "FIXED_AMOUNT",
            "data": {
              "rate": 0,
              "amount": 0,
              "applicableParameter": "TOTAL_LOAN_AMOUNT",
              "description": "string",
              "url": "string"
            },
            "url": "string",
            "extensibleData": {}
          },
          "other": {
            "chargeType": "FIXED_AMOUNT",
            "data": {
              "rate": 0,
              "amount": 0,
              "applicableParameter": "TOTAL_LOAN_AMOUNT",
              "description": "string",
              "url": "string"
            },
            "url": "string",
            "extensibleData": {}
          }
        },
        "url": "string",
        "extensibleData": {}
      },
      "url": "string",
      "description": "string",
      "creditGuarantees": {
        "cgtmseEligible": True
      }
    }
  ]
}


