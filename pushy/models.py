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
    print obj
    message = {
               'uuid': obj.uuid,
               'route': obj.get_api_url(),
               'type': 'update'
               }
    print message
    rs.publish('%s%s' % (pushy_settings.get_channel(), 'update'), json.dumps(message))
    

def setup_signals():

    for model in pushy_settings.get_models().values():
        if not model:
            logger.error('No model')
            continue
        else:
            logger.debug('Registering model: %s' % model)
            post_save.connect(pushy_post_save, sender=model)


setup_signals()

