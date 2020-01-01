import boto3

from decouple import config
from django.core.management.base import BaseCommand
from coupon.models import Brand


class Command(BaseCommand):
    help = "Uploads brand and coupon catalogues to aws dynamodb"

    def handle(self, *args, **kwargs):
        dynamodb_resource = boto3.resource(
            "dynamodb",
            region_name=config("AWS_REGION_NAME"),
            aws_access_key_id=config("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=config("AWS_SECRET_ACCESS_KEY"),
        )

        table_name = "brands"
        existing_tables = [table.name for table in dynamodb_resource.tables.all()]

        if table_name not in existing_tables:
            self.stdout.write("Table not found.. creating..")
            dynamodb_resource.create_table(
                AttributeDefinitions=[
                    {"AttributeName": "id", "AttributeType": "N"},
                ],
                KeySchema=[
                    {"AttributeName": "id", "KeyType": "HASH"},
                ],
                ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
                TableName=table_name,
            )

        table = dynamodb_resource.Table(table_name)
        if table.table_status == 'ACTIVE':
            with table.batch_writer() as batch:
                for brand in Brand.objects.all():
                    batch.put_item(
                        Item={"id": brand.pk, "name": brand.name},
                    )
        else:
            self.stdout.write("No record created.")

        self.stdout.write("done")
