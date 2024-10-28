import aws_cdk as core
import aws_cdk.assertions as assertions

from sdp_backend.sdp_backend_stack import SdpBackendStack

# example tests. To run these tests, uncomment this file along with the example
# resource in sdp_backend/sdp_backend_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = SdpBackendStack(app, "sdp-backend")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
