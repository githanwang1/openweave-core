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
