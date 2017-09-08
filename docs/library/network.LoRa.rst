.. currentmodule:: network

class LoRa
==========

This class provides a driver for the LoRa network processor in the **LoPy**. Below is an example demonstrating LoRaWAN Activation by Personalisation usage::

    from network import LoRa
    import socket
    import binascii
    import struct

    # Initialize LoRa in LORAWAN mode.
    lora = LoRa(mode=LoRa.LORAWAN)

    # create an ABP authentication params
    dev_addr = struct.unpack(">l", binascii.unhexlify('00 00 00 05'.replace(' ','')))[0]
    nwk_swkey = binascii.unhexlify('2B 7E 15 16 28 AE D2 A6 AB F7 15 88 09 CF 4F 3C'.replace(' ',''))
    app_swkey = binascii.unhexlify('2B 7E 15 16 28 AE D2 A6 AB F7 15 88 09 CF 4F 3C'.replace(' ',''))

    # join a network using ABP (Activation By Personalization)
    lora.join(activation=LoRa.ABP, auth=(dev_addr, nwk_swkey, app_swkey))

    # create a LoRa socket
    s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

    # set the LoRaWAN data rate
    s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)

    # make the socket non-blocking
    s.setblocking(False)

    # send some data
    s.send(bytes([0x01, 0x02, 0x03]))

    # get any data received...
    data = s.recv(64)
    print(data)

.. warning::
  Please ensure that there is an **antenna connected** to your device before sending/receiving LoRa messages as inproper use (e.g. without an antenna), may damage the device.


Additional examples
-------------------

For various other complete LoRa examples, check here for :ref:`additional examples<lora_examples>`.

Constructors
------------

.. class:: LoRa(id=0, ...)

   Create and configure a LoRa object. See ``init`` for params of configuration. ::

        lora = LoRa(mode=LoRa.LORAWAN)

Methods
-------

.. method:: lora.init(mode, \*, frequency=868000000, tx_power=14, bandwidth=LoRa.868000000, sf=7, preamble=8, coding_rate=LoRa.CODING_4_5, power_mode=LoRa.ALWAYS_ON, tx_iq=false, rx_iq=false, adr=false, public=true, tx_retries=1, device_class=LoRa.CLASS_A)

   This method is used to set the LoRa subsystem configuration and to specific raw LoRa or LoRaWAN.

   The arguments are:

     - ``mode`` can be either ``LoRa.LORA`` or ``LoRa.LORAWAN``.
     - ``frequency`` accepts values between 863000000 and 870000000 in the 868 band, or between 902000000 and 928000000 in the 915 band.
     - ``tx_power`` is the transmit power in dBm. It accepts between 2 and 14 for the 868 band, and between 5 and 20 in the 915 band.
     - ``bandwidth`` is the channel bandwidth in KHz. In the 868 band the accepted values are ``LoRa.BW_125KHZ`` and ``LoRa.BW_250KHZ``. In the 915 band the accepted values are ``LoRa.BW_125KHZ`` and ``LoRa.BW_500KHZ``.
     - ``sf`` sets the desired spreading factor. Accepts values between 7 and 12.
     - ``preamble`` configures the number of pre-amble symbols. The default value is 8.
     - ``coding_rate`` can take the following values: ``LoRa.CODING_4_5``, ``LoRa.CODING_4_6``,
       ``LoRa.CODING_4_7`` or ``LoRa.CODING_4_8``.
     - ``power_mode`` can be either ``LoRa.ALWAYS_ON``, ``LoRa.TX_ONLY`` or ``LoRa.SLEEP``. In ``ALWAYS_ON`` mode, the radio is always listening for incoming packets whenever a transmission is not taking place. In ``TX_ONLY`` the radio goes to sleep as soon as the transmission completes. In ``SLEEP`` mode the radio is sent to sleep permanently and won't accept any commands until the power mode is changed.
     - ``tx_iq`` enables TX IQ inversion.
     - ``rx_iq`` enables RX IQ inversion.
     - ``adr`` enables Adaptive Data Rate.
     - ``public`` selects between the public and private sync word.
     - ``tx_retries`` sets the number of TX retries in ``LoRa.LORAWAN`` mode.
     - ``device_class`` sets the LoRaWAN device class. Can be either ``LoRa.CLASS_A`` or ``LoRa.CLASS_C``.

    .. note::

       In ``LoRa.LORAWAN`` mode, only ``adr``, ``public``, ``tx_retries`` and ``device_class`` are used. All the other
       params will be ignored as they are handled by the LoRaWAN stack directly. On the other hand, in ``LoRa.LORA`` mode
       from those 3 arguments, only the ``public`` one is important in order to program the sync word. In ``LoRa.LORA`` mode ``adr``,
       ``tx_retries`` and ``device_class`` are ignored since they are only relevant to the LoRaWAN stack.

   For example, you can do::

      # initialize in raw LoRa mode
      lora.init(mode=LoRa.LORA, tx_power=14, sf=12)

   or::

      # initialize in LoRaWAN mode
      lora.init(mode=LoRa.LORAWAN)

