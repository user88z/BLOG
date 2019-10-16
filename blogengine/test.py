message_from_FM = '$1501.20180910094609;A;866796036848626;89701012418192532668,1,25001;S,0235,1700,+34,1;C,"250,20,4D0E,14E8,64,250,02,1285,2C3A,71,250,99,39A5,2E60,73,250,02,1285,2C39,75,250,02,1285,2C3D,77,250,01,00DD,3860,80";Q,0,0,123;N,[M2,S60,P0,p25,N30,t-30,G60,g2,F12];L,r8,2,t8,p18,14,s0,0,m50,0,0,0,o0,c20,0,g2,m0,a0,d0,0,n24,0,F0:0,0,15,31:0,0,30,56:rn;*F5\r\n'


def validation(message):
    message_crc = message.split(';')[-1:][0][1:3]
    message_bytes = bytes(message.rstrip(), 'utf-8')
    crc = 0
    for symbol in message_bytes[:-3]:
        crc = crc + symbol
    crc = str(hex(crc % 256))[2:].upper()
    if message_crc == crc and message[0] == '$':
        return True
    return False

if validation(message_from_FM):
    print('Done!')
print(validation(message_from_FM))
