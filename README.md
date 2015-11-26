# logstash-forwarder-panopta-plugin
Just drop this into your Panopta plugin directory:
Linux/AIX/Solaris - /usr/lib/panopta-agent/plugins/
FreeBSD - /usr/local/panopta-agent/lib/plugins/

Rebuild your metadata:
Linux/AIX/Solaris - python /usr/bin/panopta-agent/panopta_agent.py --rebuild-metadata
FreeBSD - python /usr/local/panopta-agent/bin/panopta_agent.py --rebuild-metadata

Add it to the server's config in the Panopta control panel:
http://answers.panopta.com/how-do-i-add-a-monitoring-agent-resource/

