from django.shortcuts import render
import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)

def index(request):
    logger.info('Index page acsessed')
    return HttpResponse('Hello world')

def about(request):
    try:
        result = 1/0
    except Exception as e:
        logger.exception(f'error in about page: {e}')
        return HttpResponse("about us")
    else:
        logger.debug('About page acsessed')
        return HttpResponse("This is the about page")