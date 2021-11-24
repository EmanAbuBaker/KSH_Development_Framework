from django.shortcuts import render

# Create your views here.


# Logging view in Django :
# First import the logging library from Python's standard library:
import os 
import logging
# Create a logger for this file or the name of the log level :
logger = logging.getLogger(__file__)
# or Get an instance of a logger:
logger = logging.getLogger(__name__)
