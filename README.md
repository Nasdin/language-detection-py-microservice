# Language detection as a microservice

Language detection and multi-language detection microservice.

The accuracy increases the fewer languages you configure this microservice to detect.
Accuracy ranges from 85% to 100% depending on range of languages to be detected, modifiable in the code.

## Language support in this microservice
The following languages are supported for detection, with an estimated accuracy of 95%

        ENGLISH
        CHINESE
        MALAY
        JAPANESE
        KOREAN
        RUSSIAN
        THAI
        VIETNAMESE
        TAGALOG
        HINDI

## Deployment
Personally, I've setup the CICD using Google Cloud Build, and deployed as a microservice in Cloud Run. There are no configurations to be made in the repository if you happen to fork it. Simply click a few buttons on GCP Cloud Run and Cloud Build to import this repository, then add the "CLIENT" environment as your secret key

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
       
