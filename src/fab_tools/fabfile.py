from fabric.api import env
from fabric.api import run, prefix
from fabric.context_managers import cd
#from fabric.operations import sudo
from fab_tools.fab_settings import USER, PASSWORD, PATH_PROJECT, PATH_PROJECT_SRC

def test():
    env.host = ["lgarimaldi.tuxis.com.ar"]
    env.user = USER.text
