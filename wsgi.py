import os, sys

DIRNAME=os.path.abspath(os.path.join(os.path.dirname(__file__),".."))

sys.path.append(DIRNAME)
sys.path.append(os.path.join(DIRNAME, '..'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'DepOA.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
import isapi_wsgi
# The entry points for the ISAPI extension.
def __ExtensionFactory__():
    return isapi_wsgi.ISAPISimpleHandler(application)
if __name__=='__main__':
# If run from the command-line, install ourselves.
    from isapi.install import *
    params = ISAPIParameters()
# Setup the virtual directories - this is a list of directories our
# extension uses - in this case only 1.
# Each extension has a "script map" - this is the mapping of ISAPI
# extensions.
    sm = [ScriptMapParams(Extension="*", Flags=0)]
    vd = VirtualDirParameters(Name="DepOA",Description = "ISAPI-WSGI ISAPISimpleHandler Django DepOA",ScriptMaps = sm,ScriptMapUpdate = "replace")
    params.VirtualDirs = [vd]
    HandleCommandLine(params)