.. method:: lora.join(activation, auth, \*, timeout=None)

    Join a LoRaWAN network. The parameters are:

      - ``activation``: can be either ``LoRa.OTAA`` or ``LoRa.ABP``.
      - ``auth``: is a tuple with the authentication data.

    In the case of ``LoRa.OTAA`` the authentication tuple is: ``(app_eui, app_key)``. Example::

          from network import LoRa
          import socket
          import time
          import binascii

          # Initialize LoRa in LORAWAN mode.
          lora = LoRa(mode=LoRa.LORAWAN)

          # create an OTAA authentication parameters
          app_eui = binascii.unhexlify('AD A4 DA E3 AC 12 67 6B'.replace(' ',''))
          app_key = binascii.unhexlify('11 B0 28 2A 18 9B 75 B0 B4 D2 D8 C7 FA 38 54 8B'.replace(' ',''))

          # join a network using OTAA (Over the Air Activation)
          lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)

          # wait until the module has joined the network
          while not lora.has_joined():
              time.sleep(2.5)
              print('Not yet joined...')

    In the case of ``LoRa.ABP`` the authentication tuple is: ``(dev_addr, nwk_swkey, app_swkey)``. Example::

          from network import LoRa
          import socket
          import binascii
          import struct

          # Initialize LoRa in LORAWAN mode.
          lora = LoRa(mode=LoRa.LORAWAN)

          # create an ABP authentication params
          dev_addr = struct.unpack(">l", binascii.unhexlify('00 00 00 05'.replace(' ','')))[0]
          nwk_swkey = binascii.unhexlify('2B 7E 15 16 28 AE D2 A6 AB F7 15 88 09 CF 4F 3C'.replace(' ',''))
          app_swkey = binascii.unhexlify('2B 7E 15 16 28 AE D2 A6 AB F7 15 88 09 CF 4F 3C'.replace(' ',''))

          # join a network using ABP (Activation By Personalization)
          lora.join(activation=LoRa.ABP, auth=(dev_addr, nwk_swkey, app_swkey))

.. method:: lora.bandwidth([bandwidth])

    Get or set the bandwidth in raw LoRa mode (``LoRa.LORA``). Can be either ``LoRa.BW_125KHZ`` ``(0)``, ``LoRa.BW_250KHZ`` ``(1)`` or ``LoRa.BW_500KHZ`` ``(2)``.::

		# get raw LoRa Bandwidth
		lora.bandwidth()

		# set raw LoRa Bandwidth
		lora.bandwidth(LoRa.BW_125KHZ)

.. method:: lora.frequency([frequency])

    Get or set the frequency in raw LoRa mode (``LoRa.LORA``). The allowed range is between 863000000 and 870000000 Hz for the 868 MHz band version or between 902000000 and 928000000 Hz for the 915 MHz band version.::

		# get raw LoRa Frequency
		lora.frequency()

		# set raw LoRa Frequency
		lora.frequency(868000000)

