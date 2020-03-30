const mqtt = require('async-mqtt')

const mqttEndpoint = 'mqtts://mqtt.waylay.io'

// fill in the empty fields by following the steps in the documentation: https://docs.waylay.io/features/mqtt_broker_manager/
const mqttOptions = {
  'clientId': '',
  'username': '',
  'password': '',
  'port': ''
}

const publishAcl = ''
const payload = 'test'

async function connectToMQTTClient () {
  const mqttClient = await mqtt.connect(mqttEndpoint, mqttOptions)

  mqttClient.on('connect', () => {
    console.log('Connected to mqtt client')
    return mqttClient
  })
}

async function examplePublish (publishAcl, payload) {
  const mqttClient = connectToMQTTClient()
  try {
    await mqttClient.publish(publishAcl, payload)
    await mqttClient.end()
  } catch (e) {
    console.log(e.stack)
  }
}

examplePublish(publishAcl, payload)
