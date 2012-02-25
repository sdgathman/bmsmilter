#!/usr/bin/env python
# A simple milter that has grown quite a bit.
# $Log$
# Revision 1.178  2011/11/05 16:05:08  customdesigned
# Change openspf.org -> openspf.net
#
# Revision 1.177  2011/11/01 17:43:33  customdesigned
# Trust trusted relay not to be a zombie.
#
# Revision 1.176  2011/10/03 20:07:16  customdesigned
# Make wiretap use orig_from (set efrom to orig_from earlier).
#
# Revision 1.175  2011/10/03 20:01:00  customdesigned
# Let NOTIFY suppress real DSN.  Since notify is forged on forged email,
# perhaps this should be an option.
#
# Revision 1.174  2011/10/03 17:44:38  customdesigned
# Fix SPF fail ip reported for IP6
#
# Revision 1.173  2011/06/16 20:54:48  customdesigned
# Update to pydkim-0.4 and log verified domains
#
# Revision 1.172  2011/06/07 22:24:38  customdesigned
# Remove leftover tempname in envfrom.  Save failed DKIM
#
# Revision 1.171  2011/06/07 19:45:01  customdesigned
# Check DKIM (log only)
#
# Revision 1.170  2011/05/18 02:50:54  customdesigned
# Improve chinese detection
#
# Revision 1.169  2011/04/13 19:50:04  customdesigned
# Move persistent data to /var/lib/milter
#
# Revision 1.168  2011/04/01 02:34:38  customdesigned
# Fix efrom and umis with delayed reject.
#
# Revision 1.166  2011/03/05 05:12:55  customdesigned
# Release 0.8.15
#
# Revision 1.165  2011/03/03 21:45:24  customdesigned
# Extract original MFROM from SRS
#
# Revision 1.164  2010/10/27 03:07:33  customdesigned
# Whitelist recipients from signed MFROM if aborted before DATA.
#
# Revision 1.163  2010/10/16 21:23:00  customdesigned
# Send auto-whitelist recipients to whitelist_mx
#
# Revision 1.162  2010/08/18 03:58:06  customdesigned
# Fix typos
#
# Revision 1.161  2010/08/18 03:52:09  customdesigned
# Update reputation of parsed Received-SPF header if no Gossip header.
#
# Revision 1.160  2010/06/04 03:50:28  customdesigned
# Allow wildcards just above TLD.
#
# Revision 1.159  2010/05/27 21:22:41  customdesigned
# Fix helo policy lookup
#
# Revision 1.158  2010/05/27 18:23:33  customdesigned
# Support HELO policies.
#
# Revision 1.157  2010/05/22 03:57:17  customdesigned
# Bandomain aliases to ban wildcards.
#
# Revision 1.155  2010/04/16 19:51:05  customdesigned
# Max_demerits config to disable banning ips.
#
# Revision 1.154  2010/04/09 18:37:53  customdesigned
# Best guess pass is good enough to get quarrantine DSN or get banned.
#
# Revision 1.153  2010/04/09 18:23:34  customdesigned
# Don't ban just for repeated anonymous MFROM
#
# Revision 1.152  2010/02/15 21:02:29  customdesigned
# Lower reputation bar to avoid greylisting.
#
# Revision 1.151  2009/12/31 19:23:18  customdesigned
# Don't check From unless dspam enabled.
#
# Revision 1.150  2009/12/30 20:53:20  customdesigned
# Require pymilter >= 0.9.3
#
# Revision 1.149  2009/09/14 14:59:53  customdesigned
# Allow illegal HELO from internal to accomodate broken copier firmware.
#
# Revision 1.148  2009/09/14 14:28:22  customdesigned
# Heuristically recognize multiple MXs.
#
# Revision 1.147  2009/09/14 14:24:11  customdesigned
# Trust 127.0.0.1 not to be a zombie
#
# Revision 1.146  2009/08/29 03:38:27  customdesigned
# Don't ban domains unless gossip score available.
#
# Revision 1.145  2009/08/27 21:18:16  customdesigned
# Track banned domains and expand the offenses that can ban an IP.
#
# Revision 1.141  2009/05/20 02:48:18  customdesigned
# Restrict internal DSNs to official MTAs.
#
# Revision 1.140  2009/02/04 02:40:14  customdesigned
# Parse gossip header before add_spam.  Replace nulls in smtp error txt.
# Default internal_policy flag false.
#
# Revision 1.139  2008/12/22 02:34:39  customdesigned
# Fix internal policy
#
# Revision 1.138  2008/12/13 21:22:51  customdesigned
# Split off pymilter
#
# Revision 1.137  2008/12/06 21:13:57  customdesigned
# Fix some reject messages.
#
# Revision 1.136  2008/12/04 19:42:46  customdesigned
# SPF Pass policy
#
# Revision 1.135  2008/10/23 19:58:06  customdesigned
# Example config had different names than actual code :-)
#
# Revision 1.134  2008/10/11 15:45:46  customdesigned
# Don't greylist DSNs.
#
# Revision 1.133  2008/10/09 18:44:54  customdesigned
# Skip greylisting for good reputation.
#
# Revision 1.132  2008/10/09 00:55:13  customdesigned
# Don't reset greylist timer on early retries.
#
# Revision 1.131  2008/10/08 04:57:28  customdesigned
# Greylisting
#
# Revision 1.130  2008/10/02 03:19:00  customdesigned
# Delay strike3 REJECT and don't reject if whitelisted.
# Recognize vacation messages as autoreplies.
#
# Revision 1.129  2008/09/09 23:24:56  customdesigned
# Never ban a trusted relay.
#
# Revision 1.128  2008/09/09 23:08:16  customdesigned
# Wasn't reading banned_ips
#
# Revision 1.127  2008/08/25 18:32:22  customdesigned
# Handle missing gossip_node so self tests pass.
#
# Revision 1.126  2008/08/18 17:47:57  customdesigned
# Log rcpt for SRS rejections.
#
# Revision 1.125  2008/08/06 00:52:38  customdesigned
# CBV policy sends no DSN.  DSN policy sends DSN.
#
# Revision 1.124  2008/08/05 18:04:06  customdesigned
# Send quarantine DSN to SPF PASS only.
#
# Revision 1.123  2008/07/29 21:59:29  customdesigned
# Parse ESMTP params
#
# Revision 1.122  2008/05/08 21:35:56  customdesigned
# Allow explicitly whitelisted email from banned_users.
#
# Revision 1.121  2008/04/10 14:59:35  customdesigned
# Configure gossip TTL.
#
# Revision 1.120  2008/04/02 18:59:14  customdesigned
# Release 0.8.10
#
# Revision 1.119  2008/04/01 00:13:10  customdesigned
# Do not CBV whitelisted addresses.  We already know they are good.
#
# Revision 1.118  2008/01/09 20:15:49  customdesigned
# Handle unquoted fullname when parsing email.
#
# Revision 1.117  2007/11/29 14:35:17  customdesigned
# Packaging tweaks.
#
# Revision 1.116  2007/11/01 20:09:14  customdesigned
# Support temperror policy in access.
#
# Revision 1.115  2007/10/10 18:23:54  customdesigned
# Send quarantine DSN to SPF pass (official or guessed) only.
# Reject blacklisted email too big for dspam.
#
# Revision 1.114  2007/10/10 18:07:50  customdesigned
# Check porn keywords in From header field.
#
# Revision 1.113  2007/09/25 16:37:26  customdesigned
# Tested on RH7
#
# Revision 1.112  2007/09/13 14:51:03  customdesigned
# Report domain on reputation reject.
#
# Revision 1.111  2007/07/25 17:14:59  customdesigned
# Move milter apps to /usr/lib/pymilter
#
# Revision 1.110  2007/07/02 03:06:10  customdesigned
# Ban ips on bad mailfrom offenses as well as bad rcpts.
#
# Revision 1.109  2007/06/23 20:53:05  customdesigned
# Ban IPs based on too many invalid recipients in a connection.  Requires
# configuring check_user.  Tighten HELO best_guess policy.
#
# Revision 1.108  2007/04/19 16:02:43  customdesigned
# Do not process valid SRS recipients as delayed_failure.
#
# Revision 1.107  2007/04/15 01:01:13  customdesigned
# Ban ips with too many bad rcpts on a connection.
#
# Revision 1.105  2007/04/13 17:20:09  customdesigned
# Check access_file at startup.  Compress rcpt to log.
#
# Revision 1.104  2007/04/05 17:59:07  customdesigned
# Stop querying gossip server twice.
#
# Revision 1.103  2007/04/02 18:37:25  customdesigned
# Don't disable gossip for temporary error.
#
# Revision 1.102  2007/03/30 18:13:41  customdesigned
# Report bestguess and helo-spf as key-value pairs in Received-SPF
# instead of in their own headers.
#
# Revision 1.101  2007/03/29 03:06:10  customdesigned
# Don't count DSN and unqualified MAIL FROM as internal_domain.
#
# Revision 1.100  2007/03/24 00:30:24  customdesigned
# Do not CBV for internal domains.
#
# See ChangeLog
#
# Author: Stuart D. Gathman <stuart@bmsi.com>
# Copyright 2001,2002,2003,2004,2005-2010 Business Management Systems, Inc.
# This code is under the GNU General Public License.  See COPYING for details.

import sys
import os
import StringIO
import mime
import email.Errors
import Milter
import tempfile
import time
import socket
import re
import shutil
import gc
import anydbm
import smtplib
import urllib
import Milter.dsn as dsn
from Milter.dynip import is_dynip as dynip
from Milter.utils import \
        iniplist,parse_addr,parse_header,ip4re,addr2bin,parseaddr
from Milter.config import MilterConfigParser
from Milter.greylist import Greylist

from fnmatch import fnmatchcase
from email.Utils import getaddresses
from glob import glob

# Import gossip if available
try:
  import gossip
  import gossip.client
  import gossip.server
  gossip_node = None
except: gossip = None

# Import pysrs if available
try:
  import SRS
  srsre = re.compile(r'^SRS[01][+-=]',re.IGNORECASE)
except: SRS = None
try:
  import SES
except: SES = None

# Import spf if available
try: import spf
except: spf = None

# Import dkim if available
try: import dkim
except: dkim = None

# Sometimes, MTAs reply to our DSN.  We recognize this type of reply/DSN
# and check for the original recipient SRS encoded in Message-ID.
# If found, we blacklist that recipient.
_subjpats = (
 r'^failure notice',
 r'^subjectbounce',
 r'^returned mail',
 r'^undeliver',
 r'\bdelivery\b.*\bfail',
 r'\bdelivery problem',
 r'\bnot\s+be\s+delivered',
 r'\buser unknown\b',
 r'^failed', r'^mail failed',
 r'^echec de distribution',
 r'\berror\s+sending\b',
 r'^fallo en la entrega',
 r'\bfehlgeschlagen\b'
)
refaildsn = re.compile('|'.join(_subjpats),re.IGNORECASE)

