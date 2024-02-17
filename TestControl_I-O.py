from machine import Pin, Timer
''' La Documentación para este test de control de I/O se encuentra:
                                                            https://docs.micropython.org/en/latest/library/machine.Pin.html
'''
# Configura los pines como salidas.
'''Tener en cuenta que los pines numericamente no coinciden con la numeración del micro. Consultar al micro.'''

# p6 = Pin(4, Pin.OUT)
# p7 = Pin(5, Pin.OUT)
# p12 = Pin(9, Pin.OUT)

# Enciende los pines
#p6.value(1)
#p7.value(1)
#p12.value(1)



# Apaga el pin
# p6.value(0)
# p7.value(0)
# p12.value(0)

'''--------------------------------------------------------------'''
'''--------------------------------------------------------------'''
''' 			Test de LED de RPI			    '''
" _ Asigno Pin                                                       "
# led = Pin("LED", Pin.OUT)

" Test de parpadeo"
# timer = Timer()
# def blink(timer):
#     led.toggle()
# timer.init(freq=2.5, mode=Timer.PERIODIC, callback=blink)

" Si solo quiero que solo prenda y se apague "
#led.on()  # Enciende el LED
# led.off()
'''--------------------------------------------------------------'''
'''--------------------------------------------------------------'''
