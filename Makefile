EXCLUDE_DIRS = files notifier backup logs
PROTO_FILE = $(firstword $(wildcard *.proto))
PROTO_SUBDIR = proto/$(basename $(notdir $(PROTO_FILE)))

define CONNECT_GO_CONTENT
package finance

import "github.com/thedivinez/go-libs/utils"

func Connect(addr string) (PaymentClient, error) {
	conn, err := utils.ConnectService(addr)
	if err != nil {
		return nil, err
	}
	return NewPaymentClient(conn), nil
}
endef

export CONNECT_GO_CONTENT

proto:
	@echo "Generating protobuf files..."
	mkdir -p $(PROTO_SUBDIR)
	python3 -m grpc_tools.protoc -I. \
		--python_out=./proto \
		--grpc_python_out=./proto \
		--pyi_out=./proto ./*.proto
	sed -i 's/import finance_pb2 as/import proto.finance_pb2 as/' proto/finance_pb2_grpc.py
	protoc \
	--go_out=$(PROTO_SUBDIR)/ --go_opt=paths=source_relative \
	--go-grpc_out=require_unimplemented_servers=false:$(PROTO_SUBDIR)/ \
	--go-grpc_opt=paths=source_relative $(PROTO_FILE)
	@echo "Creating connect.go file..."
	@echo "$$CONNECT_GO_CONTENT" > $(PROTO_SUBDIR)/connect.go
	@echo "✅ $(PROTO_SUBDIR)/connect.go file created!"
	@echo "Cleaning up generated files..."
	protoc-go-inject-tag -remove_tag_comment -input="proto/**/*.pb.go"
	@echo "Copying to all projects (excluding current)..."
	@for dir in ../*/; do \
		clean_dir=$${dir%/}; \
		dir_name=$$(basename "$$clean_dir"); \
		skip=0; \
		for exclude in $(EXCLUDE_DIRS); do \
			if [ "$$dir_name" = "$$exclude" ]; then \
				skip=1; \
				break; \
			fi; \
		done; \
		if [ "$$(cd "$$clean_dir" && pwd)" != "$$(pwd)" ] && [ $$skip -eq 0 ]; then \
			dest_path="$$clean_dir/$(PROTO_SUBDIR)"; \
			echo "  -> $$dest_path"; \
			rm -rf "$$dest_path"; \
			mkdir -p "$$dest_path"; \
			cp -r $(PROTO_SUBDIR)/* "$$dest_path"/ 2>/dev/null || echo "⚠️  No files to copy"; \
		elif [ $$skip -eq 1 ]; then \
			echo "  Skipping '$$dir_name' directory: $$clean_dir"; \
		fi; \
	done
	rm -rf $(PROTO_SUBDIR)
	@echo "✅ Proto generation completed!"

run: 
	python3 main.py

.PHONY: proto