# We don't want to whitelist recipients of Autoreplys and other robots.
# There doesn't seem to be a foolproof way to recognize these, so
# we use this heuristic.  The worst that can happen is someone won't get
# whitelisted when they should, or we'll whitelist some spammer for a while.
_autopats = (
 r'^read:',
 r'\bautoreply:\b',
 r'^return receipt',
 r'^Your message\b.*\bawaits moderator approval'
)
reautoreply = re.compile('|'.join(_autopats),re.IGNORECASE)
import logging

# Thanks to Chris Liechti for config parsing suggestions

# Global configuration defaults suitable for test framework.
socketname = "/tmp/pythonsock"
reject_virus_from = ()
delayed_reject = True
wiretap_users = {}
discard_users = {}
wiretap_dest = None
mail_archive = None
_archive_lock = None
blind_wiretap = True
check_user = {}
block_forward = {}
hide_path = ()
log_headers = False
block_chinese = False
case_sensitive_localpart = False
spam_words = ()
porn_words = ()
from_words = ()
banned_exts = mime.extlist.split(',')
scan_zip = False
scan_html = True
scan_rfc822 = True
internal_policy = False
internal_connect = ()
trusted_relay = ()
private_relay = ()
internal_mta = ()
trusted_forwarder = ()
internal_domains = ()
banned_users = ()
hello_blacklist = ()
smart_alias = {}
dspam_dict = None
dspam_users = {}
dspam_train = {}
dspam_userdir = None
dspam_exempt = {}
dspam_whitelist = {}
whitelist_senders = {}
whitelist_mx = ()
dspam_screener = ()
dspam_internal = True   # True if internal mail should be dspammed
dspam_reject = ()
dspam_sizelimit = 180000
srs = None
ses = None
srs_reject_spoofed = False
srs_domain = ()
spf_reject_neutral = ()
spf_accept_softfail = ()
spf_accept_fail = ()
spf_best_guess = False
spf_reject_noptr = False
supply_sender = False
access_file = None
timeout = 600
banned_ips = set()
banned_domains = set()
greylist = None
UNLIMITED = 0x7fffffff
max_demerits = UNLIMITED
errors_url = "http://bmsi.com/cgi-bin/errors.cgi"

logging.basicConfig(
        stream=sys.stdout,
        level=logging.INFO,
        format='%(asctime)s %(message)s',
        datefmt='%Y%b%d %H:%M:%S'
)
milter_log = logging.getLogger('milter')

def read_config(list):
  cp = MilterConfigParser({
    'tempdir': "/var/log/milter/save",
    'datadir': "/var/lib/milter",
    'socket': "/var/run/milter/pythonsock",
    'errors_url': "http://bmsi.com/cgi-bin/errors.cgi",
    'scan_html': 'no',
    'scan_rfc822': 'yes',
    'scan_zip': 'no',
    'block_chinese': 'no',
    'log_headers': 'no',
    'blind_wiretap': 'yes',
    'reject_spoofed': 'no',
    'reject_noptr': 'no',
    'supply_sender': 'no',
    'best_guess': 'no',
    'dspam_internal': 'yes',
    'case_sensitive_localpart': 'no',
    'internal_policy': 'no'
  })
  cp.read(list)
  if cp.has_option('milter','datadir'):
      print "chdir:",cp.get('milter','datadir')
      os.chdir(cp.get('milter','datadir'))

  # milter section
  tempfile.tempdir = cp.get('milter','tempdir')
  global socketname, timeout, check_user, log_headers
  global internal_connect, internal_domains, trusted_relay, hello_blacklist
  global case_sensitive_localpart, private_relay, internal_mta, max_demerits
  socketname = cp.get('milter','socket')
  timeout = cp.getintdefault('milter','timeout',600)
  check_user = cp.getaddrset('milter','check_user')
  log_headers = cp.getboolean('milter','log_headers')
  internal_connect = cp.getlist('milter','internal_connect')
  internal_domains = cp.getlist('milter','internal_domains')
  trusted_relay = cp.getlist('milter','trusted_relay')
  private_relay = cp.getlist('milter','private_relay')
  internal_mta = cp.getlist('milter','internal_mta')
  hello_blacklist = cp.getlist('milter','hello_blacklist')
  case_sensitive_localpart = cp.getboolean('milter','case_sensitive_localpart')
  max_demerits = cp.getintdefault('milter','max_demerits',UNLIMITED)
  errors_url = cp.get('milter','errors_url')

  # defang section
  global scan_rfc822, scan_html, block_chinese, scan_zip, block_forward
  global banned_exts, porn_words, spam_words, from_words
  if cp.has_section('defang'):
    section = 'defang'
    # for backward compatibility,
    # banned extensions defaults to empty only when defang section exists
    banned_exts = cp.getlist(section,'banned_exts')
  else: # use milter section if no defang section for compatibility
    section = 'milter'
  scan_rfc822 = cp.getboolean(section,'scan_rfc822')
  scan_zip = cp.getboolean(section,'scan_zip')
  scan_html = cp.getboolean(section,'scan_html')
  block_chinese = cp.getboolean(section,'block_chinese')
  block_forward = cp.getaddrset(section,'block_forward')
  porn_words = [x for x in cp.getlist(section,'porn_words') if len(x) > 1]
  spam_words = [x for x in cp.getlist(section,'spam_words') if len(x) > 1]
  from_words = [x for x in cp.getlist(section,'from_words') if len(x) > 1]

  # scrub section
  global hide_path, reject_virus_from, internal_policy
  hide_path = cp.getlist('scrub','hide_path')
  reject_virus_from = cp.getlist('scrub','reject_virus_from')
  internal_policy = cp.getboolean('scrub','internal_policy')

  # wiretap section
  global blind_wiretap,wiretap_users,wiretap_dest,discard_users,mail_archive
  blind_wiretap = cp.getboolean('wiretap','blind')
  wiretap_users = cp.getaddrset('wiretap','users')
  discard_users = cp.getaddrset('wiretap','discard')
  wiretap_dest = cp.getdefault('wiretap','dest')
  if wiretap_dest: wiretap_dest = '<%s>' % wiretap_dest
  mail_archive = cp.getdefault('wiretap','archive')

  global smart_alias
  for sa,v in [
      (k,cp.get('wiretap',k)) for k in cp.getlist('wiretap','smart_alias')
    ] + (cp.has_section('smart_alias') and cp.items('smart_alias',True) or []):
    print sa,v
    sm = [q.strip() for q in v.split(',')]
    if len(sm) < 2:
      milter_log.warning('malformed smart alias: %s',sa)
      continue
    if len(sm) == 2: sm.append(sa)
    if case_sensitive_localpart:
      key = (sm[0],sm[1])
    else:
      key = (sm[0].lower(),sm[1].lower())
    smart_alias[key] = sm[2:]

  # dspam section
  global dspam_dict, dspam_users, dspam_userdir, dspam_exempt, dspam_internal
  global dspam_screener,dspam_whitelist,dspam_reject,dspam_sizelimit
  global whitelist_senders,whitelist_mx
  whitelist_senders = cp.getaddrset('dspam','whitelist_senders')
  whitelist_mx = cp.getlist('dspam','whitelist_mx')
  dspam_dict = cp.getdefault('dspam','dspam_dict')
  dspam_exempt = cp.getaddrset('dspam','dspam_exempt')
  dspam_whitelist = cp.getaddrset('dspam','dspam_whitelist')
  dspam_users = cp.getaddrdict('dspam','dspam_users')
  dspam_userdir = cp.getdefault('dspam','dspam_userdir')
  dspam_screener = cp.getlist('dspam','dspam_screener')
  dspam_train = set(cp.getlist('dspam','dspam_train'))
  dspam_reject = cp.getlist('dspam','dspam_reject')
  dspam_internal = cp.getboolean('dspam','dspam_internal')
  if cp.has_option('dspam','dspam_sizelimit'):
    dspam_sizelimit = cp.getint('dspam','dspam_sizelimit')

  # spf section
  global spf_reject_neutral,spf_best_guess,SRS,spf_reject_noptr
  global spf_accept_softfail,spf_accept_fail,supply_sender,access_file
  global trusted_forwarder
  if spf:
    spf.DELEGATE = cp.getdefault('spf','delegate')
    spf_reject_neutral = cp.getlist('spf','reject_neutral')
    spf_accept_softfail = cp.getlist('spf','accept_softfail')
    spf_accept_fail = cp.getlist('spf','accept_fail')
    spf_best_guess = cp.getboolean('spf','best_guess')
    spf_reject_noptr = cp.getboolean('spf','reject_noptr')
    supply_sender = cp.getboolean('spf','supply_sender')
    access_file = cp.getdefault('spf','access_file')
    trusted_forwarder = cp.getlist('spf','trusted_forwarder')
  srs_config = cp.getdefault('srs','config')
  if srs_config: cp.read([srs_config])
  srs_secret = cp.getdefault('srs','secret')
  if SRS and srs_secret:
    global ses,srs,srs_reject_spoofed,srs_domain,banned_users
    database = cp.getdefault('srs','database')
    srs_reject_spoofed = cp.getboolean('srs','reject_spoofed')
    maxage = cp.getintdefault('srs','maxage',8)
    hashlength = cp.getintdefault('srs','hashlength',8)
    separator = cp.getdefault('srs','separator','=')
    if database:
      import SRS.DB
      srs = SRS.DB.DB(database=database,secret=srs_secret,
        maxage=maxage,hashlength=hashlength,separator=separator)
    else:
      srs = SRS.Guarded.Guarded(secret=srs_secret,
        maxage=maxage,hashlength=hashlength,separator=separator)
    if SES:
      ses = SES.new(secret=srs_secret,expiration=maxage)
      srs_domain = set(cp.getlist('srs','ses'))
      srs_domain.update(cp.getlist('srs','srs'))
    else:
      srs_domain = set(cp.getlist('srs','srs'))
    srs_domain.update(cp.getlist('srs','sign'))
    srs_domain.add(cp.getdefault('srs','fwdomain'))
    banned_users = cp.getlist('srs','banned_users')

  if gossip:
    global gossip_node, gossip_ttl
    if cp.has_option('gossip','server'):
      server = cp.get('gossip','server')
      host,port = gossip.splitaddr(server)
      gossip_node = gossip.client.Gossip(host,port)
    else:
      gossip_node = gossip.server.Gossip('gossip4.db',1000)
      for p in cp.getlist('gossip','peers'):
        host,port = gossip.splitaddr(p)
        gossip_node.peers.append(gossip.server.Peer(host,port))
    gossip_ttl = cp.getintdefault('gossip','ttl',1)

  # greylist section
  if cp.has_option('greylist','dbfile'):
    global greylist
    grey_db = cp.getdefault('greylist','dbfile')
    grey_days = cp.getintdefault('greylist','retain',36)
    grey_expire = cp.getintdefault('greylist','expire',6)
    grey_time = cp.getintdefault('greylist','time',5)
    greylist = Greylist(grey_db,grey_time,grey_expire,grey_days)

