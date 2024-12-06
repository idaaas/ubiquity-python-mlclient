# This file was automatically generated by SWIG (https://www.swig.org).
# Version 4.3.0
#
# Do not make changes to this file unless you know what you are doing - modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _libUbiquityClientWrapper
else:
    import _libUbiquityClientWrapper

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "this":
            set(self, name, value)
        elif name == "thisown":
            self.this.own(value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class ClientHandle(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        _libUbiquityClientWrapper.ClientHandle_swiginit(self, _libUbiquityClientWrapper.new_ClientHandle())

    def close(self):
        return _libUbiquityClientWrapper.ClientHandle_close(self)

    def getCreativeId(self):
        return _libUbiquityClientWrapper.ClientHandle_getCreativeId(self)

    def getQueryId(self):
        return _libUbiquityClientWrapper.ClientHandle_getQueryId(self)

    def getModelId(self):
        return _libUbiquityClientWrapper.ClientHandle_getModelId(self)

    def getStatusCode(self):
        return _libUbiquityClientWrapper.ClientHandle_getStatusCode(self)

    def getStatusString(self):
        return _libUbiquityClientWrapper.ClientHandle_getStatusString(self)

    def getPrice(self):
        return _libUbiquityClientWrapper.ClientHandle_getPrice(self)

    def getPredictionType(self):
        return _libUbiquityClientWrapper.ClientHandle_getPredictionType(self)

    def getProbability(self):
        return _libUbiquityClientWrapper.ClientHandle_getProbability(self)

    def poll(self):
        return _libUbiquityClientWrapper.ClientHandle_poll(self)

    def predict(self):
        return _libUbiquityClientWrapper.ClientHandle_predict(self)

    def putBoolean(self, value):
        return _libUbiquityClientWrapper.ClientHandle_putBoolean(self, value)

    def putCategorical(self, value):
        return _libUbiquityClientWrapper.ClientHandle_putCategorical(self, value)

    def putCreative(self, value):
        return _libUbiquityClientWrapper.ClientHandle_putCreative(self, value)

    def putNominal(self, value):
        return _libUbiquityClientWrapper.ClientHandle_putNominal(self, value)

    def putNumeric(self, value):
        return _libUbiquityClientWrapper.ClientHandle_putNumeric(self, value)

    def startBidShading(self, modelId, queryId, bidPrice, bidFloor):
        return _libUbiquityClientWrapper.ClientHandle_startBidShading(self, modelId, queryId, bidPrice, bidFloor)

    def startLineItem(self, modelId, queryId, maxCPM):
        return _libUbiquityClientWrapper.ClientHandle_startLineItem(self, modelId, queryId, maxCPM)

    def startProbability(self, modelId, queryId):
        return _libUbiquityClientWrapper.ClientHandle_startProbability(self, modelId, queryId)

    def train(self, modelId, queryId, level):
        return _libUbiquityClientWrapper.ClientHandle_train(self, modelId, queryId, level)
    __swig_destroy__ = _libUbiquityClientWrapper.delete_ClientHandle

# Register ClientHandle in _libUbiquityClientWrapper:
_libUbiquityClientWrapper.ClientHandle_swigregister(ClientHandle)

def getStatusString(statusCode):
    return _libUbiquityClientWrapper.getStatusString(statusCode)

def setAeronDirectory(directoryPath):
    return _libUbiquityClientWrapper.setAeronDirectory(directoryPath)

def setCredential(tenantId):
    return _libUbiquityClientWrapper.setCredential(tenantId)

def setApiAddress(root):
    return _libUbiquityClientWrapper.setApiAddress(root)

def setResourceStringInCache(id, configString):
    return _libUbiquityClientWrapper.setResourceStringInCache(id, configString)

def getClientHandle(*args):
    return _libUbiquityClientWrapper.getClientHandle(*args)

def openClient(clusterId):
    return _libUbiquityClientWrapper.openClient(clusterId)

def closeClient():
    return _libUbiquityClientWrapper.closeClient()

def xxh3_64bits(source):
    return _libUbiquityClientWrapper.xxh3_64bits(source)

MISSING_BOOLEAN = -1
MISSING_CATEGORICAL = -1
MISSING_NOMINAL = "_MISSING_"
MISSING_NUMERIC = float('nan')

UNDEFINED  = 0

SUCCESS  = 1
NO_DATA  = 2
BACK_PRESSURED  = 3
NO_COMPATIBLE_NODE  = 4

ARCHITECTURE_NOT_SUPPORTED  = 0x20001
AERON_INITIALIZATION_FAILED  = 0x20002
INVALID_RESOURCE_ID  = 0x20003
INVALID_APP_FOR_MODEL  = 0x20004
MISMATCHED_FEATURE_TYPE  = 0x20005
INVALID_FEEDBACK_LEVEL  = 0x20006
MISSING_CREATIVES  = 0x20007
TOO_MANY_CREATIVES  = 0x20008
MISPLACED_CREATIVE_ID  = 0x20009
NO_API_RESPONSE  = 0x2000A
FORBIDDEN  = 0x2000B
UNKNOWN_RESOURCE  = 0x2000C
OTHER_FETCH_ERROR  = 0x2000D
INVALID_CLUSTER_DESCRIPTION  = 0x2000E

APP_BID_SHADING  = 0
APP_PROBABILITY  = 1
APP_LINE_ITEM  = 2
APP_UNDEFINED  = 3