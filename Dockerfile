FROM golang:1.19-alpine3.17

WORKDIR /workspace

COPY go.mod go.sum /workspace/
RUN go mod download

COPY cmd /workspace/cmd
COPY internal /workspace/internal
COPY version.go /workspace/version.go

RUN CGO_ENABLED=0 go build -ldflags "-s -w" -trimpath -buildvcs=false -o /fern-go ./cmd/fern-go

CMD ["/fern-go"]
