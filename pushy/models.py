import logging
from django.db import models
from django.db.models.signals import post_save
import redis
import json

from pushy import settings as pushy_settings

logger = logging.getLogger(__name__)

def pushy_post_save(sender, **kwargs):
    rs = redis.StrictRedis()
    obj = kwargs['instance']
    
    message = {
               'route': obj.get_api_url(),
               'type': 'update'
               }
    logger.debug('Routing message to: %s' % pushy_settings.get_channel())
    rs.publish('%s%s' % (pushy_settings.get_channel(), 'update'), json.dumps(message))
    

def setup_signals():

    for model in pushy_settings.get_models().values():
        if not model:
            logger.error('No model to register.. django-pushy will not help too much.')
            continue
        else:
            logger.debug('Registering model: %s' % model)
            post_save.connect(pushy_post_save, sender=model)


setup_signals()

