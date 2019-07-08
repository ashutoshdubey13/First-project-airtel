import aerospike
import sys
config = {'hosts':[('127.0.0.1',3000)],'policies':{'timeout':1000}}
try:
    client=aerospike.client(config)
    client.connect()
    print ('got connected')
except:
    print ('failed to connect')
    sys.exit(1)
key=('test','demo','foo')

try:
    client.put(key,{'Name':'Ashutosh','Age':21})
    print("data inserted")
except Exception as e:
    print ("error:{0}".format(e))

(key,metadata,record)=client.get(key)
client.close()
