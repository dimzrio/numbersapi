FROM golang:alpine3.11 as builder

RUN mkdir -p $GOPATH/src/backend
COPY main.go $GOPATH/src/backend
COPY go.mod $GOPATH/src/backend

WORKDIR $GOPATH/src/backend
RUN go build -o $GOPATH/bin/backend main.go

WORKDIR  $GOPATH/bin/

ENTRYPOINT ["./backend"]

EXPOSE 8080
