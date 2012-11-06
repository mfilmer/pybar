import sys

class ProgressBar(object):
    def __init__(self, width=80, position=0, fillchar='=', boundchars=('[',']')):
        self._totalwidth = int(width)
        if len(fillchar) != 1:
            raise ValueError('fillchar must be a single character')
        self._fillchar = fillchar
        self._startchar = boundchars[0]
        self._endchar = boundchars[1]
        self._usablewidth = width - 5 - \
                len(self._startchar) - len(self._endchar)

        sys.stdout.write('\n')
        self.update(position)

    def update(self, position):
        if position < 0 or position > 1:
            raise ValueError('position must be between 0 and 1')

        if self._usablewidth > 0:
            fillcount = int(self._usablewidth * position)
            sys.stdout.write('\r{0}{1}{2}{3} {4}%'.format(self._startchar, 
                    self._fillchar * fillcount, 
                    ' ' * (self._usablewidth-fillcount), 
                    self._endchar, int(position*100)))
        else:
            sys.stdout.write('\r{0}%'.format(int(position*100)))

    def done(self):
        if self._usablewidth > 0:
            sys.stdout.write('\r{0}{1}{2} done\n'.format(self._startchar, \
                    self._fillchar*self._usablewidth, self._endchar))
        else:
            sys.stdout.write('\rdone\n')
