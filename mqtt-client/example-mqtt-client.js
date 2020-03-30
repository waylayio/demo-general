const mqtt = require('async-mqtt')

const mqttEndpoint = 'mqtts://mqtt-staging.waylay.io'

// fill in the empty fields by following the steps in the documentation: https://docs.waylay.io/features/mqtt_broker_manager/
const mqttOptions = {
  'clientId': '',
  'username': '',
  'password': '',
  'port': '8883'
}

const publishAcl = ''
const payload = JSON.stringify({ resource: 'resourceName', metricName: 'metric value' })

async function connectToMQTTClient () {
  const mqttClient = await mqtt.connect(mqttEndpoint, mqttOptions)

  mqttClient.on('connect', () => {
    console.log('Connected to mqtt client')
    examplePublish(publishAcl, payload, mqttClient)
  })
}

async function examplePublish (publishAcl, payload, mqttClient) {
  try {
    await mqttClient.publish(publishAcl, payload)
    console.log('Payload published')
    await mqttClient.end()
    console.log('Client closed')
  } catch (e) {
    console.log(e.stack)
  }
}

connectToMQTTClient()
