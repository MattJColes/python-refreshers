# python-refreshers
Matt's Python refreshers for data:

## Pre-requisites:
* Make sure to have an AWS account setup
* Have [AWS Cloud9](https://catalog.us-east-1.prod.workshops.aws/workshops/3d705026-9edc-40e8-b353-bdabb116c89c/en-US/get-started/console) installed - or if running locally - a version of [Python above 3.6](https://www.python.org/downloads/) and [VSCode](https://code.visualstudio.com/download) installed
* If you get an `aws credentials` error make sure you have the AWS CLI installed and configured with a `aws configure` command: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

## Week 1 & 2 - Python basics
Let's start learning!

#### [Learn Python On AWS Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/3d705026-9edc-40e8-b353-bdabb116c89c/en-US)

## Week 3
All about reading and writing data!

#### Reading and Writing CSV's
[Tutorial](https://realpython.com/python-interview-problem-parsing-csv-files/) - Start with this snippet for Reading and Writing CSV's:
``` python
import csv


def get_next_result(csv_file, func):
    for stats in csv.DictReader(csv_file):
        yield func(stats)
```
#### Read and write CSV's from S3
[Tutorial](https://www.stackvidhya.com/write-pandas-dataframe-as-csv-to-s3-using-boto3/)

Additional tutorial reading on Pandas, CSV's, Excel Sheets
* [Using Pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
* [Manipulating Spreadsheets](https://realpython.com/openpyxl-excel-spreadsheets-python/)

## Week 4
Secrets and visualising data

#### Managing secrets safely in AWS:
[Tutorial](https://hands-on.cloud/working-with-secrets-manager-in-python-using-boto3/)

#### Avoiding using your AWS credentials on servers and have a special AWS IAM role:
[Tutorial](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html)

#### Visualising data with Matlib Plot
[Tutorial](https://matplotlib.org/stable/tutorials/introductory/index.html)

#### Using Seaborn for additional visualisations
[Tutorial](https://www.geeksforgeeks.org/python-seaborn-tutorial/)

## Week 5
#### Boto3 and Redshift
[Tutorial](https://hevodata.com/learn/boto3-redshift/)
* [Glue and Boto3](https://www.1week4.com/it/aws/aws-glue-tutorial-boto3/)

---

## Additional Content:

* [DynamoDB and Python](https://catalog.us-east-1.prod.workshops.aws/workshops/3d705026-9edc-40e8-b353-bdabb116c89c/en-US/persisting-data/dynamodb)
* [SAM for Lambdas written in Python](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-getting-started-hello-world.html)
* [PyTest](https://realpython.com/pytest-python-testing/)
* [OOP Fundamentals](https://realpython.com/python3-object-oriented-programming/#parent-classes-vs-child-classes)
* [Data Classes](https://realpython.com/python-data-classes/)
* 


## Week 7 and 8 - All about Flask
* [Learning Flask](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

## Week 9 and 10 - Creating AWS infrastructure with Python
* [CDK and Python](https://cdkworkshop.com/30-python.html)

## Week 11 - Let's build a chatbot with Python and LEX
* [LEX Chatbots](https://github.com/MattJColes/amazon-lex-amplify-workshop/tree/master/lab1-Building_Chat_Bots_With_Lex)

## Week 12 - Final Journey
* Golden Paths!!!

### Extras!
* [Pygame](https://www.techwithtim.net/tutorials/game-development-with-python/pygame-tutorial/)
