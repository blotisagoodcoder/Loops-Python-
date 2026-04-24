Emergecy_codes = {
'Help!' : '29102',
'Requesting Backup!' : '12393',
'EMERGENCY!' : '9421'
 }

print('Emergency Code for HELP:')
print(Emergecy_codes.get('HELP','NOT FOUND.'))

print('Emergency Code for BACKUP: ')
print(Emergecy_codes.get('BACKUP', 'NOT FOUND.'))

print('Emergency Code for EMERGENCY: ')
print(Emergecy_codes.get('EMERGENCY', 'NOT FOUND.'))