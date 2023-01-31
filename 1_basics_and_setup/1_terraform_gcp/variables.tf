terraform ***REMOVED***
  required_version = ">= 1.0"
  backend "local" ***REMOVED******REMOVED***  # Can change from "local" to "gcs" (for google) or "s3" (for aws), if you would like to preserve your tf-state online
  required_providers ***REMOVED***
    google = ***REMOVED***
      source  = "hashicorp/google"
    ***REMOVED***
  ***REMOVED***
***REMOVED***

provider "google" ***REMOVED***
  project = var.project
  region = var.region
  // credentials = file(var.credentials)  # Use this if you do not want to set env-var GOOGLE_APPLICATION_CREDENTIALS
***REMOVED***

