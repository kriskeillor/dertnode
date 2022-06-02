import serial
port_list = ["/dev/ttyAMA0"]
for port in port_list:
  try:
    serPrt = serial.Serial(port,
      baudrate=115200,
      bytesize=serial.EIGHTBITS,
      parity=serial.PARITY_NONE,
      stopbits=serial.STOPBITS_ONE,
      timeout=0,
      xonxoff=False,
      rtscts=False,
      write_timeout=None,
      dsrdtr=False,
      inter_byte_timeout=None,
      exclusive=True)
    print("Serial port", port, " ready for test.")
    while True:
      if (serPrt.in_waiting > 0):
        # read and convert from binary to ASCII
        data_str = serPrt.read(serPrt.in_waiting).decode("ascii")
        print(data_str, end='')
      #val = serialPort.read(1)
      #val_str = val.decode("utf-8")
      #print(val_str)
  except IOError as err:
    print ("IOError on", port, "\n");
    print (err.errno)
    print (e)
