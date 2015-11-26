import agent_util
import sys
import os
from datetime import datetime, timedelta

class LogstashForwarderPlugin(agent_util.Plugin):
    textkey = "logstash_forwarder"
    label = "Logstash Forwarder"
 
    @classmethod
    def get_metadata(self, config):
        status = agent_util.SUPPORTED
        msg = None

        if not os.path.isdir("/var/log/logstash-forwarder"):
            self.log.info("logstash-forwarder not found")
            status = agent_util.UNSUPPORTED
            msg = "logstash-forwarder log folder not found!"
            return {}

        data = {
            "logs_per_minute": {
                "label": "Logs forwarded per minute",
                "options": None,
                "status": status,
                "error_message": msg,
                "unit": None,
            }
        }
        return data

    def check(self, textkey, option, config):
        cmd = 'tail -25 /var/log/logstash-forwarder/logstash-forwarder.err'
        retcode, output = agent_util.execute_command(cmd)
        logs_per_min = 0
        last_minute = output.strip().split('\n')
        for item in last_minute:
            if 'processing' in item:
                line = item.split()
                time = ' '.join(line[0:2])
                parts = time.split('.')
                time = datetime.strptime(parts[0], "%Y/%m/%d %H:%M:%S")
                time = time.replace(microsecond=int(parts[1]))
                if (datetime.now() - timedelta(seconds=60)) > time: continue
                else: logs_per_min = logs_per_min + int(line[-2])
            else: continue
        return logs_per_min

