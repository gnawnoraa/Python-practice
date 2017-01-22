""" practice python
    Written by: 105598065
    Date: 2017/01/20
"""

# ==================== class: Chain ====================
class Chain(object):

    def __init__(self, path = ''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    """
    def users(self, str):
        self._path = ':' + str
        return self._path
    """

# ==================== Statements ====================
print Chain().status.user.timeline.list