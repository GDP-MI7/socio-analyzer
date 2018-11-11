const Twit = require('twit')
const fs = require('fs');

const hashTag = "#girlPower"

var T = new Twit({
  consumer_key: "***************************",
  consumer_secret: "***************************",
  access_token: "***************************",
  access_token_secret: "***************************",
  timeout_ms: 60 * 1000,  // optional HTTP request timeout to apply to all requests.
  strictSSL: true,     // optional - requires SSL certificates to be valid.
})

T.get('search/tweets', { q: hashTag, count: 1000 }, function (err, data, response) {
  var twitsData = JSON.stringify(data.statuses);
  fs.writeFile('./output.json', twitsData, 'utf8', function () {
    console.log("Output generated successfully")
  });
})    