# language_detection_in_gcp


Simple language detection and multi-language detection microservice, CICD-ed using Google Cloud Build, deployed as a microservice in Cloud Run.

## 2 POST endpoints

1. `/` 

        singular language detection with confidence values
#### returns 

        {predicted: <language>, confidence: <confidence>}
#### expects 

        {message: <message>, key: <secret client key>}
  
2. `/multiple`

        multiple language detection, list of language and phrases in the sentence that is detected in that language
#### returns 
        
        {results: [<language>: <sentence containing the <language> language>]}
        
#### expects 

        {message: <message>, key: <secret client key>}
        
### Example for multiple

        {"message": "what does this mean 'dua ekor burung'",
        "key": "MYSPECIALKEY"}

#### returns
```{
    "results": [
        {
            "ENGLISH": "what does this mean "
        },
        {
            "MALAY": "'dua ekor burung'"
        }
    ]
}
```
       
        
## 1 Get Endpoint

1. `/`
     
       Shows the currently supported languages to be detected
       No parameters or headers necessary
       
       
       
## Authentication

The POST endpoints requires the caller to be authorized via providing a "key" in the request body.
The key needs to match the Client key which is fed via an Environment variable, "CLIENT" in the docker container running this microservice. 
       
