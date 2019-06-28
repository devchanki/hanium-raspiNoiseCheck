from mcp3208 import MCP3208
import time

adc=MCP3208()
while True:
    print('ADC[{}]: {:.2f}'.format(0,adc.read(0)))
    time.sleep(0.1)
