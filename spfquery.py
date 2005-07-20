#!/usr/bin/python2.3

# Author: Stuart D. Gathman <stuart@bmsi.com>
# Copyright 2004 Business Management Systems, Inc.
# This code is under the GNU General Public License.  See COPYING for details.

# $Log$
# Revision 1.1.1.1  2005/05/31 18:07:19  customdesigned
# Release 0.6.9
#
# Revision 2.3  2004/04/19 22:12:11  stuart
# Release 0.6.9
#
# Revision 2.2  2004/04/18 03:29:35  stuart
# Pass most tests except -local and -rcpt-to
#
# Revision 2.1  2004/04/08 18:41:15  stuart
# Reject numeric hello names
#
# Driver for SPF test system

import spf
import sys

from optparse import OptionParser

class PerlOptionParser(OptionParser):
    def _process_args (self, largs, rargs, values):
        """_process_args(largs : [string],
                         rargs : [string],
                         values : Values)

        Process command-line arguments and populate 'values', consuming
        options and arguments from 'rargs'.  If 'allow_interspersed_args' is
        false, stop at the first non-option argument.  If true, accumulate any
        interspersed non-option arguments in 'largs'.
        """
        while rargs:
            arg = rargs[0]
            # We handle bare "--" explicitly, and bare "-" is handled by the
            # standard arg handler since the short arg case ensures that the
            # len of the opt string is greater than 1.
            if arg == "--":
                del rargs[0]
                return
            elif arg[0:2] == "--":
                # process a single long option (possibly with value(s))
                self._process_long_opt(rargs, values)
            elif arg[:1] == "-" and len(arg) > 1:
                # process a single perl style long option
		rargs[0] = '-' + arg
                self._process_long_opt(rargs, values)
            elif self.allow_interspersed_args:
                largs.append(arg)
                del rargs[0]
            else:
		return

def format(q):
  res,code,txt = q.check()
  print res
  if res in ('pass','neutral','unknown'): print
  else: print txt
  print 'spfquery:',q.get_header_comment(res)
  print 'Received-SPF:',q.get_header(res,'spfquery')

def main(argv):
  parser = PerlOptionParser()
  parser.add_option("--file",dest="file")
  parser.add_option("--ip",dest="ip")
  parser.add_option("--sender",dest="sender")
  parser.add_option("--helo",dest="hello_name")
  parser.add_option("--local",dest="local_policy")
  parser.add_option("--rcpt-to",dest="rcpt")
  parser.add_option("--default-explanation",dest="explanation")
  parser.add_option("--sanitize",type="int",dest="sanitize")
  parser.add_option("--debug",type="int",dest="debug")
  opts,args = parser.parse_args(argv)
  if opts.ip:
    q = spf.query(opts.ip,opts.sender,opts.hello_name,local=opts.local_policy)
    if opts.explanation:
      q.set_default_explanation(opts.explanation)
    format(q)
  if opts.file:
    if opts.file == '0':
      fp = sys.stdin
    else:
      fp = open(opts.file,'r')
    for ln in fp:
      ip,sender,helo,rcpt = ln.split(None,3)
      q = spf.query(ip,sender,helo,local=opts.local_policy)
      if opts.explanation:
	q.set_default_explanation(opts.explanation)
      format(q)
    fp.close()
    
if __name__ == "__main__":
  import sys
  main(sys.argv[1:])
