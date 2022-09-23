from peewee import Model, \
    CharField, \
    DecimalField, \
    DateField, \
    PostgresqlDatabase

db = PostgresqlDatabase(
    database="",
    password="",
    user="postgres",
    host="localhost",
    port=5432
)


class Data(Model):
    link_of_photo = CharField(max_length=255)
    date_posted = DateField()
    price = DecimalField()

    class Meta:
        database = db


db.connect()
db.create_tables([Data])



