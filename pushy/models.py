import logging
from django.db import models
from django.db.models.signals import post_save
import redis
import json
import time

from pushy import settings as pushy_settings

from multiprocessing import Pool

logger = logging.getLogger(__name__)

pool = Pool(processes=10)

def pushy_publish(channel, key, message):
    rs = redis.StrictRedis()
    time.sleep(0.005)
    rs.publish('%s%s' % (channel, key), json.dumps(message))
    

def pushy_post_save(sender, **kwargs):
    rs = redis.StrictRedis()
    obj = kwargs['instance']
    
    message = {
               'route': obj.get_api_url(),
               'type': 'update'
               }
    logger.debug('Routing message to: %s' % pushy_settings.get_channel())
    
    #pushy_publish(pushy_settings.get_channel(), 'update', message)
    
    pool.apply_async(pushy_publish(pushy_settings.get_channel(), 'update', message))
    
    """
    
    
    print 'SLEEEEEEEEEEEEEEEEEP!'
    time.sleep(0.5)
    rs.publish('%s%s' % (pushy_settings.get_channel(), 'update'), json.dumps(message))
    """

def setup_signals():

    for model in pushy_settings.get_models().values():
        if not model:
            logger.error('No model to register.. django-pushy will not help too much.')
            continue
        else:
            logger.debug('Registering model: %s' % model)
            post_save.connect(pushy_post_save, sender=model)


setup_signals()

