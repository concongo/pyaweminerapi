from pyaweminerapi import pyaweminapi

t = pyaweminapi('http://vd-server.ddns.net:17790')
miners = t.getMinersBriefing()

print miners