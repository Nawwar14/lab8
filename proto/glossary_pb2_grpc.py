# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import glossary_pb2 as glossary__pb2


class GlossaryServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddTerm = channel.unary_unary(
                '/glossary.GlossaryService/AddTerm',
                request_serializer=glossary__pb2.Term.SerializeToString,
                response_deserializer=glossary__pb2.TermResponse.FromString,
                )
        self.GetTerm = channel.unary_unary(
                '/glossary.GlossaryService/GetTerm',
                request_serializer=glossary__pb2.Keyword.SerializeToString,
                response_deserializer=glossary__pb2.Term.FromString,
                )
        self.GetAllTerms = channel.unary_unary(
                '/glossary.GlossaryService/GetAllTerms',
                request_serializer=glossary__pb2.Empty.SerializeToString,
                response_deserializer=glossary__pb2.TermsList.FromString,
                )
        self.UpdateTerm = channel.unary_unary(
                '/glossary.GlossaryService/UpdateTerm',
                request_serializer=glossary__pb2.Term.SerializeToString,
                response_deserializer=glossary__pb2.TermResponse.FromString,
                )
        self.DeleteTerm = channel.unary_unary(
                '/glossary.GlossaryService/DeleteTerm',
                request_serializer=glossary__pb2.Keyword.SerializeToString,
                response_deserializer=glossary__pb2.TermResponse.FromString,
                )


class GlossaryServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AddTerm(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTerm(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllTerms(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateTerm(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteTerm(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GlossaryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddTerm': grpc.unary_unary_rpc_method_handler(
                    servicer.AddTerm,
                    request_deserializer=glossary__pb2.Term.FromString,
                    response_serializer=glossary__pb2.TermResponse.SerializeToString,
            ),
            'GetTerm': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTerm,
                    request_deserializer=glossary__pb2.Keyword.FromString,
                    response_serializer=glossary__pb2.Term.SerializeToString,
            ),
            'GetAllTerms': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllTerms,
                    request_deserializer=glossary__pb2.Empty.FromString,
                    response_serializer=glossary__pb2.TermsList.SerializeToString,
            ),
            'UpdateTerm': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateTerm,
                    request_deserializer=glossary__pb2.Term.FromString,
                    response_serializer=glossary__pb2.TermResponse.SerializeToString,
            ),
            'DeleteTerm': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteTerm,
                    request_deserializer=glossary__pb2.Keyword.FromString,
                    response_serializer=glossary__pb2.TermResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'glossary.GlossaryService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GlossaryService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AddTerm(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/glossary.GlossaryService/AddTerm',
            glossary__pb2.Term.SerializeToString,
            glossary__pb2.TermResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTerm(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/glossary.GlossaryService/GetTerm',
            glossary__pb2.Keyword.SerializeToString,
            glossary__pb2.Term.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAllTerms(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/glossary.GlossaryService/GetAllTerms',
            glossary__pb2.Empty.SerializeToString,
            glossary__pb2.TermsList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateTerm(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/glossary.GlossaryService/UpdateTerm',
            glossary__pb2.Term.SerializeToString,
            glossary__pb2.TermResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteTerm(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/glossary.GlossaryService/DeleteTerm',
            glossary__pb2.Keyword.SerializeToString,
            glossary__pb2.TermResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
