from flask.ext.wtf import regexp

from flaskext.babel import lazy_gettext as _

USERNAME_RE = r'^[\w.+-]+$'

is_username = regexp(USERNAME_RE,
                     message=_("You can only use letters, numbers or dashes"))