def findsrs(fp):
  lastln = None
  for ln in fp:
    if lastln:
      if ln[0].isspace() and ln[0] != '\n':
        lastln += ln
        continue
      try:
        name,val = lastln.rstrip().split(None,1)
        pos = val.find('<SRS')
        if pos >= 0:
          end = val.find('>',pos+4)
          return srs.reverse(val[pos+1:end])
      except: pass
    lnl = ln.lower()
    if lnl.startswith('action:'):
      if lnl.split()[-1] != 'failed': break
    for k in ('message-id:','x-mailer:','sender:','references:'):
      if lnl.startswith(k):
        lastln = ln
        break

def inCharSets(v,*encs):
  try: u = unicode(v,'utf8')
  except: return True
  for enc in encs:
    try:  
      s = u.encode(enc,'backslashreplace')
      return s.count(r'\u') < 3
    except: UnicodeError
  return False

def param2dict(str):
  pairs = [x.split('=',1) for x in str]
  for e in pairs:
    if len(e) < 2: e.append(None)
  return dict([(k.upper(),v) for k,v in pairs])

class SPFPolicy(object):
  "Get SPF policy by result from sendmail style access file."
  def __init__(self,sender):
    self.sender = sender
    self.domain = sender.split('@')[-1].lower()
    if access_file:
      try: acf = anydbm.open(access_file,'r')
      except: acf = None
    else: acf = None
    self.acf = acf

  def close(self):
    if self.acf:
      self.acf.close()

  def getPolicy(self,pfx):
    acf = self.acf
    if not acf: return None
    try:
      return acf[pfx + self.sender]
    except KeyError:
      try:
        return acf[pfx + self.domain]
      except KeyError:
        try:
          return acf[pfx]
        except KeyError:
          return None

  def getFailPolicy(self):
    policy = self.getPolicy('spf-fail:')
    if not policy:
      if self.domain in spf_accept_fail:
        policy = 'CBV'
      else:
        policy = 'REJECT'
    return policy

  def getNonePolicy(self):
    policy = self.getPolicy('spf-none:')
    if not policy:
      if spf_reject_noptr:
        policy = 'REJECT'
      else:
        policy = 'CBV'
    return policy

  def getSoftfailPolicy(self):
    policy = self.getPolicy('spf-softfail:')
    if not policy:
      if self.domain in spf_accept_softfail:
        policy = 'OK'
      elif self.domain in spf_reject_neutral:
        policy = 'REJECT'
      else:
        policy = 'CBV'
    return policy

  def getNeutralPolicy(self):
    policy = self.getPolicy('spf-neutral:')
    if not policy:
      if self.domain in spf_reject_neutral:
        policy = 'REJECT'
      policy = 'OK'
    return policy

  def getPermErrorPolicy(self):
    policy = self.getPolicy('spf-permerror:')
    if not policy:
      policy = 'REJECT'
    return policy

  def getTempErrorPolicy(self):
    policy = self.getPolicy('spf-temperror:')
    if not policy:
      policy = 'REJECT'
    return policy

  def getPassPolicy(self):
    policy = self.getPolicy('spf-pass:')
    if not policy:
      policy = 'OK'
    return policy

from Milter.cache import AddrCache

cbv_cache = AddrCache(renew=7)
auto_whitelist = AddrCache(renew=60)
blacklist = AddrCache(renew=30)

def isbanned(dom,s):
  if dom in s: return True
  a = dom.split('.')
  if a[0] == '*': a = a[1:]
  if len(a) < 2: return False
  a[0] = '*'
  return isbanned('.'.join(a),s)
RE_MULTIMX = re.compile(r'^(mail|smtp|mx)[0-9]{1,3}[.]')

