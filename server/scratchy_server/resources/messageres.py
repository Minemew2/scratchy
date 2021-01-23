import uuid
from flask_restful import Resource, abort, request
from scratchy_server.model.messageModel import MessageModel
from scratchy_server.database import database

class MessageRes(Resource):
    def get(self, MessageId):
        if not MessageId in database["messages"]:
            abort(404)

        return database["messages"][messageId].__dict__

    def post(self):
        messageData = request.get_json()
        message = messageModel()
        message.id = uuid.uuid4().hex
        message.content = messageData['content'] if 'content' in messageData else "Empty message"
        message.author = messageData['author'] if 'author' in messageData else "/-\|/|0|/|ym0|_|5"
        message.timestamp = messageData['timestamp'] if 'timestamp' in messageData else 000000
        if not "roomId" in messageData :
            abort(400)
        message.roomId = messageData['roomId']



        database['messages'][message.id] = message
        return message.__dict__

    def delete(self, messageId):
        if not messageId in database["messages"]:
            abort(404)

        if messageId in database["messages"]:
            del database["messages"][messageId]