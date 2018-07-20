# example-authz-registry
This is an example repo to show a way that's used by UChicago group to manage ACL to access commons

The repository is supposed to be used by the authorization list maintainers who add/remove people from projects, and make pull request( example [pull request](https://github.com/DataBiosphere/example-authz-registry/pull/1)) to be approved so that the history of changes are all version tracked in github.

When the pull request is made, a travis build is triggered to do some basic checking to make sure the user file is not malformed. After the pull request is merged, a travis build is triggered to push the file to a S3 bucket. Then you can setup listeners in AWS to trigger downstream auth updates on various systems.

## Setup
To setup a real authz registry, you need to enable travisCI, create an AWS S3 bucket, and create a aws bot keypairs to let Travis push the user file to S3. The credentials will be encrypted by Travis's private key. Travis is free for public repository and [pricing](https://travis-ci.com/plans) is here for private ones. There are other [CI tools](https://github.com/marketplace/category/continuous-integration) that does similar job.
