
async function handleRequest (req, res) {
  try {
    const _ = require("lodash")
    const codes = [{code:5501, name: "vibration"}, {code:5601, name: "lightLuminance"},{code:5600, name: "temperature"}, {code:5602, name: "times_two"}, {code:5603, name: "luminance_value"}]
    const notifications = req.body.notifications

    var data = _.map(notifications, payload => {
      console.log('payload', payload)
      var path = payload.path.split("/")
      var path_code = parseInt(path[path.length - 1])
      var value  =  parseFloat(Buffer.from(payload.payload, 'base64').toString("ascii"))
      var resource = payload.ep
      var code = _.find(codes, code => {return code.code === path_code})
      var obj = {
       resource
      }
      if(!code){
        obj[path_code] = value
      }else {
        obj[code.name] = value
      }

      return obj
    })
    waylay.data.postSeries(data)
      .then(response => res.send(response))
      .catch(err => {
        const error = err.response ? err.response.data : err.message
        console.error(error)
        res.status(500).send(error)
    })
  }catch (err){
    console.error(err)
  }
}
