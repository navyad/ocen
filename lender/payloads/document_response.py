
payload = {
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
  "loanApplications": [
    {
      "createdDate": "2023-10-29",
      "loanApplicationId": "string",
      "loanApplicationStatus": "CREATED",
      "kyc": {
        "kycRefNo": "string",
        "description": "string",
        "business": {
          "type": "CKYC",
          "scale": "MICRO",
          "category": "SERVICE",
          "name": "string",
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
          "email": "string",
          "phoneNumber": "string",
          "incorporationDate": "2023-10-29",
          "commencementDate": "2023-10-29",
          "udyam": {
            "registrationNumber": "string",
            "registrationDate": "2023-10-29",
            "extensibleData": {}
          },
          "status": "SUCCESS",
          "extensibleData": {}
        },
        "individual": {
          "type": "CKYC",
          "name": "string",
          "dob": "string",
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
          "status": "SUCCESS",
          "email": "string",
          "phoneNumber": "string",
          "extensibleData": {}
        },
        "next": {
          "type": "REDIRECT",
          "data": {
            "url": "string"
          }
        },
        "extensibleData": {}
      },
      "offers": [
        {
          "id": "string",
          "validTill": "2023-10-29",
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
          "disbursement": {
            "plans": [
              {
                "id": "string",
                "title": "string",
                "shortDescription": "string",
                "description": "string",
                "paymentUrl": "string",
                "payNowAllowed": True,
                "editPlanAllowed": True,
                "changeMethodAllowed": True,
                "automatic": True,
                "scheduleType": "RECURRING",
                "noOfInstallment": 0,
                "frequency": "MONTHLY",
                "tenure": {
                  "duration": 0,
                  "unit": "MONTH"
                },
                "totalAmount": 0,
                "principal": 0,
                "interestAmount": 0,
                "penalty": 0,
                "startDate": "2023-10-29",
                "status": "ACTIVE",
                "url": "string",
                "extensibleData": {}
              }
            ],
            "accountDetails": [
              {
                "id": "string",
                "description": "string",
                "status": "ACTIVE",
                "accountDataType": "ACCOUNT",
                "data": {
                  "accountType": "CURRENT",
                  "accountIFSC": "string",
                  "accountNumber": "string",
                  "vpa": "string",
                  "maskedAccountNumber": "string",
                  "accountHolderName": "string",
                  "url": "string"
                },
                "extensibleData": {}
              }
            ]
          },
          "repayment": {
            "plans": [
              {
                "id": "string",
                "title": "string",
                "shortDescription": "string",
                "description": "string",
                "paymentUrl": "string",
                "payNowAllowed": True,
                "editPlanAllowed": True,
                "changeMethodAllowed": True,
                "automatic": True,
                "scheduleType": "RECURRING",
                "noOfInstallment": 0,
                "frequency": "MONTHLY",
                "tenure": {
                  "duration": 0,
                  "unit": "MONTH"
                },
                "totalAmount": 0,
                "principal": 0,
                "interestAmount": 0,
                "penalty": 0,
                "startDate": "2023-10-29",
                "status": "ACTIVE",
                "url": "string",
                "extensibleData": {}
              }
            ]
          },
          "description": "string",
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
      "description": "string",
      "url": "string",
      "extensibleData": {},
      "rejectionDetails": [
        {
          "reason": "LOW_CREDIT_SCORE",
          "description": "string",
          "url": "string",
          "extensibleData": {}
        }
      ],
      "actionRequired": [
        {
          "actionType": "ADD_DOCUMENT",
          "description": "string",
          "reference": {
            "object": "string",
            "value": "string"
          },
          "url": "string",
          "extensibleData": {}
        }
      ]
    }
  ]
}
