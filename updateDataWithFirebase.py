import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from mcp3208 import MCP3208


adc=MCP3208()

cred = credentials.Certificate("../haniumnoisecheckapp-firebase-adminsdk-bov3x-d0d71d795f.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://haniumnoisecheckapp.firebaseio.com/'
})

ref = db.reference('/noise/id')
ref_id = ref.child('1')


while True:
    tmp= adc.read(0)
    if( tmp > 30 ):
        ref_id.push({
            'time': time.ctime(),
            'vib':tmp,
    })
    print("uploaded complete")
