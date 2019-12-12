#
#   Copyright (c) 2019 Google LLC.
#   Copyright (c) 2016-2018 Nest Labs, Inc.
#   All rights reserved.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from nestlabs.gateway.v2 import gateway_api_pb2 as nestlabs_dot_gateway_dot_v2_dot_gateway__api__pb2


class GatewayServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Observe = channel.unary_stream(
        '/nestlabs.gateway.v2.GatewayService/Observe',
        request_serializer=nestlabs_dot_gateway_dot_v2_dot_gateway__api__pb2.ObserveRequest.SerializeToString,
        response_deserializer=nestlabs_dot_gateway_dot_v2_dot_gateway__api__pb2.ObserveResponse.FromString,
        )


class GatewayServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Observe(self, request, context):
    """Requests current and future updates to a Resource instance's state.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_GatewayServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Observe': grpc.unary_stream_rpc_method_handler(
          servicer.Observe,
          request_deserializer=nestlabs_dot_gateway_dot_v2_dot_gateway__api__pb2.ObserveRequest.FromString,
          response_serializer=nestlabs_dot_gateway_dot_v2_dot_gateway__api__pb2.ObserveResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'nestlabs.gateway.v2.GatewayService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
