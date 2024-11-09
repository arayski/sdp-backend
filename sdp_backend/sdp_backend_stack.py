from aws_cdk import (
    Stack,
    aws_lambda,
)
from constructs import Construct
import os

class SdpBackendStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # ========== Lambda Definitions ==================================

        test_function1 = aws_lambda.Function(
            self, "Function1",
            runtime = aws_lambda.Runtime.PYTHON_3_12,
            handler="lambda_function.py",
            code=aws_lambda.Code.from_asset("lambdas/test1")
        )

        test_function2 = aws_lambda.Function(
            self, "Function2",
            runtime = aws_lambda.Runtime.PYTHON_3_12,
            handler="lambda_function.py",
            code=aws_lambda.Code.from_asset("lambdas/test2")
        )
