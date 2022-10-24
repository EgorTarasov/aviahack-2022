FROM golang:alpine as builder

WORKDIR /build/
COPY go.mod .
COPY go.sum .
RUN go mod download
COPY . /build/
RUN go build -o main ./cmd/main

FROM alpine
COPY --from=builder /build/main /app/
WORKDIR /app
CMD ["./main"]
