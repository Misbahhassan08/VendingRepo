#!/usr/bin/env python

import pigpio

class decoder:

   """Class to decode mechanical rotary encoder pulses."""

   def __init__(self, pi, gpioA, gpioB,callback,weighting=0.0):

      """
      Instantiate the class with the pi and gpios connected to
      rotary encoder contacts A and B.  The common contact
      should be connected to ground.  The callback is
      called when the rotary encoder is turned.  It takes
      one parameter which is +1 for clockwise and -1 for
      counterclockwise.

      EXAMPLE

      import time
      import pigpio

      import rotary_encoder

      pos = 0

      def callback(way):

         global pos

         pos += way

         print("pos={}".format(pos))

      pi = pigpio.pi()

      decoder = rotary_encoder.decoder(pi, 7, 8, callback)

      time.sleep(300)

      decoder.cancel()

      pi.stop()

      """

      self.pi = pi
      self.gpioA = gpioA
      self.gpioB = gpioB
      self.callback = callback
      
      if weighting < 0.0:
         weighting = 0.0
      elif weighting > 0.99:
         weighting = 0.99
         
      self._new = 1.0 - weighting # Weighting for new reading.
      self._old = weighting       # Weighting for old reading.

      self.levA = 0
      self.levB = 0

      self.lastGpio = None
      self._high_tick = None
      self._period = None
      self._high = None

      self.pi.set_mode(gpioA, pigpio.INPUT)
      self.pi.set_mode(gpioB, pigpio.INPUT)

      self.pi.set_pull_up_down(gpioA, pigpio.PUD_UP)
      self.pi.set_pull_up_down(gpioB, pigpio.PUD_UP)

      self.cbA = self.pi.callback(gpioA, pigpio.EITHER_EDGE, self._pulse)
      self.cbB = self.pi.callback(gpioB, pigpio.EITHER_EDGE, self._pulse)
      self._cb = self.pi.callback(gpioA, pigpio.EITHER_EDGE, self._pulse)
   
   def _pulse(self, gpio, level,tick):

      """
      Decode the rotary encoder pulse.

                   +---------+         +---------+      0
                   |         |         |         |
         A         |         |         |         |
                   |         |         |         |
         +---------+         +---------+         +----- 1

             +---------+         +---------+            0
             |         |         |         |
         B   |         |         |         |
             |         |         |         |
         ----+         +---------+         +---------+  1
      """
      self.forword = "Forward"
      self.reverse = "Reverse"
      if level == 1:

         if self._high_tick is not None:
            t = pigpio.tickDiff(self._high_tick, tick)

            if self._period is not None:
               self._period = (self._old * self._period) + (self._new * t)
            else:
               self._period = t

         self._high_tick = tick

      elif level == 0:

         if self._high_tick is not None:
            t = pigpio.tickDiff(self._high_tick, tick)

            if self._high is not None:
               self._high = (self._old * self._high) + (self._new * t)
            else:
               self._high = t
      if gpio == self.gpioA:
         self.levA = level
      else:
         self.levB = level;

      if gpio != self.lastGpio: # debounce
         self.lastGpio = gpio

         if   gpio == self.gpioA and level == 1:
            if self.levB == 1:
               self.callback(1,self.forword,1)
         elif gpio == self.gpioB and level == 1:
            if self.levA == 1:
               self.callback(-1,self.reverse,1)
               
   def frequency(self):
      """
      Returns the PWM frequency.
      """
      if self._period is not None:
         feq = int((1000000.0 / self._period)/60)
         return feq
      else:
         return 0.0

   def pulse_width(self):
      """
      Returns the PWM pulse width in microseconds.
      """
      if self._high is not None:
         return self._high
      else:
         return 0.0

   def duty_cycle(self):
      """
      Returns the PWM duty cycle percentage.
      """
      if self._high is not None:
         return 100.0 * self._high / self._period
      else:
         return 0.0

   def cancel(self):

      """
      Cancel the rotary encoder decoder.
      """

      self.cbA.cancel()
      self.cbB.cancel()
      self._cb.cancel()

if __name__ == "__main__":

   import time
   import pigpio
   
   #PWM_GPIO = 4
   #RUN_TIME = 60.0
   #SAMPLE_TIME = 2.0
   
   pos = 0
   puls = 0
   def callback(way,direction,pulses):

      global pos
      global puls
      pos += way
      puls += pulses
      f = decoder.frequency()
      print(f"pos : {pos} &  Dir : {direction} & Pulses : {puls} & Freq : {f}")
   pi = pigpio.pi()

   decoder = decoder(pi, 17, 18, callback)
   '''start = time.time()
   while (time.time() - start) < RUN_TIME:

      time.sleep(SAMPLE_TIME)

      f = decoder.frequency()
      pw = decoder.pulse_width()
      dc = decoder.duty_cycle()
     
      print("f={:.1f} pw={} dc={:.2f}".format(f, int(pw+0.5), dc))
'''   
   
   time.sleep(300)
   
   decoder.cancel()
   pi.stop()


