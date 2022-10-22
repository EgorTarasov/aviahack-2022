from tortoise import fields, Model


class Task(Model):
    id = fields.UUIDField(pk=True)
    taskState = fields.CharField(max_length=256)
    busState = fields.JSONField()
    driver = fields.UUIDField()
    distance = fields.IntField()  # метры
    flight = fields.CharField(max_length=256)
    startPoint = fields.IntField()  # id точки начала
    endPoint = fields.IntField()


class Flight(Model):
    date = fields.IntField()  # Unixtime
    type = fields.CharField(max_length=256)  # A - прилет, D - вылет
    terminal = fields.CharField(max_length=256)
    # код авиакомпании
    number = fields.IntField()
    scheduledTime = fields.IntField()
    airportCode = fields.CharField(max_length=256)
    airport = fields.CharField(max_length=256)
    planeType = fields.CharField(max_length=256)
    parkingId = fields.CharField(max_length=256)
    gateId = fields.CharField(max_length=256)
    passengersCount = fields.IntField()


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
    state = fields.CharField(max_length=256)


class BusState(Model):
    label = fields.CharField(max_length=256)
    duration = fields.IntField()
    order = (
        fields.IntField()
    )  # порядок состояния (посадка -> движение -> высадка, ожидание)


class Goal(Model):
    id = fields.UUIDField(pk=True)
    name = fields.TextField()
    # tasks = fields.ManyToManyField('models.Task', related_name='tasks', through='goal_task')

    user = fields.ForeignKeyField("users.User", related_name="goals")
