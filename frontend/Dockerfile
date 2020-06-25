FROM golang:alpine3.11 as builder

RUN mkdir -p $GOPATH/src/frontend
COPY main.go $GOPATH/src/frontend 
COPY go.sum $GOPATH/src/frontend 
COPY go.mod $GOPATH/src/frontend 
COPY templates $GOPATH/bin/templates

WORKDIR $GOPATH/src/frontend
RUN go build -o $GOPATH/bin/frontend main.go

WORKDIR  $GOPATH/bin/

ENTRYPOINT ["./frontend"]

EXPOSE 8080
