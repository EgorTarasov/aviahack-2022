from tortoise import fields, Model


class Task(Model):
    id = fields.UUIDField(pk=True)
    journal = fields.ForeignKeyField("task.Journal", related_name="tasks")
    scheduledTime = fields.IntField()
    taskState = fields.CharField(max_length=256)
    bus = fields.IntField()
    distance = fields.IntField()  # метры
    flight = fields.CharField(max_length=256)
    # startPoint = fields.IntField()  # id точки начала
    # endPoint = fields.IntField()


class Journal(Model):
    id: int
    flight = fields.ForeignKeyField("task.Flight", related_name="journals")
    currentTask: int
    # Tasks: [Task]


class Flight(Model):
    number = fields.IntField(pk=True)
    date = fields.IntField()  # Unixtime
    type = fields.CharField(max_length=256)  # A - прилет, D - вылет
    terminal = fields.CharField(max_length=256)
    # код авиакомпании
    scheduledTime = fields.IntField()
    airportCode = fields.CharField(max_length=256)
    airport = fields.CharField(max_length=256)
    planeType = fields.CharField(max_length=256)
    parkingId = fields.CharField(max_length=256)
    gateId = fields.CharField(max_length=256)
    passengersCount = fields.IntField()

    class Meta:
        ordering = ["date"]


class Point(Model):
    pointId = fields.IntField(pk=True)
    locationId = fields.CharField(max_length=256)


class Road(Model):
    id = fields.IntField(pk=True)
    sourceId = fields.IntField()
    targetId = fields.IntField()
    distance = fields.IntField()


class Bus(Model):
    id = fields.UUIDField(pk=True)
    driver = fields.UUIDField(null=True)
    journal = fields.ForeignKeyField("task.Journal", "bus")
    state = fields.CharField(max_length=256)
    point = fields.CharField(max_length=256)


class BusState(Model):
    label = fields.CharField(max_length=256)
    duration = fields.IntField()
    order = (
        fields.IntField()
    )  # порядок состояния (посадка -> движение -> высадка, ожидание)
