# language_detection_in_gcp


Simple language detection and multi-language detection microservice, CICD-ed using Google Cloud Build, deployed as a microservice in Cloud Run.

## 2 POST endpoints

1. `/` 

        singular language detection with confidence values
        returns {predicted: <language>, confidence: <confidence>}
  
2. `/multiple`

        multiple language detection, list of language and phrases in the sentence that is detected in that language
        returns {results: [<language>: <sentence containing the <language> language>]}
        
## 1 Get Endpoint

1. `/`
     
       Shows the currently supported languages to be detected
       
