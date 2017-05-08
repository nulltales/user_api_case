
# Users API prototype

A prototype REST API using Django+DRF deployed serverlessly (?) on AWS Lambda.

## Local development

- Check out this repo.
- Make sure you have virtualenv installed [https://virtualenv.pypa.io/en/stable/installation/]()
- Run:

```sh
sudo pip install virtualenv        # If needed
make install                       # to install dependencies
make fixtures                      # to create the DB and populate with random users.
make test                          # to run tests
make serve                         # to run the local development server
```

## Deploy to lambda

- Make sure you have your ~/.aws/credentials file setup. [AWS Credentials](https://aws.amazon.com/blogs/security/a-new-and-standardized-way-to-manage-credentials-in-the-aws-sdks/) 

```sh
make install
source .venv/bin/activate          # Zappa requires this.
zappa certify demo                 # creates SSL endpoint
make deploystatic                  # uploads static files to S3
                                   # you will need valid AWS_ACCESS_KEY_ID  & AWS_SECRET_ACCESS_KEY in your env.
zappa deploy demo                  # deploys the lambda
zappa update demo                  # updates deployed lambda code

```
- Go to the URL zappa provides.
