var baseURL = 'http://127.0.0.1:5000/time-allocation';

var data = {
  'event_name':'assignment',
  'deadline':'deadline',
  'hours':'durationTime',
  'blocks':'chunks'
}


var options = {
  'method' : 'post',
  'contentType': 'application/json',
  'payload': '{"event_name": "assignment"}'
}

fetch('http://127.0.0.1:5000/time-allocation')
  .then(response => response.json())
  .then(data =>console.log(data))
