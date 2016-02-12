from __future__ import absolute_import

from influxdb import InfluxDBClient
from time_execution.backends.base import BaseMetricsBackend


class InfluxBackend(BaseMetricsBackend):
    def __init__(self, **kwargs):
        kwargs.setdefault('use_udp', True)
        self.client = InfluxDBClient(**kwargs)

    def write(self, name, **data):
        value = data.pop('value')
        self.client.write_points([{
            'measurement': name,
            'fields': {
                'value': value,
                },
            'tags': data,
            }])

