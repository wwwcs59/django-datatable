#!/usr/bin/env python
# coding: utf-8

class Column(object):
    def __init__(self, field=None, index=False, attrs={}, header=None, header_attrs={}):
        self.field = field
        self.index = index
        self.attrs = attrs
        self.header = ColumnHeader(text=header, attrs=header_attrs)

    def render_attrs(self):
        """ Render attributes of <td> to html.
        """
        html = ''
        for attr in self.attrs:
            html = html + '{0}={1}'.format(attr, self.attrs.get(attr))
        return html


class ColumnHeader(object):

    def __init__(self, text=None, attrs={}):
        self.text = text
        self.attrs = attrs
        
    def render_attrs(self):
        """ Render attributes of <th> to html.
        """
        html = ''
        for attr in self.attrs:
            html = html + '{0}={1}'.format(attr, self.attrs.get(attr))
        return html
