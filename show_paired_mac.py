#!/usr/bin/env python3

"""
https://eleccelerator.com/wiki/index.php?title=DualShock_4
"""

import hid
import time

# enumerate USB devices
for d in hid.enumerate():
    keys = list(d.keys())
    keys.sort()
    for key in keys:
        print("%s : %s" % (key, d[key]))
    print()

# try opening a device, then perform write and read
try:
    print("Opening the device")

    h = hid.device()
    h.open(1356, 1476)  # Sony Dualshock 4

    print("Manufacturer: %s" % h.get_manufacturer_string())
    print("Product: %s" % h.get_product_string())
    print("Serial No: %s" % h.get_serial_number_string())

    # enable non-blocking mode
    h.set_nonblocking(1)

    feature_report = h.get_feature_report(0x12, 255)

    bytes = list(reversed(feature_report))
    remote_mac = bytes[0:6]

    for byte in remote_mac:
        print(format(byte, "02x"))

    # write some data to the device
    # print("Write the data")
    # h.write([0, 63, 35, 35] + [0] * 61)

    # wait
    # time.sleep(0.05)

    # read back the answer
    # print("Read the data")
    # while True:
    #    d = h.read(64)
    #    if d:
    #        print(d)
    #    else:
    #        break

    print("Closing the device")
    h.close()

except IOError as ex:
    print(ex)


print("Done")