.. method:: lora.coding_rate([coding_rate])

    Get or set the coding rate in raw LoRa mode (``LoRa.LORA``). The allowed values are: ``LoRa.CODING_4_5`` ``(0)``, ``LoRa.CODING_4_6`` ``(1)``, ``LoRa.CODING_4_7`` ``(2)`` and ``LoRa.CODING_4_8`` ``(3)``. ::

		# get raw LoRa Coding Rate
		lora.coding_rate()

		# set raw LoRa Coding Rate
		lora.coding_rate(LoRa.CODING_4_5)

.. method:: lora.preamble([preamble])

    Get or set the number of preamble symbols in raw LoRa mode (``LoRa.LORA``).::

		# get raw LoRa preamble symbols
		lora.preamble()

		# set raw LoRa preamble symbols
		lora.preamble(LoRa.CODING_4_5)

.. method:: lora.sf([sf])

    Get or set the spreading factor value in raw LoRa mode (``LoRa.LORA``). The minimmum value is 7 and the maximum is 12.::

		# get raw LoRa spread factor value
		lora.sf()

		# set raw LoRa spread factor value
		lora.sf(7)

.. method:: lora.power_mode([power_mode])

    Get or set the power mode in raw LoRa mode (``LoRa.LORA``). The accepted values are: ``LoRa.ALWAYS_ON``, ``LoRa.TX_ONLY`` and ``LoRa.SLEEP``.::

.. method:: lora.stats()

    Return a named tuple with usefel information from the last received LoRa or LoRaWAN packet. The named tuple has the following form:

    ``(rx_timestamp, rssi, snr, sftx, sfrx, sftx, tx_trials)``

    Example: ::

        lora.stats()


    Where:

       - ``rx_timestamp`` is an internat timestamp of the last received packet with microseconds presicion.
       - ``rssi`` holds the received signal strength in dBm.
       - ``snr`` contains the signal to noise ratio id dB.
       - ``sfrx`` tells the data rate (in the case of ``LORAWAN`` mode) or the spreading factor (in the case of ``LORA`` mode) of the last packet received.
       - ``sftx`` tells the data rate (in the case of ``LORAWAN`` mode) or the spreading factor (in the case of ``LORA`` mode) of the last packet transmitted.
       - ``tx_trials`` is the number of tx attempts of the last transmitted packet (only relevant for ``LORAWAN`` confirmed packets).

.. method:: lora.has_joined()

    Returns ``True`` if a LoRaWAN network has been joined. ``False`` otherwise.::

		lora.has_joined()

.. method:: lora.add_channel(index, \*, frequency, dr_min, dr_max)

    Add a LoRaWAN channel on the specified index. If there's already a channel with that index it will be replaced with the new one.

    The arguments are:

      - ``index``: Index of the channel to add. Accepts values between **0 and 15 for EU** and between **0 and 71 for US**.
      - ``frequency``: Center frequency in Hz of the channel.
      - ``dr_min``: Minimum data rate of the channel (0-7).
      - ``dr_max``: Maximum data rate of the channel (0-7).

	Examples: ::

		lora.add_channel(index=0, frequency=868000000, dr_min=5, dr_max=6)

.. method:: lora.remove_channel(index)

     Removes the channel from the specified index. On the 868MHz band the channels 0 to 2 cannot be removed, they can only be replaced by other channels using the ``lora.add_channel`` method. A way to remove all channels except for one is to add the same channel, 3 times on indexes 0, 1 and 2. An example can be seen below: ::

		 lora.remove_channel()

     On the 915MHz band there are no restrictions around this.

.. method:: lora.mac()

   Returns a byte object with the 8-Byte MAC address of the LoRa radio.::

	   lora.mac()

