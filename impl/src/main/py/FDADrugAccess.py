import requests
import logging
import json
import time
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager
import ssl
import sys

logger = logging.getLogger(__name__)


class SSLAdapter(HTTPAdapter):
    '''An HTTPS Transport Adapter that uses an arbitrary SSL version.'''
    def __init__(self, ssl_version=None, **kwargs):
        self.ssl_version = ssl_version
        super(SSLAdapter, self).__init__(**kwargs)
    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = PoolManager(num_pools=connections,
                                       maxsize=maxsize,
                                       block=block,
                                       ssl_version=self.ssl_version)


class FDADrugAccess(object):
    def __init__(self):
        self.labelurl   = "https://api.fda.gov/drug/label.json"
        self.eventsurl  = "https://api.fda.gov/drug/event.json"
        self.session    = requests.Session()
        self.session.mount('https://', 
                            SSLAdapter(ssl_version=ssl.PROTOCOL_TLSv1_2))
        logging.info("Initialized requests Session")

    def getDrugs(self,limit=10,offset=0):
        logger.info("Executing getDrugs with limit: %d, offset: %d" % (limit,offset))
        payload = {'limit': limit,'skip': offset}
        response = requests.get(self.labelurl, params=payload)
        if response.status_code != 200:
            logger.error("API Invocation failed with %s" % (self.labelurl))
            logger.error("API Status Code: %r" % (response.status_code))
            raise Exception("API Failed with %s" % (response.text))
        return response.json()

    def getDrugByBrand(self,brand,limit=10,offset=0):
        logger.info("Executing getDrugByBrand with name: %s limit: %d, offset: %d" % 
                                                        (brand,limit,offset))
        payload = {'search': brand, 'limit': limit,'skip': offset}
        response = requests.get(self.labelurl, params=payload)
        if response.status_code != 200:
            logger.error("API Invocation failed with %s" % (self.labelurl))
            logger.error("API Status Code: %r" % (response.status_code))
            raise Exception("API Failed with %s" % (response.text))
        return response.json()

    def searchDrugByName(self,brand,limit=10,offset=0):
        logger.info("Executing searchDrugByName with name: %s limit: %d, offset: %d" % 
                                                        (brand,limit,offset))
        payload = {'search': brand, 'limit': limit,'skip': offset}
        response = requests.get(self.labelurl, params=payload)
        if response.status_code != 200:
            logger.error("API Invocation failed with %s" % (self.labelurl))
            logger.error("API Status Code: %r" % (response.status_code))
            raise Exception("API Failed with %s" % (response.text))
        return response.json()
    
    def getUserEventsForDrug(self,brand,limit=10,offset=0):
        logger.info("Executing getUserEventsForDrug with name: %s limit: %d, offset: %d" % 
                                                        (brand,limit,offset))
        payload = {'search': brand, 'limit': limit,'skip': offset}
        response = requests.get(self.eventsurl, params=payload)
        if response.status_code != 200:
            logger.error("API Invocation failed with %s" % (self.labelurl))
            logger.error("API Status Code: %r" % (response.status_code))
            raise Exception("API Failed with %s" % (response.text))
        return response.json()
        