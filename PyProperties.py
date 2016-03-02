# -*- coding: utf-8 -*-
import os


class Properties:
    def __init__(self, prop_file, is_strip=False):
        self.path = os.path.normpath(prop_file)
        if not os.path.isfile(self.path):
            raise IOError("The path that you specified is not a file.")
        else:
            self.file = open(self.path, 'r+')
            lines = self.file.readlines()
            self.mappings = {}
            for line in lines:
                if not line.lstrip().startswith('#'):
                    key_value = line.split('=')
                    if 1 < len(key_value):
                        if is_strip:
                            self.mappings[key_value[0]] = key_value[1].rstrip('\r').rstrip('\n')
                        else:
                            self.mappings[key_value[0]] = key_value[1]
            self.file.close()

    def get_property(self, key):
        if self.mappings.has_key(key):
            return self.mappings[key]
        else:
            return None

    def set_property(self, key, value):
        if self.mappings.has_key(key):
            self.mappings[key] = value

    def store(self):
        if not os.path.isfile(self.path):
            raise IOError("The path that you specified is not a file.")
        else:
            lkey_value = []
            for key, value in self.mappings.iteritems():
                lkey_value.append(key + '=' + value + '\n')
            f = open(self.path, 'wb')
            f.writelines(lkey_value)
            f.flush()
            f.close()
