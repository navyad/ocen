"""ocen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from lender import views as lender_views
from loanagent import views as loanagent_views


urlpatterns = [
    path('v4.0.0alpha/loanApplications/createLoanRequest', lender_views.create_loan_application), 
    path('v4.0.0alpha/loanApplications/createLoanResponse', loanagent_views.create_loan_application_response), 

    path('v4.0.0alpha/consent/consentHandleRequest', lender_views.consent_handle_request), 
    path('v4.0.0alpha/consent/consentHandleResponse', loanagent_views.consent_handle_response), 
    
    path('v4.0.0alpha/consent/journeyNotify', lender_views.consent_journey_notify), 
    path('v4.0.0alpha/consent/statusRequest', loanagent_views.consent_status_request), 
    path('v4.0.0alpha/consent/statusResponse', lender_views.consent_status_response), 

    path('v4.0.0alpha/offers/generateoffersRequest', lender_views.generate_offer_request), 
    path('v4.0.0alpha/offers/generateoffersResponse', loanagent_views.generate_offer_response), 

    path('v4.0.0alpha/offers/sendAdditionalDocumentsRequest', lender_views.document_request), 
    path('v4.0.0alpha/offers/sendAdditionalDocumentsResponse', loanagent_views.document_response), 
]
