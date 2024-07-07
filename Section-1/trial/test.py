# from pycipher import Rot13
# a=Rot13().encipher('defend the east wall of the castle')
# print(a)
# b=Rot13().decipher(a)
# print(b)

# import codecs
# #48657861646563696D616C206973206A757374206F6E65206F66207365766572616C2028696E66696E6974656C792920706F737369626C65207261646963657321
# # Example hex values
# hex_values = "48657861646563696D616C206973206A757374206F6E65206F66207365766572616C2028696E66696E6974656C792920706F737369626C65207261646963657321" 
# result_string = codecs.decode(hex_values, 'hex').decode('utf-8')
# print(result_string)



import base64
base64_message = 'QmFzZTY0IGhhcyBhIGxvdCBvZiBjb3VzaW5zIHN1Y2ggYXMgQmFzZTMyLCBCYXNlNTgsIGV0Yy4='
base64_bytes = base64_message.encode('ascii')
print(base64_bytes)
message_bytes = base64.b64decode(base64_bytes)
print(message_bytes)
message = message_bytes.decode('ascii')
print(message)