class bmsMilter(Milter.Base):
  """Milter to replace attachments poisonous to Windows with a WARNING message,
     check SPF, and other anti-forgery features, and implement wiretapping
     and smart alias redirection."""

  def log(self,*msg):
    milter_log.info('[%d] %s',self.id,' '.join([str(m) for m in msg]))

  def logstream(outerself):
    "Return a file like object that call self.log for each line"
    class LineWriter(object):
      def __init__(self):
	self._buf = ''

      def write(self,s):
	s = self._buf + s
	pos = s.find('\n')
	while pos >= 0:
	  outerself.log(s[:pos])
	  s = s[pos+1:]
	  pos = s.find('\n')
	self._buf = s
    return LineWriter()

  def __init__(self):
    self.tempname = None
    self.mailfrom = None        # sender in SMTP form
    self.canon_from = None      # sender in end user form
    self.fp = None
    self.pristine_headers = None
    self.bodysize = 0
    self.id = Milter.uniqueID()

  # delrcpt can only be called from eom().  This accumulates recipient
  # changes which can then be applied by alter_recipients()
  def del_recipient(self,rcpt):
    rcpt = rcpt.lower()
    if not rcpt in self.discard_list:
      self.discard_list.append(rcpt)

  # addrcpt can only be called from eom().  This accumulates recipient
  # changes which can then be applied by alter_recipients()
  def add_recipient(self,rcpt):
    rcpt = rcpt.lower()
    if not rcpt in self.redirect_list:
      self.redirect_list.append(rcpt)

  # addheader can only be called from eom().  This accumulates added headers
  # which can then be applied by alter_headers()
  def add_header(self,name,val,idx=-1):
    self.new_headers.append((name,val,idx))
    self.log('%s: %s' % (name,val))

  def delay_reject(self,*args,**kw):
    if delayed_reject:
      self.reject = (args,kw)
      return Milter.CONTINUE
    self.htmlreply(*args,**kw)
    return Milter.REJECT

  def connect(self,hostname,unused,hostaddr):
    self.internal_connection = False
    self.trusted_relay = False
    self.reject = None
    self.offenses = 0
    # sometimes people put extra space in sendmail config, so we strip
    self.receiver = self.getsymval('j').strip()
    if hostaddr and len(hostaddr) > 0:
      ipaddr = hostaddr[0]
      if iniplist(ipaddr,internal_connect):
        self.internal_connection = True
      if iniplist(ipaddr,trusted_relay):
        self.trusted_relay = True
    else: ipaddr = ''
    self.connectip = ipaddr
    self.missing_ptr = dynip(hostname,self.connectip)
    if self.internal_connection:
      connecttype = 'INTERNAL'
    else:
      connecttype = 'EXTERNAL'
    if self.trusted_relay:
      connecttype += ' TRUSTED'
    if self.missing_ptr:
      connecttype += ' DYN'
    self.log("connect from %s at %s %s" % (hostname,hostaddr,connecttype))
    self.hello_name = None
    self.connecthost = hostname
    if addr2bin(ipaddr) in banned_ips:
      self.log("REJECT: BANNED IP")
      return self.delay_reject('550','5.7.1', 'Banned for dictionary attacks')
    if hostname == 'localhost' and not ipaddr.startswith('127.') \
    or hostname == '.':
      self.log("REJECT: PTR is",hostname)
      return self.delay_reject('550','5.7.1',
        '"%s" is not a reasonable PTR name'%hostname)
    return Milter.CONTINUE

  def hello(self,hostname):
    self.hello_name = hostname
    self.log("hello from %s" % hostname)
    if not self.internal_connection:
      # Allow illegal HELO from internal network, some email enabled copier/fax
      # type devices (Toshiba) have broken firmware.
      if ip4re.match(hostname):
        self.log("REJECT: numeric hello name:",hostname)
        self.setreply('550','5.7.1','hello name cannot be numeric ip')
        return Milter.REJECT
      if hostname in hello_blacklist:
        self.log("REJECT: spam from self:",hostname)
        self.setreply('550','5.7.1',
          'Your mail server lies.  Its name is *not* %s.' % hostname)
        return self.offense(inc=4)
    if hostname == 'GC':
      n = gc.collect()
      self.log("gc:",n,' unreachable objects')
      self.log("auto-whitelist:",len(auto_whitelist),' entries')
      self.log("cbv_cache:",len(cbv_cache),' entries')
      self.setreply('550','5.7.1','%d unreachable objects'%n)
      return Milter.REJECT
    # HELO not allowed after MAIL FROM
    if self.mailfrom: self.offense(inc=2)
    return Milter.CONTINUE

  def smart_alias(self,to):
    if smart_alias:
      if case_sensitive_localpart:
        t = parse_addr(to)
      else:
        t = parse_addr(to.lower())
      if len(t) == 2:
        ct = '@'.join(t)
      else:
        ct = t[0]
      if case_sensitive_localpart:
        cf = self.efrom
      else:
        cf = self.efrom.lower()
      cf0 = cf.split('@',1)
      if len(cf0) == 2:
        cf0 = '@' + cf0[1]
      else:
        cf0 = cf
      for key in ((cf,ct),(cf0,ct)):
        if smart_alias.has_key(key):
          self.del_recipient(to)
          for t in smart_alias[key]:
            self.add_recipient('<%s>'%t)

  def offense(self,inc=1,min=0):
    self.offenses += inc
    if self.offenses < min:
      self.offenses = min
    if self.offenses > max_demerits and not self.trusted_relay:
      try:
        ip = addr2bin(self.connectip)
        if ip not in banned_ips:
          banned_ips.add(ip)
          print >>open('banned_ips','a'),self.connectip
          self.log("BANNED IP:",self.connectip)
      except: pass
    return Milter.REJECT

  # multiple messages can be received on a single connection
  # envfrom (MAIL FROM in the SMTP protocol) seems to mark the start
  # of each message.
  def envfrom(self,f,*str):
    self.log("mail from",f,str)
    #param = param2dict(str)
    #self.envid = param.get('ENVID',None)
    #self.mail_param = param
    self.fp = StringIO.StringIO()
    self.pristine_headers = StringIO.StringIO()
    if self.tempname:
      os.remove(self.tempname)  # remove any leftover from previous message
    self.tempname = None
    self.mailfrom = f
    self.forward = True
    self.bodysize = 0
    self.hidepath = False
    self.discard = False
    self.dspam = True
    self.whitelist = False
    self.blacklist = False
    self.greylist = False
    self.reject_spam = True
    self.data_allowed = True
    self.delayed_failure = None
    self.trust_received = self.trusted_relay
    self.trust_spf = self.trusted_relay or self.internal_connection
    self.external_spf = None
    self.redirect_list = []
    self.discard_list = []
    self.new_headers = []
    self.recipients = []
    self.confidence = None
    self.cbv_needed = None
    self.whitelist_sender = False
    self.postmaster_reply = False
    self.orig_from = None
    self.has_dkim = False
    self.dkim_domain = None
    if f == '<>' and internal_mta and self.internal_connection:
      if not iniplist(self.connectip,internal_mta):
        self.log("REJECT: pretend MTA at ",self.connectip,
            " sending MAIL FROM ",f)
        self.setreply('550','5.7.1',
        'Your PC is trying to send a DSN even though it is not an MTA.',
        'If you are running MS Outlook, it is broken.  If you want to',
        'send return receipts, use a more standards compliant email client.'
        )
        return Milter.REJECT
    if self.canon_from:
      self.reject = None	# reset delayed reject seen after mail from
    t = parse_addr(f)
    if len(t) == 2: t[1] = t[1].lower()
    self.canon_from = '@'.join(t)
    self.efrom = self.canon_from
    # Some braindead MTAs can't be relied upon to properly flag DSNs.
    # This heuristic tries to recognize such.
    self.is_bounce = (f == '<>' or t[0].lower() in banned_users
        #and t[1] == self.hello_name
    )

    # Check SMTP AUTH, also available:
    #   auth_authen  authenticated user
    #   auth_author  (ESMTP AUTH= param)
    #   auth_ssf     (connection security, 0 = unencrypted)
    #   auth_type    (authentication method, CRAM-MD5, DIGEST-MD5, PLAIN, etc)
    # cipher_bits  SSL encryption strength
    # cert_subject SSL cert subject
    # verify       SSL cert verified

    self.user = self.getsymval('{auth_authen}')
    if self.user:
      # Very simple SMTP AUTH policy by default:
      #   any successful authentication is considered INTERNAL
      # Detailed authorization policy is configured in the access file below.
      self.internal_connection = True
      self.log(
        "SMTP AUTH:",self.user, self.getsymval('{auth_type}'),
        "sslbits =",self.getsymval('{cipher_bits}'),
        "ssf =",self.getsymval('{auth_ssf}'), "INTERNAL"
      )
      if self.getsymval('{verify}'):
        self.log("SSL AUTH:",
          self.getsymval('{cert_subject}'),
          "verify =",self.getsymval('{verify}')
        )
      if self.reject:
	self.log("REJECT CANCELED")
	self.reject = None

    self.fp.write('From %s %s\n' % (self.canon_from,time.ctime()))
    self.internal_domain = False
    self.umis = None
    if len(t) == 2:
      user,domain = t
      for pat in internal_domains:
        if fnmatchcase(domain,pat):
          self.internal_domain = True
          break
      if srs and domain in srs_domain and user.lower().startswith('srs0'):
        try:
          newaddr = srs.reverse(self.canon_from)
          self.orig_from = newaddr
          self.efrom = newaddr
          self.log("Original MFROM:",newaddr)
        except:
          self.log("REJECT: bad MFROM signature",self.canon_from)
          self.setreply('550','5.7.1','Bad MFROM signature')
          return Milter.REJECT
      if self.internal_connection:
        if self.user:
          p = SPFPolicy('%s@%s'%(self.user,domain))
          policy = p.getPolicy('smtp-auth:')
          p.close()
        else:
          policy = None
          # trust ourself not to be a zombie
          if self.trusted_relay or self.connectip.strip() == '127.0.0.1':
            policy = 'OK'
        if policy:
          if policy != 'OK':
            self.log("REJECT: unauthorized user",self.user,
                "at",self.connectip,"sending MAIL FROM",self.canon_from)
            self.setreply('550','5.7.1',
              'SMTP user %s is not authorized to use MAIL FROM %s.' %
              (self.user,self.canon_from)
            )
            return Milter.REJECT
        elif internal_domains and not self.internal_domain:
          self.log("REJECT: zombie PC at ",self.connectip,
              " sending MAIL FROM ",self.canon_from)
          self.setreply('550','5.7.1',
          'Your PC is using an unauthorized MAIL FROM.',
          'It is either badly misconfigured or controlled by organized crime.'
          )
          return Milter.REJECT
      # effective from
      if self.orig_from:
        user,domain = self.orig_from.split('@')
      if isbanned(domain,banned_domains):
        self.log("REJECT: banned domain",domain)
	return self.delay_reject('550','5.7.1',template='bandom',domain=domain)
      if self.internal_connection:
        wl_users = whitelist_senders.get(domain,())
        if user in wl_users or '' in wl_users:
          self.whitelist_sender = True
          
      self.rejectvirus = domain in reject_virus_from
      if user in wiretap_users.get(domain,()):
        self.add_recipient(wiretap_dest)
        self.smart_alias(wiretap_dest)
      if user in discard_users.get(domain,()):
        self.discard = True
      exempt_users = dspam_whitelist.get(domain,())
      if user in exempt_users or '' in exempt_users:
        self.dspam = False
    else:
      self.rejectvirus = False
      domain = None
    if not self.hello_name:
      self.log("REJECT: missing HELO")
      self.setreply('550','5.7.1',"It's polite to say HELO first.")
      return Milter.REJECT
    self.spf = None
    self.policy = None
    if not (self.internal_connection or self.trusted_relay)     \
        and self.connectip and spf:
      rc = self.check_spf()
      if rc != Milter.CONTINUE:
        if rc != Milter.TEMPFAIL: self.offense()
        return rc
      self.greylist = True
    else:
      if spf and internal_policy and self.internal_connection:
        q = spf.query(self.connectip,self.canon_from,self.hello_name,
                receiver=self.receiver,strict=False)
        q.result = 'pass'
        p = SPFPolicy(q.s)
        if self.need_cbv(p.getPassPolicy(),q,'internal'):
          self.log('REJECT: internal mail from',q.s)
          self.setreply('550','5.7.1',
            "We don't accept internal mail from %s" %q.o,
            "Your email from %s comes from an internal IP, however"%q.o,
            "internal senders are not authorized to use %s."%q.o
          )
          return Milter.REJECT
      rc = Milter.CONTINUE
    res = self.spf and self.spf_guess
    hres = self.spf and self.spf_helo
    # Check whitelist and blacklist
    if auto_whitelist.has_key(self.efrom):
      self.greylist = False
      if res == 'pass' or self.trusted_relay:
        self.whitelist = True
        self.log("WHITELIST",self.efrom)
      else:
        self.dspam = False
        self.log("PROBATION",self.efrom)
      if res not in ('permerror','softfail'):
        self.cbv_needed = None
    elif cbv_cache.has_key(self.efrom) and cbv_cache[self.efrom] \
        or self.efrom in blacklist:
      # FIXME: don't use cbv_cache for blacklist if policy is 'OK'
      if not self.internal_connection:
        self.offense(inc=2)
        if not dspam_userdir:
          if domain in blacklist:
            self.log('REJECT: BLACKLIST',self.efrom)
            return self.delay_reject('550','5.7.1',
              'Sender email local blacklist')
          else:
            res = cbv_cache[self.efrom]
            desc = "CBV: %d %s" % res[:2]
            self.log('REJECT:',desc)
            return self.delay_reject('550','5.7.1',*desc.splitlines())
        self.greylist = False   # don't delay - use spam for training
        self.blacklist = True
        self.log("BLACKLIST",self.efrom)
    elif not self.reject:
      # REJECT delayed until after checking whitelist
      if self.policy in ('REJECT', 'BAN'):
          self.log('REJECT: no PTR, HELO or SPF')
          self.offense() # ban ip if too many bad MFROMs
          return self.delay_reject(template='anon',
                mfrom=self.efrom,helo=self.hello_name,ip=self.connectip)
      if domain and rc == Milter.CONTINUE \
	  and not (self.internal_connection or self.trusted_relay):
	rc = self.create_gossip(domain,res,hres)
    return rc

  def create_gossip(self,domain,res,hres):
    global gossip
    if gossip and gossip_node:
      if self.spf and self.spf.result == 'pass':
	qual = 'SPF'
      elif res == 'pass':
	qual = 'GUESS'
      elif hres == 'pass':
	qual = 'HELO'
	domain = self.spf.h
      else:   
	# No good identity: blame purported domain.  Qualify by SPF
	# result so NEUTRAL will get separate reputation from SOFTFAIL.
	qual = res
      try:
	umis = gossip.umis(domain+qual,self.id+time.time())
	res = gossip_node.query(umis,domain,qual,1)
	if res:
	  res,hdr,val = res
	  self.add_header(hdr,val)
	  a = val.split(',')
	  self.reputation = int(a[-2])
	  self.confidence = int(a[-1])
	  self.umis = umis
	  self.from_domain = domain
	  self.from_qual = qual
	  # We would like to reject on bad reputation here, but we
	  # need to give special consideration to postmaster.  So
	  # we have to wait until envrcpt().  Perhaps an especially
	  # bad reputation could be rejected here.
	  if self.reputation < -70 and self.confidence > 5:
	    self.log('REJECT: REPUTATION')
	    return self.delay_reject('550','5.7.1',template='illrepute',
                domain=domain,score=self.reputation,qual=qual)
	  if self.reputation > 40 and self.confidence > 0:
	    self.greylist = False
      except:
	gossip = None
	raise
    return Milter.CONTINUE

  def check_spf(self):
    receiver = self.receiver
    for tf in trusted_forwarder:
      q = spf.query(self.connectip,'',tf,receiver=receiver,strict=False)
      res,code,txt = q.check()
      if res == 'none':
        res,code,txt = q.best_guess('v=spf1 a mx')
      if res == 'pass':
        self.log("TRUSTED_FORWARDER:",tf)
        break
    else:
      q = spf.query(self.connectip,self.canon_from,self.hello_name,
          receiver=receiver,strict=False)
      q.set_default_explanation(
        'SPF fail: see http://openspf.net/why.html?sender=%s&ip=%s' % (q.s,q.c))
      res,code,txt = q.check()
    q.result = res
    if res in ('unknown','permerror') and q.perm_error and q.perm_error.ext:
      self.cbv_needed = (q,'permerror') # report SPF syntax error to sender
      res,code,txt = q.perm_error.ext   # extended (lax processing) result
      txt = 'EXT: ' + txt
    p = SPFPolicy(q.s)
    # FIXME: try:finally to close policy db, or reuse with lock
    if res in ('error','temperror'):
      if self.need_cbv(p.getTempErrorPolicy(),q,'temperror'):
        self.log('TEMPFAIL: SPF %s %i %s' % (res,code,txt))
        self.setreply(str(code),'4.3.0',txt,
          'We cannot accept your email until the DNS server for %s' % q.o,
          'is operational for TXT record queries.'
        )
        return Milter.TEMPFAIL
      res,code,txt = 'none',250,'EXT: ignoring DNS error'
    hres = None
    if res != 'pass':
      if self.mailfrom != '<>':
        # check hello name via spf unless spf pass
        h = spf.query(self.connectip,'',self.hello_name,receiver=receiver)
        hres,hcode,htxt = h.check()
        # FIXME: in a few cases, rejecting on HELO neutral causes problems
        # for senders forced to use their braindead ISPs email service.
        hp = SPFPolicy(self.hello_name)
        policy = hp.getPolicy('helo-%s:'%hres)
        if not policy:
          if hres in ('deny','fail','neutral','softfail'):
            # Even the most idiotic admin that uses non-existent domains
            # for helo is not going to forge 'gmail.com'.  So ban the IP too.
            if self.hello_name == 'gmail.com':
              policy = 'BAN'
            else:
              policy = 'REJECT'
          else:
            policy = 'OK'
        if self.need_cbv(policy,q,'heloerror'):
          self.log('REJECT: hello SPF: %s 550 %s' % (hres,htxt))
          return self.delay_reject('550','5.7.1',htxt,
            "The hostname given in your MTA's HELO response is not listed",
            "as a legitimate MTA in the SPF records for your domain.  If you",
            "get this bounce, the message was not in fact a forgery, and you",
            "should IMMEDIATELY notify your email administrator of the problem."
          )
        if hres == 'none' and spf_best_guess \
          and not dynip(self.hello_name,self.connectip):
          # HELO must match more exactly.  Don't match PTR or zombies
          # will be able to get a best_guess pass on their ISPs domain.
          hres,hcode,htxt = h.best_guess('v=spf1 a mx')
      else:
        hres,hcode,htxt = res,code,txt
      ores = res
      if self.internal_domain and res == 'none':
        # we don't accept our own domains externally without an SPF record
        self.log('REJECT: spam from self',q.o)
        return self.delay_reject('550','5.7.1',"I hate talking to myself!")
      if spf_best_guess and res == 'none':
        #self.log('SPF: no record published, guessing')
        q.set_default_explanation(
                'SPF guess: see http://openspf.net/why.html')
        # best_guess should not result in fail
        if self.missing_ptr:
          # ignore dynamic PTR for best guess
          res,code,txt = q.best_guess('v=spf1 a/24 mx/24')
        else:
          res,code,txt = q.best_guess()
        if res != 'pass' and hres == 'pass' and spf.domainmatch([q.h],q.o):
          res = 'pass'  # get a guessed pass for valid matching HELO 
      if self.missing_ptr and ores == 'none' and res != 'pass' \
                and hres != 'pass':
        # this bad boy has no credentials whatsoever
        res = 'none'
        policy = p.getNonePolicy()
        if policy in ('CBV','DSN'):
          self.offense(inc=0,min=2)    # ban ip if any bad recipient
        self.need_cbv(policy,q,'strike3')
        # REJECT delayed until after checking whitelist
    if res in ('deny', 'fail'):
      if self.need_cbv(p.getFailPolicy(),q,'fail'):
        self.log('REJECT: SPF %s %i %s' % (res,code,txt))
        # A proper SPF fail error message would read:
        # forger.biz [1.2.3.4] is not allowed to send mail with the domain
        # "forged.org" in the sender address.  Contact <postmaster@forged.org>.
        if q.d in hello_blacklist:
          self.offense(inc=4)
        return self.delay_reject(str(code),'5.7.1',txt)
    elif res == 'softfail':
      if self.need_cbv(p.getSoftfailPolicy(),q,'softfail'):
        self.log('REJECT: SPF %s %i %s' % (res,code,txt))
        return self.delay_reject('550','5.7.1',
          'SPF softfail: If you get this Delivery Status Notice, your email',
          'was probably legitimate.  Your administrator has published SPF',
          'records in a testing mode.  The SPF record reported your email as',
          'a forgery, which is a mistake if you are reading this.  Please',
          'notify your administrator of the problem immediately.'
        )
    elif res == 'neutral':
      if self.need_cbv(p.getNeutralPolicy(),q,'neutral'):
        self.log('REJECT: SPF neutral for',q.s)
        return self.delay_reject('550','5.7.1',
          'mail from %s must pass SPF: http://openspf.net/why.html' % q.o,
          'The %s domain is one that spammers love to forge.  Due to' % q.o,
          'the volume of forged mail, we can only accept mail that',
          'the SPF record for %s explicitly designates as legitimate.' % q.o,
          'Sending your email through the recommended outgoing SMTP',
          'servers for %s should accomplish this.' % q.o
        )
    elif res == 'pass':
      if self.need_cbv(p.getPassPolicy(),q,'pass'):
        self.log('REJECT: SPF pass for',q.s)
        self.setreply('550','5.7.1',
          "We don't accept mail from %s" %q.o,
          "Your email from %s comes from an authorized server, however"%q.o,
          "we still don't want it - we just don't like %s."%q.o
        )
        return Milter.REJECT
    elif res in ('unknown','permerror'):
      if self.need_cbv(p.getPermErrorPolicy(),q,'permerror'):
        self.log('REJECT: SPF %s %i %s' % (res,code,txt))
        # latest SPF draft recommends 5.5.2 instead of 5.7.1
        return self.delay_reject(str(code),'5.5.2',txt.replace('\0','^@'),
          'There is a fatal syntax error in the SPF record for %s' % q.o,
          'We cannot accept mail from %s until this is corrected.' % q.o
        )
    kv = {}
    if hres and q.h != q.o:
      kv['helo_spf'] = hres
    if res != q.result:
      kv['bestguess'] = res
    self.add_header('Received-SPF',q.get_header(q.result,receiver,**kv),0)
    self.spf_guess = res
    self.spf_helo = hres
    self.spf = q
    return Milter.CONTINUE

  # hide_path causes a copy of the message to be saved - until we
  # track header mods separately from body mods - so use only
  # in emergencies.
  def envrcpt(self,to,*str):
    try:
      param = param2dict(str)
      self.notify = param.get('NOTIFY','FAILURE,DELAY').upper().split(',')
      if 'NEVER' in self.notify: self.notify = ()
      # FIXME: self.notify needs to be by rcpt
      #self.rcpt_param = param
    except:
      self.log("REJECT: invalid PARAM:",to,str)
      self.setreply('550','5.7.1','Invalid RCPT PARAM')
      return Milter.REJECT
    # mail to MAILER-DAEMON is generally spam that bounced
    for daemon in ('MAILER-DAEMON','auto-notify'):
      if to.startswith('<%s@'%daemon):
        self.log('REJECT: RCPT TO:',to,str)
        self.setreply('550','5.7.1','%s does not accept mail'%daemon)
        return Milter.REJECT
    try:
      t = parse_addr(to)
      newaddr = False
      if len(t) == 2:
        t[1] = t[1].lower()
        user,domain = t
        if self.is_bounce and srs and domain in srs_domain:
          oldaddr = '@'.join(parse_addr(to))
          try:
            if ses:
              newaddr = ses.verify(oldaddr)
            else:
              newaddr = oldaddr,
            if len(newaddr) > 1:
              newaddr = newaddr[0]
              self.log("ses rcpt:",newaddr)
            else:
              newaddr = srs.reverse(oldaddr)
              # Currently, a sendmail map reverses SRS.  We just log it here.
              self.log("srs rcpt:",newaddr)
            self.dspam = False    # verified as reply to mail we sent
            self.blacklist = False
            self.greylist = False
            self.delayed_failure = False
          except:
            if not (self.internal_connection or self.trusted_relay):
              if srsre.match(oldaddr):
                self.log("REJECT: srs spoofed:",oldaddr)
                self.setreply('550','5.7.1','Invalid SRS signature')
                return Milter.REJECT
              if oldaddr.startswith('SES='):
                self.log("REJECT: ses spoofed:",oldaddr)
                self.setreply('550','5.7.1','Invalid SES signature')
                return Milter.REJECT
              # reject for certain recipients are delayed until after DATA
	      if auto_whitelist.has_precise_key(self.canon_from):
		self.log("WHITELIST: DSN from",self.canon_from)
	      else:
                #if srs_reject_spoofed \
                #  and user.lower() not in ('postmaster','abuse'):
                #  return self.forged_bounce(to)
                self.data_allowed = not srs_reject_spoofed

        if not self.internal_connection and domain in private_relay:
          self.log('REJECT: RELAY:',to)
          self.setreply('550','5.7.1','Unauthorized relay for %s' % domain)
          return Milter.REJECT

        # non DSN mail to SRS address will bounce due to invalid local part
        canon_to = '@'.join(t)
        if canon_to == 'postmaster@' + self.receiver:
          self.postmaster_reply = True

        self.recipients.append(canon_to)
        # FIXME: use newaddr to check rcpt
        users = check_user.get(domain)
        if self.discard:
          self.del_recipient(to)
        # don't check userlist if signed MFROM for now
        userl = user.lower()
        if users and not newaddr and not userl in users:
          self.log('REJECT: RCPT TO:',to,str)
          if gossip and self.umis:
            gossip_node.feedback(self.umis,1)
            self.umis = None
          return self.offense()
        # FIXME: should dspam_exempt be case insensitive?
        if user in block_forward.get(domain,()):
          self.forward = False
        exempt_users = dspam_exempt.get(domain,())
        if user in exempt_users or '' in exempt_users:
          if self.blacklist:
            self.log('REJECT: BLACKLISTED, rcpt to',to,str)
            self.setreply('550','5.7.1','Sending domain has been blacklisted')
            return Milter.REJECT
          self.dspam = False
        if userl != 'postmaster' and self.umis    \
          and self.reputation < -50 and self.confidence > 3:
          domain = self.from_domain
          self.log('REJECT: REPUTATION, rcpt to',to,str)
          self.setreply('550','5.7.1','%s has been sending mostly spam'%domain)
          return Milter.REJECT

        if domain in hide_path:
          self.hidepath = True
        if not domain in dspam_reject:
          self.reject_spam = False

    except:
      self.log("rcpt to",to,str)
      raise
    if self.greylist and greylist and self.canon_from and not self.reject:
      # no policy for trusted or internal
      rc = greylist.check(self.connectip,self.canon_from,canon_to)
      if rc == 0:
        self.log("GREYLIST:",self.connectip,self.canon_from,canon_to)
        self.setreply('451','4.7.1',
          'Greylisted: http://projects.puremagic.com/greylisting/',
          'Please retry in %.1f minutes'%(greylist.greylist_time/60.0))
        return Milter.TEMPFAIL
      self.log("GREYLISTED: %d"%rc)
      
    self.log("rcpt to",to,str)
    self.smart_alias(to)
    # get recipient after virtusertable aliasing
    #rcpt = self.getsymval("{rcpt_addr}")
    #self.log("rcpt-addr",rcpt);
    return Milter.CONTINUE

  # Heuristic checks for spam headers
  def check_header(self,name,val):
    lname = name.lower()
    # val is decoded header value
    if lname == 'subject':
      
      # check for common spam keywords
      for wrd in spam_words:
        if val.find(wrd) >= 0:
          self.log('REJECT: %s: %s' % (name,val))
          self.setreply('550','5.7.1','That subject is not allowed')
          return Milter.REJECT

      # even if we wanted the Taiwanese spam, we can't read Chinese
      if block_chinese:
        if not inCharSets(val,'iso-8859-1'):
          self.log('REJECT: %s: %s' % (name,val))
          self.setreply('550','5.7.1',"We don't understand that charset")
          return Milter.REJECT

      # check for spam that claims to be legal
      lval = val.lower().strip()
      for adv in ("adv:","adv.","adv ",
        "<adv>","<ad>","[adv]","(adv)","advt:","advert:","[spam]"):
        if lval.startswith(adv):
          self.log('REJECT: %s: %s' % (name,val))
          self.setreply('550','5.7.1','No soliciting allowed')
          return Milter.REJECT
      for adv in ("adv","(adv)","[adv]","(non-spam)"):
        if lval.endswith(adv):
          self.log('REJECT: %s: %s' % (name,val))
          self.setreply('550','5.7.1','No soliciting allowed')
          return Milter.REJECT

      # check for porn keywords
      for w in porn_words:
        if lval.find(w) >= 0:
          self.log('REJECT: %s: %s' % (name,val))
          self.setreply('550','5.7.1','That subject is not allowed')
          return Milter.REJECT

      # check for annoying forwarders
      if not self.forward:
        if lval.startswith("fwd:") or lval.startswith("[fw"):
          self.log('REJECT: %s: %s' % (name,val))
          self.setreply('550','5.7.1','I find unedited forwards annoying')
          return Milter.REJECT

      # check for delayed bounce of CBV
      if self.postmaster_reply and srs:
        if refaildsn.search(lval):
          self.delayed_failure = val.strip()
          # if confirmed by finding our signed Message-ID, 
          # original sender (encoded in Message-ID) is blacklisted

    elif lname == 'from' and self.dspam:
      fname,email = parseaddr(val)
      for w in spam_words:
      	if fname.find(w) >= 0:
          self.log('REJECT: %s: %s' % (name,val))
          self.setreply('550','5.7.1','No soliciting')
          return self.bandomain()
      for w in from_words:
      	if fname.find(w) >= 0:
          self.log('REJECT: %s: %s' % (name,val))
          self.setreply('550','5.7.1','No soliciting')
          return self.bandomain()
      # check for porn keywords
      lval = fname.lower().strip()
      for w in porn_words:
        if lval.find(w) >= 0:
          self.log('REJECT: %s: %s' % (name,val))
          self.setreply('550','5.7.1','Watch your language')
          return self.bandomain()
      if email.lower().startswith('postmaster@'):
        # Yes, if From header comes last, this might not help much.
        # But this is a heuristic - if MTAs would send proper DSNs in
        # the first place, none of this would be needed.
        self.is_bounce = True
      
    # check for invalid message id
    elif lname == 'message-id' and len(val) < 4:
      self.log('REJECT: %s: %s' % (name,val))
      return Milter.REJECT

    # check for common bulk mailers
    elif lname == 'x-mailer':
      mailer = val.lower()
      if mailer in ('direct email','calypso','mail bomber') \
        or mailer.find('optin') >= 0:
        self.log('REJECT: %s: %s' % (name,val))
        return Milter.REJECT
    return Milter.CONTINUE

  def forged_bounce(self,rcpt='-'):
    if self.mailfrom != '<>':
      self.log("REJECT: bogus DSN",rcpt)
      self.setreply('550','5.7.1',
        "I do not accept normal mail from %s." % self.mailfrom.split('@')[0],
        "All such mail has turned out to be Delivery Status Notifications",
        "which failed to be marked as such.  Please send a real DSN if",
        "you need to.  Use another MAIL FROM if you need to send me mail."
      )
    else:
      self.log('REJECT: bounce with no SRS encoding',rcpt)
      self.setreply('550','5.7.1',
        "I did not send you that message. Please consider implementing SPF",
        "(http://openspf.net) to avoid bouncing mail to spoofed senders.",
        "Thank you."
      )
    return Milter.REJECT

  def bandomain(self,wild=0):
    if self.spf and self.spf_guess == 'pass' and self.confidence == 0:
      domain = self.spf.o
      if not isbanned(domain,banned_domains):
	m = RE_MULTIMX.match(domain)
	if m:
	  orig = domain
	  domain = '*.' + domain[m.end():]
	  self.log('BAN DOMAIN:',orig,'->',domain)
	else:
	  if wild:
	    a = domain.split('.')[wild:]
	    if len(a) > 1: domain = '*.'+'.'.join(a)
	  self.log('BAN DOMAIN:',domain)
	try:
	  fp = open('banned_domains','at')
	  print >>fp,domain 
	finally: fp.close()
	banned_domains.add(domain)
    return Milter.REJECT

  def data(self):
    if self.reject:
      self.log("DELAYED REJECT")
      args,kw = self.reject
      self.htmlreply(*args,**kw)
      return Milter.REJECT
    if not self.data_allowed:
      return self.forged_bounce()
    return Milter.CONTINUE
    
  def header(self,name,hval):
    if self.data() == Milter.REJECT:
      return Milter.REJECT
    lname = name.lower()
    # decode near ascii text to unobfuscate
    val = parse_header(hval)
    if not self.internal_connection and not (self.blacklist or self.whitelist):
      rc = self.check_header(name,val)
      if rc != Milter.CONTINUE:
        if gossip and self.umis:
          gossip_node.feedback(self.umis,1)
        return rc
    elif self.whitelist_sender:
      # check for AutoReplys
      if (lname == 'subject' and reautoreply.match(val)) \
	or (lname == 'user-agent' and val.lower().startswith('vacation')):
          self.whitelist_sender = False
          self.log('AUTOREPLY: not whitelisted')

    # log selected headers
    if log_headers or lname in ('subject','x-mailer'):
      self.log('%s: %s' % (name,val))
    elif self.trust_received and lname == 'received':
      self.trust_received = False
      self.trust_spf = False
      self.log('%s: %s' % (name,val.splitlines()[0]))
    elif self.trust_spf and lname == 'received-spf':
      self.trust_spf = False
      self.external_spf = val
      self.log('%s: %s' % (name,val.splitlines()[0]))
    elif dkim and lname == 'dkim-signature':
      self.has_dkim = True
      self.log('%s: %s' % (name,val.splitlines()[0]))
    # FIXME: keep both decoded and pristine headers.  DKIM needs
    # pristine headers.
    if self.fp:
      try:
        val = val.encode('iso-8859-1')
      except:
        val = hval
      self.fp.write("%s: %s\n" % (name,val))    # add decoded header to buffer
      self.pristine_headers.write("%s: %s\n" % (name,hval))
    return Milter.CONTINUE

  def eoh(self):
    if not self.fp: return Milter.TEMPFAIL      # not seen by envfrom
    if self.data() == Milter.REJECT:
      return Milter.REJECT
    for name,val,idx in self.new_headers:
      self.fp.write("%s: %s\n" % (name,val))    # add new headers to buffer
    self.fp.write("\n")                         # terminate headers
    if not self.internal_connection:
      msg = None        # parse headers only if needed
      if not self.delayed_failure:
        self.fp.seek(0)
        msg = email.message_from_file(self.fp)
        if msg.get_param('report-type','').lower() == 'delivery-status':
          self.is_bounce = True
          self.delayed_failure = msg.get('subject','DSN')
      # log when neither sender nor from domains matches mail from domain
      if supply_sender and self.mailfrom != '<>':
        if not msg:
          self.fp.seek(0)
          msg = email.message_from_file(self.fp)
        mf_domain = self.canon_from.split('@')[-1]
        for rn,hf in getaddresses(msg.get_all('from',[])
                + msg.get_all('sender',[])):
          t = parse_addr(hf)
          if len(t) == 2:
            hd = t[1].lower()
            if hd == mf_domain or mf_domain.endswith('.'+hd): break
        else:
          for f in msg.get_all('from',[]):
            self.log('From:',f)
          sender = msg.get_all('sender')
          if sender:
            for f in sender:
              self.log('Sender:',f)
          else:
            self.log("NOTE: Supplying MFROM as Sender");
            self.add_header('Sender',self.mailfrom)
      del msg
    # copy headers to a temp file for scanning the body
    self.fp.seek(0)
    headers = self.fp.getvalue()
    self.fp.close()
    fd,fname = tempfile.mkstemp(".defang")
    self.tempname = fname
    self.fp = os.fdopen(fd,"w+b")
    self.fp.write(headers)      # IOError (e.g. disk full) causes TEMPFAIL
    self.body_start = self.fp.tell()
    # check if headers are really spammy
    if dspam_dict and not self.internal_connection:
      ds = dspam.dspam(dspam_dict,dspam.DSM_PROCESS,
        dspam.DSF_CHAINED|dspam.DSF_CLASSIFY)
      try:
        ds.process(headers)
        if ds.probability > 0.93 and self.dspam and not self.whitelist:
          self.log('REJECT: X-DSpam-HeaderScore: %f' % ds.probability)
          self.setreply('550','5.7.1','Your Message looks spammy')
          return Milter.REJECT
        self.add_header('X-DSpam-HeaderScore','%f'%ds.probability)
      finally:
        ds.destroy()
    self.ioerr = None
    return Milter.CONTINUE

  @Milter.noreply
  def body(self,chunk):         # copy body to temp file
    try:
      if self.fp:
        self.fp.write(chunk)      # IOError causes TEMPFAIL in milter
        self.bodysize += len(chunk)
    except Exception,x:
      if not self.ioerr:
        self.ioerr = x
	self.log(x)
      self.fp = None
    return Milter.CONTINUE

  def _headerChange(self,msg,name,value):
    if value:   # add header
      self.addheader(name,value)
    else:       # delete all headers with name
      h = msg.getheaders(name)
      if h:
        for i in range(len(h),0,-1):
          self.chgheader(name,i-1,'')

  def _chk_ext(self,name):
    "Check a name for dangerous Winblows extensions."
    if not name: return name
    lname = name.lower()
    for ext in self.bad_extensions:
      if lname.endswith(ext): return name
    return None

    
  def _chk_attach(self,msg):
    "Filter attachments by content."
    # check for bad extensions
    mime.check_name(msg,self.tempname,ckname=self._chk_ext,scan_zip=scan_zip)
    # remove scripts from HTML
    if scan_html:
      mime.check_html(msg,self.tempname)        
    # don't let a tricky virus slip one past us
    if scan_rfc822:
      msg = msg.get_submsg()
      if isinstance(msg,email.Message.Message):
        return mime.check_attachments(msg,self._chk_attach)
    return Milter.CONTINUE

  def alter_recipients(self,discard_list,redirect_list):
    for rcpt in discard_list:
      if rcpt in redirect_list: continue
      self.log("DISCARD RCPT: %s" % rcpt)       # log discarded rcpt
      self.delrcpt(rcpt)
    for rcpt in redirect_list:
      if rcpt in discard_list: continue
      self.log("APPEND RCPT: %s" % rcpt)        # log appended rcpt
      self.addrcpt(rcpt)
      if not blind_wiretap:
        self.addheader('Cc',rcpt)

  # 
  def gossip_header(self):
    "Set UMIS from GOSSiP header."
    msg = email.message_from_file(self.fp)
    gh = msg.get_all('x-gossip')
    if gh:
      self.log('X-GOSSiP:',gh[0])
      self.umis,_ = gh[0].split(',',1)
    elif self.spf:
      domain = self.spf.o
      if domain:
	self.create_gossip(domain,self.spf_guess,self.spf_helo)

  def check_dkim(self):
    if self.has_dkim:
      self.fp.seek(self.body_start)
      txt = self.pristine_headers.getvalue()+'\n'+self.fp.read()
      res = False
      try:
        d = dkim.DKIM(txt,logger=milter_log)
	res = d.verify()
      except dkim.DKIMException as x:
	self.log('DKIM: %s'%x)
      except Exception as x:
	milter_log.error("check_dkim: %s",x,exc_info=True)
      if res:
	self.log('DKIM: Pass (%s)'%d.domain)
        self.dkim_domain = d.domain
      else:
	fd,fname = tempfile.mkstemp(".dkim")
	with os.fdopen(fd,"w+b") as fp:
	  fp.write(txt)
	self.log('DKIM: Fail (saved as %s)'%fname)
      return res

  # check spaminess for recipients in dictionary groups
  # if there are multiple users getting dspammed, then
  # a signature tag for each is added to the message.

  # FIXME: quarantine messages rejected via fixed patterns above
  #        this will give a fast start to stats

  def check_spam(self):
    "return True/False if self.fp, else return Milter.REJECT/TEMPFAIL/etc"
    self.screened = False
    if not dspam_userdir: return False
    ds = Dspam.DSpamDirectory(dspam_userdir)
    ds.log = self.log
    ds.headerchange = self._headerChange
    modified = False
    for rcpt in self.recipients:
      if dspam_users.has_key(rcpt.lower()):
        user = dspam_users.get(rcpt.lower())
        if user:
          try:
            self.fp.seek(0)
            txt = self.fp.read()
            if user in ('bandom','spam','falsepositive') \
                and self.internal_connection:
              if spf and self.external_spf:
                q = spf.query('','','')
                p = q.parse_header(self.external_spf)
		self.spf_guess = p.get('bestguess',q.result)
		self.spf_helo = p.get('helo',None)
		self.log("External SPF:",self.spf_guess)
		self.spf = q
              else:
                self.spf = None
            if user == 'bandom' and self.internal_connection:
	      if self.spf:
                if self.spf_guess == 'pass' or q.result == 'none':
		  self.confidence = 0	# ban regardless of reputation status
		  s = rcpt.split('@')[0][-1]
                  self.bandomain(wild=s.isdigit() and int(s))
              user = 'spam'
            if user == 'spam' and self.internal_connection:
              sender = dspam_users.get(self.efrom)
              if sender:
                self.log("SPAM: %s" % sender)   # log user for SPAM
                self.fp.seek(0)
                self.gossip_header()
                self.fp = None
                ds.add_spam(sender,txt)
                txt = None
                return Milter.DISCARD
            elif user == 'falsepositive' and self.internal_connection:
              sender = dspam_users.get(self.efrom)
              if sender:
                self.log("FP: %s" % sender)     # log user for FP
                txt = ds.false_positive(sender,txt)
                self.fp = StringIO.StringIO(txt)
                self.gossip_header()
                self.delrcpt('<%s>' % rcpt)
                self.recipients = None
                self.rejectvirus = False
                return True
            elif not self.internal_connection or dspam_internal:
              if len(txt) > dspam_sizelimit:
                self.log("Large message:",len(txt))
                if self.blacklist:
                  self.log('REJECT: BLACKLISTED')
                  self.setreply('550','5.7.1',
                        '%s has been blacklisted.'%self.efrom)
                  self.fp = None
                  return Milter.REJECT
                return False
              if user == 'honeypot' and Dspam.VERSION >= '1.1.9':
                keep = False    # keep honeypot mail
                self.fp = None
                if len(self.recipients) > 1:
                  self.log("HONEYPOT:",rcpt,'SCREENED')
                  if self.whitelist:
                    # don't train when recipients includes honeypot
                    return False
                  if self.spf and self.mailfrom != '<>':
                    # check that sender accepts quarantine DSN
                    if self.spf_guess == 'pass':
                      msg = mime.message_from_file(StringIO.StringIO(txt))
                      rc = self.send_dsn(self.spf,msg,'quarantine',fail=True)
                      del msg
                    else:
                      rc = self.send_dsn(self.spf)
                    if rc != Milter.CONTINUE:
                      return rc 
                  ds.check_spam(user,txt,self.recipients,quarantine=True,
                        force_result=dspam.DSR_ISSPAM)
                else:
                  ds.check_spam(user,txt,self.recipients,quarantine=keep,
                        force_result=dspam.DSR_ISSPAM)
                  self.log("HONEYPOT:",rcpt)
                return Milter.DISCARD
              if self.whitelist:
                # Sender whitelisted: tag, but force as ham.  
                # User can change if actually spam.
                txt = ds.check_spam(user,txt,self.recipients,
                        force_result=dspam.DSR_ISINNOCENT)
              elif self.blacklist:
                txt = ds.check_spam(user,txt,self.recipients,
                        force_result=dspam.DSR_ISSPAM)
              elif user in dspam_train:
                txt = ds.check_spam(user,txt,self.recipients)
              else:
                txt = ds.check_spam(user,txt,self.recipients,classify=True)
                if txt:
                  self.add_header("X-DSpam-Score",'%f' % ds.probability)
                  return False
              if not txt:
                # DISCARD if quarrantined for any recipient.  It
                # will be resent to all recipients if they submit
                # as a false positive.
                self.log("DSPAM:",user,rcpt)
                self.fp = None
                return Milter.DISCARD
              self.fp = StringIO.StringIO(txt)
              modified = True
          except Exception,x:
            self.log("check_spam:",x)
            milter_log.error("check_spam: %s",x,exc_info=True)
    # screen if no recipients are dspam_users
    if not modified and dspam_screener and not self.internal_connection \
        and self.dspam:
      self.fp.seek(0)
      txt = self.fp.read()
      if len(txt) > dspam_sizelimit:
        self.log("Large message:",len(txt))
        return False
      screener = dspam_screener[self.id % len(dspam_screener)]
      if not ds.check_spam(screener,txt,self.recipients,
        classify=True,quarantine=False):
        if self.whitelist:
          # messages is whitelisted but looked like spam, Train on Error
          self.log("TRAIN:",screener,'X-Dspam-Score: %f' % ds.probability)
          # user can't correct anyway if really spam, so discard tag
          ds.check_spam(screener,txt,self.recipients,
                  force_result=dspam.DSR_ISINNOCENT)
          return False
        if self.reject_spam and self.spf.result != 'pass':
          self.log("DSPAM:",screener,
                'REJECT: X-DSpam-Score: %f' % ds.probability)
          self.setreply('550','5.7.1','Your Message looks spammy')
          self.fp = None
          return Milter.REJECT
        self.log("DSPAM:",screener,"SCREENED %f" % ds.probability)
        if self.spf and self.mailfrom != '<>':
          # check that sender accepts quarantine DSN
          self.fp.seek(0)
	  if self.spf_guess == 'pass' or self.cbv_needed:
	    msg = mime.message_from_file(self.fp)
	    if self.spf_guess == 'pass':
	      rc = self.send_dsn(self.spf,msg,'quarantine',fail=True)
	    else:
	      rc = self.do_needed_cbv(msg)
	    del msg
	  else:
	    rc = self.send_dsn(self.spf)
          if rc != Milter.CONTINUE:
            self.fp = None
            return rc
        if not ds.check_spam(screener,txt,self.recipients,classify=True):
          self.fp = None
          return Milter.DISCARD
        # Message no longer looks spammy, deliver normally. We lied in the DSN.
      elif self.blacklist:
        # message is blacklisted but looked like ham, Train on Error
        self.log("TRAINSPAM:",screener,'X-Dspam-Score: %f' % ds.probability)
        ds.check_spam(screener,txt,self.recipients,quarantine=False,
                force_result=dspam.DSR_ISSPAM)
        self.fp = None
        self.setreply('550','5.7.1', 'Sender email local blacklist')
        return Milter.REJECT
      elif self.whitelist and ds.totals[1] < 1000:
        self.log("TRAIN:",screener,'X-Dspam-Score: %f' % ds.probability)
        # user can't correct anyway if really spam, so discard tag
        ds.check_spam(screener,txt,self.recipients,
                force_result=dspam.DSR_ISINNOCENT)
        return False
      # log spam score for screened messages
      self.add_header("X-DSpam-Score",'%f' % ds.probability)
      self.screened = True
    return modified

  # train late in eom(), after failed CBV
  # FIXME: need to undo if registered as ham with a dspam_user
  def train_spam(self):
    "Train screener with current message as spam"
    if not dspam_userdir: return
    if not dspam_screener: return
    ds = Dspam.DSpamDirectory(dspam_userdir)
    ds.log = self.log
    self.fp.seek(0)
    txt = self.fp.read()
    if len(txt) > dspam_sizelimit:
      self.log("Large message:",len(txt))
      return
    screener = dspam_screener[self.id % len(dspam_screener)]
    # since message will be rejected, we do not quarantine
    ds.check_spam(screener,txt,self.recipients,force_result=dspam.DSR_ISSPAM,
        quarantine=False)
    self.log("TRAINSPAM:",screener,'X-Dspam-Score: %f' % ds.probability)

  def do_needed_cbv(self,msg):
    q,template_name = self.cbv_needed
    rc = self.send_dsn(q,msg,template_name)
    self.cbv_needed = None
    return rc

  def need_cbv(self,policy,q,tname):
    self.policy = policy
    if policy == 'CBV':
      if self.mailfrom != '<>' and not self.cbv_needed:
        self.cbv_needed = (q,None)
    elif policy == 'DSN':
      if self.mailfrom != '<>' and not self.cbv_needed:
        self.cbv_needed = (q,tname)
    elif policy == 'WHITELIST':
        self.whitelist = True
    elif policy != 'OK':
      if policy == 'BAN':
	self.offense(inc=3)
      elif self.offenses:
        self.offense()	 # multiple forged domains are extra evil
      return True
    return False

  def whitelist_rcpts(self):
    whitelisted = []
    for canon_to in self.recipients:
      user,domain = canon_to.split('@')
      if internal_domains:
        for pat in internal_domains:
          if fnmatchcase(domain,pat): break
        else:
          auto_whitelist[canon_to] = None
          whitelisted.append(canon_to)
          self.log('Auto-Whitelist:',canon_to)
      else:
        auto_whitelist[canon_to] = None
        whitelisted.append(canon_to)
        self.log('Auto-Whitelist:',canon_to)
    return whitelisted

  def eom(self):
    if self.ioerr:
      fname = tempfile.mktemp(".ioerr")  # save message that caused crash
      os.rename(self.tempname,fname)
      self.tempname = None
      return Milter.TEMPFAIL
    if not self.fp:
      return Milter.ACCEPT      # no message collected - so no eom processing

    if self.is_bounce and len(self.recipients) > 1:
      self.log("REJECT: DSN to multiple recipients")
      self.setreply('550','5.7.1', 'DSN to multiple recipients')
      return Milter.REJECT

    try:
      # check for delayed bounce
      if self.delayed_failure:
        self.fp.seek(0)
        sender = findsrs(self.fp)
        if sender:
          cbv_cache[sender] = 550,self.delayed_failure
          # make blacklisting persistent, since delayed DSNs are expensive
          blacklist[sender] = None
          try:
            # save message for debugging
            fname = tempfile.mktemp(".dsn")
            os.rename(self.tempname,fname)
          except:
            fname = self.tempname
          self.tempname = None
          self.log('BLACKLIST:',sender,fname)
          return Milter.DISCARD
      
      self.check_dkim()

      # analyze external mail for spam
      spam_checked = self.check_spam()  # tag or quarantine for spam
      if not self.fp:
        if gossip and self.umis:
          gossip_node.feedback(self.umis,1)
        return spam_checked

      # analyze all mail for dangerous attachments and scripts
      self.fp.seek(0)
      msg = mime.message_from_file(self.fp)
      # pass header changes in top level message to sendmail
      msg.headerchange = self._headerChange

      # filter leaf attachments through _chk_attach
      assert not msg.ismodified()
      self.bad_extensions = ['.' + x for x in banned_exts]
      rc = mime.check_attachments(msg,self._chk_attach)
    except:     # milter crashed trying to analyze mail
      exc_type,exc_value = sys.exc_info()[0:2]
      if dspam_userdir and exc_type == dspam.error:
        if not exc_value.strerror:
          exc_value.strerror = exc_value.args[0]
        if exc_value.strerror == 'Lock failed':
          milter_log.warn("LOCK: BUSY") # log filename
          self.setreply('450','4.2.0',
                'Too busy discarding spam.  Please try again later.')
          return Milter.TEMPFAIL
      fname = tempfile.mktemp(".fail")  # save message that caused crash
      os.rename(self.tempname,fname)
      self.tempname = None
      if exc_type == email.Errors.BoundaryError:
        milter_log.warn("MALFORMED: %s",fname)  # log filename
        if self.internal_connection:
          # accept anyway for now
          return Milter.ACCEPT
        self.setreply('554','5.7.7',
                'Boundary error in your message, are you a spammer?')
        return Milter.REJECT
      if exc_type == email.Errors.HeaderParseError:
        milter_log.warn("MALFORMED: %s",fname)  # log filename
        self.setreply('554','5.7.7',
                'Header parse error in your message, are you a spammer?')
        return Milter.REJECT
      milter_log.error("FAIL: %s",fname)        # log filename
      # let default exception handler print traceback and return 451 code
      raise
    if rc == Milter.REJECT: return rc
    if rc == Milter.DISCARD: return rc

    if rc == Milter.CONTINUE: rc = Milter.ACCEPT # for testbms.py compat

    defanged = msg.ismodified()

    if self.hidepath: del msg['Received']

    if self.recipients == None:
      # false positive being recirculated
      self.recipients = msg.get_all('x-dspam-recipients',[])
      if self.recipients:
        for rcptlist in self.recipients:
          for rcpt in rcptlist.split(','):
            self.addrcpt('<%s>' % rcpt.strip())
        del msg['x-dspam-recipients']
      else:
        self.addrcpt(self.mailfrom)
    else:
      self.alter_recipients(self.discard_list,self.redirect_list)
      # auto whitelist original recipients
      if not defanged and self.whitelist_sender:
        whitelisted = self.whitelist_rcpts()
        if whitelisted:
          for mx in whitelist_mx:
            try:
              self.send_rcpt(mx,whitelisted)
              self.log('Tell MX:',mx)
            except Exception,x:
              self.log('Tell MX:',mx,x)

    for name,val,idx in self.new_headers:
      try:
        try:
          self.addheader(name,val,idx)
        except TypeError:
          val = val.replace('\x00',r'\x00')
          self.addheader(name,val,idx)
      except Milter.error:
        self.addheader(name,val)        # older sendmail can't insheader

    # Do not send CBV to internal domains (since we'll just get
    # the "Fraudulent MX" error).  Whitelisted senders clearly do not
    # need CBV.  However, whitelisted domains might (to discover 
    # bogus localparts).  Need a way to tell the difference.
    if self.cbv_needed and not self.internal_domain:
      rc = self.do_needed_cbv(msg)
      if rc == Milter.REJECT:
        # Do not feedback here, because feedback should only occur
        # for messages that have gone to DATA.  Reputation lets us
        # reject before DATA for persistent spam domains, saving
        # cycles and bandwidth.

        # Do feedback here, because CBV costs quite a bit more than
        # simply rejecting before DATA.  Bad reputation will acrue to
        # the IP or HELO, since we won't get here for validated MAILFROM.
        #       See Proverbs 26:4,5
        if gossip and self.umis:
          gossip_node.feedback(self.umis,1)
        self.train_spam()
        return Milter.REJECT
      if rc != Milter.CONTINUE:
        return rc

    if mail_archive:
      global _archive_lock
      if not _archive_lock:
        import thread
        _archive_lock = thread.allocate_lock()
      _archive_lock.acquire()
      try:
        fin = open(self.tempname,'r')
        fout = open(mail_archive,'a')
        shutil.copyfileobj(fin,fout,8192)
      finally:
        _archive_lock.release()
        fin.close()
        fout.close()
      
    if not defanged and not spam_checked:
      if gossip and self.umis and self.screened:
        gossip_node.feedback(self.umis,0)
      os.remove(self.tempname)
      self.tempname = None      # prevent re-removal
      self.log("eom")
      return rc                 # no modified attachments

    # Body modified, copy modified message to a temp file 
    if defanged:
      if self.rejectvirus and not self.hidepath:
        self.log("REJECT virus from",self.mailfrom)
        self.setreply('550','5.7.1','Attachment type not allowed.',
                'You attempted to send an attachment with a banned extension.')
        self.tempname = None
        return Milter.REJECT
      self.log("Temp file:",self.tempname)
      self.tempname = None      # prevent removal of original message copy
    out = tempfile.TemporaryFile()
    try:
      msg.dump(out)
      out.seek(0)
      # Since we wrote headers with '\n' (no CR),
      # the following header/body split should always work.
      msg = out.read().split('\n\n',1)[-1]
      self.replacebody(msg)     # feed modified message to sendmail
      if spam_checked: 
        if gossip and self.umis:
          gossip_node.feedback(self.umis,0)
        self.log("dspam")
      return rc
    finally:
      out.close()
    return Milter.TEMPFAIL

  ## Send recipients to primary MX for auto whitelisting
  def send_rcpt(self,mx,rcpts,timeout=30):
    if not srs: return  # requires SRS for authentication
    sender = srs.forward(self.canon_from,self.receiver)
    smtp = smtplib.SMTP()
    toolate = time.time() + timeout
    smtp.connect(mx)
    code,resp = smtp.helo(self.receiver)
    if not (200 <= code <= 299):
      raise smtplib.SMTPHeloError(code, resp)
    code,resp = smtp.docmd('MAIL FROM: <%s>'%sender)
    if code != 250:
      raise smtplib.SMTPSenderRefused(code, resp, '<%s>'%sender)
    badrcpts = {}
    for rcpt in rcpts:
      code,resp = smtp.rcpt(rcpt)
      if code not in (250,251):
        badrcpts[rcpt] = (code,resp)# permanent error
    smtp.quit()
    if badrcpts: return badrcpts
    return None

  def htmlreply(self,code='550',xcode='5.7.1',*msg,**kw):
    if 'template' in kw:
      template = kw['template']
      del kw['template']
      desc = "%s/%s?%s" % (errors_url,template,urllib.urlencode(kw))
      self.setreply(code,xcode,desc.replace('%','%%'),*msg)
    else:
      try:
        self.setreply(code,xcode,*msg)
      except ValueError,x:
        self.log(x)

  def send_dsn(self,q,msg=None,template_name=None,fail=False):
    if fail:
      if not self.notify: template_name = None
    else:
      if 'DELAY' not in self.notify: template_name = None
    if template_name and template_name.startswith('helo'):
      sender = 'postmaster@'+q.h
    else:
      sender = q.s
    cached = cbv_cache.has_key(sender)
    if cached:
      self.log('CBV:',sender,'(cached)')
      res = cbv_cache[sender]
    else:
      m = None
      if template_name:
        fname = template_name+'.txt'
        try:
          template = file(template_name+'.txt').read()
          m = dsn.create_msg(q,self.recipients,msg,template)
          self.log('CBV:',sender,'Using:',fname)
        except IOError: pass
      if not m:
        self.log('CBV:',sender,'PLAIN (%s)'%q.result)
      else:
        if srs:
          # Add SRS coded sender to various headers.  When (incorrectly)
          # replying to our DSN, any of these which are preserved
          # allow us to track the source.
          msgid = srs.forward(sender,self.receiver)
          m.add_header('Message-Id','<%s>'%msgid)
          if 'x-mailer' in m:
            m.replace_header('x-mailer','"%s" <%s>' % (m['x-mailer'],msgid))
          else:
            m.add_header('X-Mailer','"Python Milter" <%s>'%msgid)
          m.add_header('Sender','"Python Milter" <%s>'%msgid)
        m = m.as_string()
        print >>open(template_name+'.last_dsn','w'),m
      # if missing template, do plain CBV
      res = dsn.send_dsn(sender,self.receiver,m,timeout=timeout)
    if res:
      desc = "CBV: %d %s" % res[:2]
      if 400 <= res[0] < 500:
        self.log('TEMPFAIL:',desc)
        self.setreply('450','4.2.0',*desc.splitlines())
        return Milter.TEMPFAIL
      cbv_cache[sender] = res
      self.log('REJECT:',desc)
      try:
        self.htmlreply(mfrom=sender,msg=res[1],template='dsnrefused')
      except TypeError:
        self.setreply('550','5.7.1',"Callback failure")
      return Milter.REJECT
    cbv_cache[sender] = res
    return Milter.CONTINUE

  def close(self):
    if self.tempname:
      os.remove(self.tempname)  # remove in case session aborted
    if self.fp:
      self.fp.close()
    
    return Milter.CONTINUE

  def abort(self):
    if self.whitelist_sender and self.recipients and self.trusted_relay:
      self.whitelist_rcpts()
    else:
      self.log("abort after %d body chars" % self.bodysize)
    return Milter.CONTINUE

