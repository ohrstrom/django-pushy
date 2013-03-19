from django.db import models
from django.db.models.signals import post_save
import redis
import json

from pushy import settings as pushy_settings


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
    rs.publish('pushy_update', json.dumps(message))
    

def setup_signals():

    for model in pushy_settings.get_models().values():
        if not model:
            print 'not model'
            continue
        else:
            print 'registering!'
            post_save.connect(pushy_post_save, sender=model)


setup_signals()

