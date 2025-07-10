proto-gen-py:
	python3 -m grpc_tools.protoc -I. \
		--python_out=./proto \
		--grpc_python_out=./proto \
		--pyi_out=./proto ./*.proto

proto-clean-py:
	sed -i 's/import finance_pb2 as/import proto.finance_pb2 as/' proto/finance_pb2_grpc.py

proto-gen-go:
	protoc \
		--proto_path=. \
		--go_out=../go-libs/finance --go_opt=paths=source_relative \
		--go-grpc_out=../go-libs/finance --go-grpc_opt=paths=source_relative,require_unimplemented_servers=false ./finance.proto

proto-clean-go:
	protoc-go-inject-tag -remove_tag_comment -input="../go-libs/finance/*.pb.go"

proto: proto-gen-py proto-clean-py proto-gen-go proto-clean-go

run: 
	python3 main.py

.PHONY: proto