.. method:: lora.callback(trigger, handler=None, arg=None)

   Specify a callback handler for the LoRa radio. The trigger types are ``LoRa.RX_PACKET_EVENT``, ``LoRa.TX_PACKET_EVENT`` and ``LoRa.TX_FAILED_EVENT``

   The ``LoRa.RX_PACKET_EVENT` event is raised for every received packet.
   The ``LoRa.TX_PACKET_EVENT`` event is raised as soon as the packet transmisison cycle ends. In the case of non-confirmed transmissions, this will occur at the end of the
   receive windows, but, in the case of confirmed transmissions, this event will only be raised if the **ack** is received. If the **ack** is not received ``LoRa.TX_FAILED_EVENT``
   will be raised after the number of ``tx_retries`` configured have been performed.

   An example of how this callback functions can be seen the in method :ref:`lora.events() <lora_events>`.

.. method:: lora.ischannel_free(rssi_threshold)

    This method is used to check for radio activity on the current LoRa channel, and if the rssi of the measured activity is lower than the `rssi_threshold` given, the return value will
    be ``True``, otherwise ``False``. Example::

        lora.ischannel_free(-100)

.. method:: lora.set_battery_level(level)

    Set the battery level value that will be sent when the LoRaWAN MAC command that retrieves the battery level is received. This command is sent by the network and handled
    automatically by the LoRaWAN stack. Value should be in percentage, from 0 to 100. Values larger than 100 will be clipped.::

        lora.set_battery_level(75)

.. _lora_events:

.. method:: lora.events()

   This method returns a value with bits sets (if any) indicating the events that have triggered the callback. Please note that
   by calling this function the internal events registry is cleared automatically, therefore calling it immediately for a second time
   will most likely return a value of 0.

   Example::

        def lora_cb(lora):
            events = lora.events()
            if events & LoRa.RX_PACKET_EVENT:
                print('Lora packet received')
            if events & LoRa.TX_PACKET_EVENT:
                print('Lora packet sent')

        lora.callback(trigger=(LoRa.RX_PACKET_EVENT | LoRa.TX_PACKET_EVENT), handler=lora_cb)


Constants
---------

.. data:: LoRa.LORA
          LoRa.LORAWAN

    LoRa stack mode

.. data:: LoRa.OTAA
          LoRa.ABP

    LoRaWAN join procedure

.. data:: LoRa.ALWAYS_ON
          LoRa.TX_ONLY
          LoRa.SLEEP

    Raw LoRa power mode

.. data:: LoRa.BW_125KHZ
          LoRa.BW_250KHZ
          LoRa.BW_500KHZ

    Raw LoRa bandwidth

.. data:: LoRa.CODING_4_5
          LoRa.CODING_4_6
          LoRa.CODING_4_7
          LoRa.CODING_4_8

    Raw LoRa coding rate

.. data:: LoRa.RX_PACKET_EVENT
          LoRa.TX_PACKET_EVENT
          LoRa.TX_FAILED_EVENT

    Callback trigger types (may be ORed)

.. data:: LoRa.CLASS_A
          LoRa.CLASS_C

    LoRaWAN device class


Working with LoRa and LoRaWAN sockets
-------------------------------------

LoRa sockets are created in the following way::

   import socket
   s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

And they **must** be created after initializing the LoRa network card.

LoRa sockets support the following standard methods from the :class:`socket <.socket>` module:

.. method:: socket.close()

   Usage: ``s.close()``

.. method:: socket.bind(port_number)

   Usage: ``s.bind(1)``

   .. note::

      The ``.bind()`` method is only applicable when the radio is configured in ``LoRa.LORAWAN`` mode.

.. method:: socket.send(bytes)

   Usage: ``s.send(bytes([1, 2, 3]))`` or: ``s.send('Hello')``

.. method:: socket.recv(bufsize)

   Usage: ``s.recv(128)``

.. method:: socket.setsockopt(level, optname, value)

   Set the value of the given socket option. The needed symbolic constants are defined in the
   socket module (SO_* etc.). In the case of LoRa the values are always integers. Examples::

      # configuring the data rate
      s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)

      # selecting non-confirmed type of messages
      s.setsockopt(socket.SOL_LORA, socket.SO_CONFIRMED, False)

      # selecting confirmed type of messages
      s.setsockopt(socket.SOL_LORA, socket.SO_CONFIRMED, True)

   .. note::

      Socket options are only applicable when the LoRa radio is used in ``LoRa.LORAWAN`` mode.
      When using the radio in ``LoRa.LORA`` mode, use the class methods to change the spreading
      factor, bandwidth and coding rate to the desired values.

.. method:: socket.settimeout(value)

   Sets the socket timeout value in seconds. Accepts floating point values.

   Usage: ``s.settimeout(5.5)``

.. method:: socket.setblocking(flag)

   Usage: ``s.setblocking(True)``
