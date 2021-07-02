import time
import os
from prometheus_client.core import GaugeMetricFamily, REGISTRY, CounterMetricFamily
from prometheus_client import start_http_server
from app.app import  get_status_code

class CustomCollector(object):
    def __init__(self):
      pass

    def collect(self):
      g = GaugeMetricFamily("custom_exporter_py", "This collector verify the status code of request", labels=['url'])
      for row in get_status_code():
        g.add_metric([row['url']], row['status']) 
      yield g

if __name__ == '__main__':
    start_http_server(5530)
    REGISTRY.register(CustomCollector())
    while True:
        time.sleep(1)