def main():
  if access_file:
    try:
      acf = anydbm.open(access_file,'r')
      acf.close()
    except:
      milter_log.error('Unable to read: %s',access_file)
      return
  try:
    global banned_ips
    banned_ips = set(addr2bin(ip) 
        for fn in glob('banned_ips*')
        for ip in open(fn))
    print len(banned_ips),'banned ips'
  except:
    milter_log.exception('Error reading banned_ips')

  try:
    global banned_domains
    banned_domains = set(dom.strip()
	    for fn in glob('banned_domains*')
	    for dom in open(fn))
    print len(banned_domains),'banned domains'
  except:
    milter_log.exception('Error reading banned_domains')

  Milter.factory = bmsMilter
  flags = Milter.CHGBODY + Milter.CHGHDRS + Milter.ADDHDRS
  if wiretap_dest or smart_alias or dspam_userdir:
    flags = flags + Milter.ADDRCPT
  if srs or len(discard_users) > 0 or smart_alias or dspam_userdir:
    flags = flags + Milter.DELRCPT
  Milter.set_flags(flags)
  socket.setdefaulttimeout(60)
  milter_log.info("bms milter startup")
  Milter.runmilter("pythonfilter",socketname,timeout)
  milter_log.info("bms milter shutdown")

if __name__ == "__main__":
  read_config(["/etc/mail/pymilter.cfg","milter.cfg"])

  cbv_cache.load('send_dsn.log',age=30)
  auto_whitelist.load('auto_whitelist.log',age=120)
  blacklist.load('blacklist.log',age=60)
      
  if dspam_dict:
    import dspam        # low level spam check
  if dspam_userdir:
    import dspam
    import Dspam        # high level spam check
    try:
      dspam_version = Dspam.VERSION
    except:
      dspam_version = '1.1.4'
    assert dspam_version >= '1.1.5'
  main()
