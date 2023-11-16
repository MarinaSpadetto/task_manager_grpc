import grpc
import time
import uuid
import task_pb2
import task_pb2_grpc
from concurrent import futures


_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class TaskService(task_pb2_grpc.TaskServiceServicer):

    def CreateTask(self, request, context):
        # print(f"Received request: {request}")
        task_id = str(uuid.uuid4())
        task = task_pb2.Task(id=task_id, title=request.title, completed=request.completed)
        # print(f"Sending response: {task}")
        return task

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    task_pb2_grpc.add_TaskServiceServicer_to_server(TaskService(), server)
    server.add_insecure_port('0.0.0.0:50051')
    server.start()
    print("Server started. Listening on port 50051...")
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
