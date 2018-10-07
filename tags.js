// Imports the Google Cloud client library.
const Storage = require('@google-cloud/storage');

// Imports the Google Cloud client library
const vision = require('@google-cloud/vision');

//define key variables
var cwd = process.cwd();

var key = cwd + '/quikShop.json';
var image = cwd + '/image1.jpeg';
var done = 0

var tags = []

GOOGLE_APPLICATION_CREDENTIAL = key;

function convert(array, target){
  var target = array.toString()
  var target = target.replace(/\r/g, "").replace(/\n/g, "");
  console.log(target)

}

const client = new vision.ImageAnnotatorClient();

//execute image calculation
client
  .labelDetection(image)
  .then(results => {
    const labels = results[0].labelAnnotations;
    console.log('Labels:');
    labels.forEach(label => {tags.push(label.description)});
    
    console.log(tags)

    if(done != 2){
      done = done + 1
    }
    else{
      convert(tags, tags)
    }
  })
  .catch(err => {
    console.error('ERROR:', err);
  });


client
  .logoDetection(image)
  .then(results => {
    const logos = results[0].logoAnnotations;
    console.log('Logos:');
    logos.forEach(logo => {tags.push(logo.description)});
    
    console.log(tags)

    if(done != 2){
      done = done + 1
    }
    else{
      convert(tags, tags)
    }
  })
  .catch(err => {
    console.error('ERROR:', err);
  });

client
  .textDetection(image)
  .then(results => {
    const detections = results[0].textAnnotations;
    console.log('Text:');
    detections.forEach(text => {tags.push(text.description)});
    
    console.log(tags)

    if(done != 2){
      done = done + 1
    }
    else{
      convert(tags, tags)
    }
  })
  .catch(err => {
    console.error('ERROR:', err);
  });