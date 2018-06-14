import logging

#Project Imports
from FDADrugAccess import *

logger = logging.getLogger(__name__)

class Service() :

    def initialize(self, configsAsJson):
        try:
            logger.info("Service is getting initialized")
        except Exception as ex:
            logger.exception(ex)
            logger.error("Service failed to initialize")
            raise

    def start(self, contextAsJson):
        try:
            logger.info("Service is getting started")
        except Exception as ex:
            logger.exception(ex)
            logger.error("Service failed to start")
            raise

    def stop(self, contextAsJson):
        try:
            logger.info("Service is getting stopped")
        except Exception as ex:
            logger.exception(ex)
            logger.error("Service failed to stop")
            raise

    def getDrugs(self, limit, offset, **kwargs):
        try:
            drugAccess= FDADrugAccess()
            return drugAccess.getDrugs(limit,offset)
        except Exception as ex:
            logger.exception(ex)
            logger.error("Error while executing getDrugs API")
            raise Exception(ex.message)

    def getDrugByBrand(self, brandName, limit, offset, **kwargs):
        try:
            drugAccess= FDADrugAccess()
            return drugAccess.getDrugByBrand(brandName,limit,offset)
        except Exception as ex:
            logger.exception(ex)
            logger.error("Error while executing getDrugs API")
            raise Exception(ex.message)

    def searchDrugByName(self, name, limit, offset, **kwargs):
        try:
            drugAccess= FDADrugAccess()
            return drugAccess.searchDrugByName(name,limit,offset)
        except Exception as ex:
            logger.exception(ex)
            logger.error("Error while executing getDrugs API")
            raise Exception(ex.message)

    def getUserEventsForDrug(self, drugName, limit, offset, **kwargs):
        try:
            drugAccess= FDADrugAccess()
            return drugAccess.getUserEventsForDrug(drugName,limit,offset)
        except Exception as ex:
            logger.exception(ex)
            logger.error("Error while executing getDrugs API")
            raise Exception(ex.message)

