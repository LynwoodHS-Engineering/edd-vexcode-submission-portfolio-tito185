while True:
 if bumper_a.pressing() and bumper_b.pressing():
  led_c.on()
  led_d.off()
 else:
  led_d.on()
  led_c.off()
