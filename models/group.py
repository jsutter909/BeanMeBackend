from mongoengine import (Document,
                         EmbeddedDocument,
                         EmbeddedDocumentField,
                         ListField,
                         StringField,
                         IntField)


class ScheduledTask(EmbeddedDocument):

    taskId = StringField(db_field="taskID", required=True)
    interval = IntField(db_field="timeInMS", required=True)

class GroupUser(EmbeddedDocument):

    userId = StringField(db_field="userID", required=True)
    beans = IntField(db_field="numBeans", required=True)


class Groups(Document):

    name = StringField(db_field="groupName", required=True)
    users = ListField(EmbeddedDocumentField(GroupUser), db_field="userList", required=True)
    scheduledTasks = ListField(StringField(), db_field="scheduledTasks", required=True)
    invitedUsers = ListField(StringField(db_field="invitedUsers", required=True))

